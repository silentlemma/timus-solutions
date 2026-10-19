"""Generate unique-answer grids: python gen.py MODE SEED."""

import random
import sys

MAX_SIDE = 500
MAX_QUERIES = 50
MAX_POWER = 100000
MAX_VALUE = 10**9
SMALL_SIDE = 10
MEDIUM_MIN = 20
MEDIUM_MAX = 40
MEDIUM_QUERIES = 10
REGION_DIVISOR = 3
ARGUMENTS = 3


def unique(grid, powers):
    height, width = len(grid), len(grid[0])
    prefixes = []
    for row in grid:
        prefix = [0]
        for value in row:
            prefix.append(prefix[-1] + value)
        prefixes.append(prefix)
    for power in set(powers):
        best, count = -1, 0
        for row in range(height):
            for col in range(width):
                total = 0
                for current in range(row, min(height, row + power + 1)):
                    end = min(width, col + power - current + row + 1)
                    total += prefixes[current][end] - prefixes[current][col]
                if total > best:
                    best, count = total, 1
                elif total == best:
                    count += 1
        if count != 1:
            return False
    return True


def random_grid(rng, mode):
    if mode == "small":
        height = rng.randint(1, SMALL_SIDE)
        width = rng.randint(1, SMALL_SIDE)
        count = rng.randint(1, MEDIUM_QUERIES)
    elif mode == "thin":
        height, width = 1, MAX_SIDE
        if rng.randrange(2):
            height, width = width, height
        count = MAX_QUERIES
    else:
        height = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        width = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        count = MEDIUM_QUERIES
    limit = height + width
    powers = [rng.randint(1, limit) for _ in range(count)]
    powers[0] = 1
    powers[-1] = MAX_POWER
    while True:
        grid = [[rng.randint(0, MAX_VALUE) for _ in range(width)] for _ in range(height)]
        # Certification avoids relying on random weights to break every tie.
        if unique(grid, powers):
            return grid, powers


def maximum_grid(rng, interior):
    if interior:
        first = rng.randint(MAX_SIDE // REGION_DIVISOR, MAX_SIDE // 2)
        left = rng.randint(MAX_SIDE // REGION_DIVISOR, MAX_SIDE // 2)
        grid = [[1] * MAX_SIDE for _ in range(MAX_SIDE)]
        for row in range(first, MAX_SIDE):
            for col in range(left, MAX_SIDE):
                grid[row][col] = MAX_VALUE - (row - first) - (col - left)
        # These small triangles fit inside the positive rectangle. Losing a
        # large cell costs more than all the differences between large cells.
        powers = list(range(1, MAX_QUERIES)) + [MAX_POWER]
    else:
        grid = [
            [MAX_VALUE - row * (MAX_SIDE + 1) - col for col in range(MAX_SIDE)]
            for row in range(MAX_SIDE)
        ]
        # Strict decrease and positivity make the top-left cell uniquely best.
        powers = [rng.randint(1, 2 * MAX_SIDE) for _ in range(MAX_QUERIES)]
        powers[0] = 1
        powers[1] = 2
        powers[-2] = 2 * MAX_SIDE - 2
        powers[-1] = MAX_POWER
    return grid, powers


def main():
    modes = ("small", "thin", "medium", "max", "interior")
    if len(sys.argv) != ARGUMENTS or sys.argv[1] not in modes:
        raise SystemExit("usage: gen.py {small,thin,medium,max,interior} SEED")
    mode = sys.argv[1]
    rng = random.Random(int(sys.argv[2]))
    if mode in ("max", "interior"):
        grid, powers = maximum_grid(rng, mode == "interior")
    else:
        grid, powers = random_grid(rng, mode)
    print(len(grid), len(grid[0]))
    for row in grid:
        print(*row)
    print(len(powers))
    print(*powers)


if __name__ == "__main__":
    main()
