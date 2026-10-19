"""Generate valid grids; the minimum jump height is always a unique integer."""

import random
import sys

MAX_SIZE = 100
MAX_HEIGHT = 100000
SMALL_SIZE = 6
PALETTE_SIZE = 5
STEP = 137
MODE_SMALL = 1
MODE_RANDOM = 2
MODE_MAXIMUM = 3
MODE_FLAT = 4
MODE_LATE_ESCAPE = 5
MODE_SLOPE = 6
MODE_CHECKERBOARD = 7
MODE_BASIN = 8
MODE_ROW = 9
MODE_COLUMN = 10
MODE_DRY_START = 11
MODE_BLOCKED = 12
MODE_TERRACES = 13
MODE_DEADLINE = 14


def generate(mode, seed):
    rng = random.Random(seed)
    rows = MAX_SIZE
    columns = MAX_SIZE
    if mode == MODE_SMALL:
        rows = rng.randint(1, SMALL_SIZE)
        columns = rng.randint(1, SMALL_SIZE)
        if rows * columns == 1:
            columns = 2
    elif mode in (MODE_RANDOM, MODE_BASIN, MODE_TERRACES):
        rows = rng.randint(2, MAX_SIZE)
        columns = rng.randint(2, MAX_SIZE)
    elif mode == MODE_ROW:
        rows = 1
    elif mode == MODE_COLUMN:
        columns = 1
    cells = rows * columns
    start, source = rng.sample(range(cells), 2)
    if mode == MODE_SMALL:
        palette = [0, 1, 2, 10, MAX_HEIGHT]
        grid = [rng.choice(palette) for _ in range(cells)]
    elif mode in (MODE_RANDOM, MODE_MAXIMUM):
        grid = [rng.randint(0, MAX_HEIGHT) for _ in range(cells)]
    elif mode == MODE_FLAT:
        grid = [rng.randint(0, MAX_HEIGHT)] * cells
    elif mode == MODE_LATE_ESCAPE:
        grid = [0] * cells
        grid[-1] = MAX_HEIGHT
        start, source = 1, 0
    elif mode == MODE_SLOPE:
        grid = [(row + column) * STEP for row in range(rows) for column in range(columns)]
        start, source = 0, cells - 1
    elif mode == MODE_CHECKERBOARD:
        low = rng.randint(0, MAX_HEIGHT // 2)
        high = rng.randint(low + 1, MAX_HEIGHT)
        grid = [
            high if (row + column) % 2 else low for row in range(rows) for column in range(columns)
        ]
        start, source = columns + 1, 1
    elif mode == MODE_BASIN:
        low = rng.randint(0, MAX_HEIGHT // 2)
        grid = [low] * cells
        for cell in range(cells):
            if rng.randrange(PALETTE_SIZE) == 0:
                grid[cell] = rng.randint(low + 1, MAX_HEIGHT)
        grid[start] = low
        grid[source] = low
    elif mode in (MODE_ROW, MODE_COLUMN):
        grid = [rng.randrange(PALETTE_SIZE) for _ in range(cells)]
    elif mode == MODE_DRY_START:
        grid = [rng.randint(1, MAX_HEIGHT) for _ in range(cells)]
        grid[source] = 0
    elif mode == MODE_BLOCKED:
        grid = [0] * cells
        for row in range(rows):
            grid[row * columns] = MAX_HEIGHT
        start, source = 2, 1
    elif mode == MODE_TERRACES:
        grid = [
            min(MAX_HEIGHT, (row // 2 + column // 2) * STEP)
            for row in range(rows)
            for column in range(columns)
        ]
    elif mode == MODE_DEADLINE:
        grid = [0] * cells
        grid[columns - 1] = MAX_HEIGHT
        source = columns - 2
        start = 0
    else:
        raise SystemExit("unknown mode")
    return rows, columns, grid, start, source


def main():
    mode, seed = map(int, sys.argv[1:])
    rows, columns, grid, start, source = generate(mode, seed)
    print(rows, columns)
    for row in range(rows):
        print(*grid[row * columns : (row + 1) * columns])
    print(start // columns + 1, start % columns + 1)
    print(source // columns + 1, source % columns + 1)


if __name__ == "__main__":
    main()
