"""Usage: gen.py SEED MODE.

Modes: wide,tall,snake,comb,ladder,adjacent,barrier,irregular,irregular_tall.
Large fields have 100000 cells; ladder is 2 by 1000.
"""

import random
import sys

LONG_SIDE = 1000
SHORT_SIDE = 100


def generate(seed, mode):
    rows, cols = SHORT_SIDE, LONG_SIDE
    if mode == "tall":
        rows, cols = LONG_SIDE, SHORT_SIDE
    elif mode == "ladder":
        rows = 2
    elif mode == "snake":
        rows, cols = LONG_SIDE, SHORT_SIDE
    grid = [bytearray(b"#" * cols) for _ in range(rows)]
    start, target = (0, 0), (rows - 1, cols - 1)
    if mode == "snake":
        for row in range(rows):
            if row % 2 == 0:
                grid[row][:] = b"." * cols
            else:
                col = cols - 1 if (row // 2) % 2 == 0 else 0
                grid[row][col] = ord(".")
        target = rows - 1, 0
    elif mode == "comb":
        grid[0][:] = b"." * cols
        for row in range(1, rows):
            for col in range(0, cols, 2):
                grid[row][col] = ord(".")
        target = 0, cols - 1
    elif mode in ("irregular", "irregular_tall"):
        rng = random.Random(seed)
        middle = rows // 2
        for row in range(rows):
            for col in range(cols):
                boundary = row in (0, rows - 1) or col in (0, cols - 1)
                if boundary or row == middle or rng.random() < 0.62:
                    grid[row][col] = ord(".")
        start, target = (middle, 0), (middle, cols - 1)
        if mode == "irregular_tall":
            grid = [bytearray(grid[r][c] for r in range(rows)) for c in range(cols)]
            rows, cols = cols, rows
            start, target = (0, middle), (rows - 1, middle)
    else:
        grid = [bytearray(b"." * cols) for _ in range(rows)]
        if mode == "adjacent":
            target = 0, 1
        elif mode == "ladder":
            target = 0, cols - 1
        elif mode == "barrier":
            middle = rows // 2
            for row in range(1, rows - 1):
                if row != middle:
                    grid[row][cols // 3 : 2 * cols // 3] = b"#" * (cols // 3)
            start, target = (middle, 0), (middle, cols - 1)
        elif mode not in ("wide", "tall"):
            raise ValueError("unknown mode")
    return [bytes(row) for row in grid], start, target


if __name__ == "__main__":
    grid, start, target = generate(int(sys.argv[1]), sys.argv[2])
    print(len(grid), len(grid[0]))
    print(start[0] + 1, start[1] + 1)
    print(target[0] + 1, target[1] + 1)
    for row in grid:
        print(row.decode("ascii"))
