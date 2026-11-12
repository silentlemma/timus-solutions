from io import StringIO
from itertools import islice
import sys


ARROWS = ">v<^"
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
REGISTERS = 26
VALUE_LIMIT = 100000
TICK_LIMIT = 1000000


def execute(grid, values, write):
    height, width = len(grid), len(grid[0])
    memory = [0] * REGISTERS
    row = column = direction = current = last = 0
    for _ in range(TICK_LIMIT):
        instruction = grid[row][column]
        match instruction:
            case "#":
                return
            case ">" | "v" | "<" | "^":
                direction = ARROWS.index(instruction)
            case "@":
                turn = -1 if current == 0 else 1
                direction = (direction + turn) % len(DIRECTIONS)
            case "?":
                last = next(values, last)
                current = last
            case "!":
                write(f"{current}\n")
                current = 0
            case "+":
                current += 1
            case "-":
                current -= 1
            case _ if "A" <= instruction <= "Z":
                index = ord(instruction) - ord("A")
                current, memory[index] = memory[index], current
        if abs(current) > VALUE_LIMIT:
            write("OVERFLOW ERROR\n")
            return
        dr, dc = DIRECTIONS[direction]
        row, column = row + dr, column + dc
        if not (0 <= row < height and 0 <= column < width):
            write("RUNTIME ERROR\n")
            return
    write("TIME LIMIT EXCEEDED\n")


def main():
    tokens = iter(sys.stdin.read().split())
    height, _width = int(next(tokens)), int(next(tokens))
    grid = [next(tokens) for _ in range(height)]
    count = int(next(tokens))
    values = map(int, islice(tokens, count))
    output = StringIO()
    execute(grid, values, output.write)
    sys.stdout.write(output.getvalue())


if __name__ == "__main__":
    main()
