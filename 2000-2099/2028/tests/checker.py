"""Accept any grid program computing every triangular sum for inputs 1 through 100."""

from pathlib import Path
import sys

ALPHABET = 26
VALUE_LIMIT = 100000
TICKS = 1000000
TARGET_MAX = 100
UP = 3
OFFSETS = ((0, 1), (1, 0), (0, -1), (-1, 0))
ARROWS = {">": 0, "v": 1, "<": 2, "^": UP}
OPERATORS = set("^>v<.ABCDEFGHIJKLMNOPQRSTUVWXYZ?!+-@#")


def parse_program(raw):
    try:
        tokens = raw.decode("ascii").split()
        if len(tokens) < 2:
            return None
        height, width = map(int, tokens[:2])
    except (ValueError, UnicodeDecodeError):
        return None
    if not (1 <= height <= TARGET_MAX and 1 <= width <= TARGET_MAX):
        return None
    grid = tokens[2:]
    if len(grid) != height or any(len(row) != width or set(row) - OPERATORS for row in grid):
        return None
    return grid


def run_vm(grid, values, output_limit=None):
    row = column = direction = current = cursor = maximum = 0
    memory = [0] * ALPHABET
    output = []
    for tick in range(1, TICKS + 1):
        op = grid[row][column]
        if op == "#":
            return output, "halt", tick, maximum
        if op in ARROWS:
            direction = ARROWS[op]
        elif "A" <= op <= "Z":
            index = ord(op) - ord("A")
            current, memory[index] = memory[index], current
        elif op == "?":
            current = values[cursor]
            if cursor + 1 < len(values):
                cursor += 1
        elif op == "!":
            output.append(str(current))
            current = 0
            if output_limit is not None and len(output) > output_limit:
                return output, "excess-output", tick, maximum
        elif op == "+":
            current += 1
        elif op == "-":
            current -= 1
        elif op == "@":
            direction = (direction + (-1 if current == 0 else 1)) % len(OFFSETS)
        maximum = max(maximum, abs(current))
        if current < -VALUE_LIMIT or current > VALUE_LIMIT:
            return output + ["OVERFLOW ERROR"], "overflow", tick, maximum
        dr, dc = OFFSETS[direction]
        row, column = row + dr, column + dc
        if not (0 <= row < len(grid) and 0 <= column < len(grid[0])):
            return output + ["RUNTIME ERROR"], "runtime", tick, maximum
    return output + ["TIME LIMIT EXCEEDED"], "time", TICKS, maximum


def check_program(raw):
    grid = parse_program(raw)
    if grid is None:
        return False
    for n in range(1, TARGET_MAX + 1):
        output, reason, _ticks, _maximum = run_vm(grid, [n], output_limit=1)
        if reason != "halt" or output != [str(sum(range(1, n + 1)))]:
            return False
    return True


def main():
    actual = Path(sys.argv[3]).read_bytes()
    if not check_program(actual):
        print(
            "Invalid grid or not a normally terminating triangular-sum program for every n=1..100"
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
