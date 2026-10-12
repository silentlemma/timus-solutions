"""A 500 by 500 town and 20 experiments: a seed and a mode. Mode 1 gives
random roads with control points, mode 2 a grid of streets where many
shortest routes tie, mode 3 a long winding road with points along it,
mode 4 a town where every road cell is a control point."""

import random
import sys

SIZE = 500
TESTS = 20
GAP = 3  # blocks between the streets in mode 2
DENSITY = {1: 0.6, 2: 0.05, 3: 0.02, 4: 1.0}  # how many road cells are points


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    grid = [["."] * SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        for c in range(SIZE):
            if mode in (1, 4):
                road = rng.random() < DENSITY[1]
            elif mode == 2:
                road = r % GAP == 0 or c % GAP == 0
            else:
                road = r % 2 == 0 or (c == SIZE - 1 if r % 4 == 1 else c == 0)
            if road:
                grid[r][c] = "o" if rng.random() < DENSITY[mode] else "#"
    points = sum(row.count("o") for row in grid)
    if points == 0:
        grid[0][0] = "o"
        points = 1
    print(SIZE, SIZE)
    for row in grid:
        print("".join(row))
    print(TESTS)
    for _ in range(TESTS):
        print(rng.randint(1, points))


main()
