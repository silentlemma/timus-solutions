from io import StringIO
import sys

ALPHABET = 26
VALUE_LIMIT = 100000
TICKS = 1000000
UP = 3
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
ARROWS = {">": 0, "v": 1, "<": 2, "^": UP}


def solve(grid, inputs):
    height, width = len(grid), len(grid[0])
    row = column = direction = current = cursor = 0
    memory = [0] * ALPHABET
    output = StringIO()
    write = output.write
    for _ in range(TICKS):
        op = grid[row][column]
        if op == "!":
            write(str(current) + "\n")
            current = 0
        elif op == "?":
            current = inputs[cursor]
            if cursor + 1 < len(inputs):
                cursor += 1
        elif op == "+":
            current += 1
        elif op == "-":
            current -= 1
        elif op == "@":
            direction = (direction + (-1 if current == 0 else 1)) % len(DIRECTIONS)
        elif op == "#":
            return output.getvalue()
        elif op in ARROWS:
            direction = ARROWS[op]
        elif "A" <= op <= "Z":
            index = ord(op) - ord("A")
            current, memory[index] = memory[index], current
        if current < -VALUE_LIMIT or current > VALUE_LIMIT:
            write("OVERFLOW ERROR\n")
            return output.getvalue()
        dr, dc = DIRECTIONS[direction]
        row += dr
        column += dc
        if row < 0 or row >= height or column < 0 or column >= width:
            write("RUNTIME ERROR\n")
            return output.getvalue()
    write("TIME LIMIT EXCEEDED\n")
    return output.getvalue()


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    height, _width = int(next(tokens)), int(next(tokens))
    grid = [next(tokens).decode("ascii") for _ in range(height)]
    count = int(next(tokens))
    inputs = [int(next(tokens)) for _ in range(count)]
    sys.stdout.write(solve(grid, inputs))


if __name__ == "__main__":
    main()
