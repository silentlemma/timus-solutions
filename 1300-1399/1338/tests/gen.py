"""A 500 by 500 town and 20 experiments: a seed and a mode. Mode 1 gives
random roads with control points, mode 2 a grid of streets where many
shortest routes tie, mode 3 a long winding road with points along it,
mode 4 a town where every road cell is a control point. Mode 5 gives a
fully open rectangle of control points, mode 6 a single winding chain
with a point at every road cell, and mode 7 random rectangular roads
and points. Modes 5-7 accept optional width and height after the mode;
defaults are 500 by 500 for modes 5-6 and 41 by 17 for mode 7."""

import random
import sys

SIZE = 500
TESTS = 20
GAP = 3  # blocks between the streets in mode 2
DENSITY = {1: 0.6, 2: 0.05, 3: 0.02, 4: 1.0}  # how many road cells are points


def rectangle(seed, mode):
    rng = random.Random(seed)
    default = (41, 17) if mode == 7 else (SIZE, SIZE)
    w, h = map(int, sys.argv[3:5]) if len(sys.argv) > 3 else default
    assert 1 <= w <= SIZE and 1 <= h <= SIZE
    grid = []
    for r in range(h):
        row = []
        for c in range(w):
            if mode == 5:
                cell = "o"
            elif mode == 6:
                road = r % 2 == 0 or (
                    r < h - 1 and c == (w - 1 if r % 4 == 1 else 0)
                )
                cell = "o" if road else "."
            else:
                cell = "." if rng.random() >= 0.72 else (
                    "o" if rng.random() < 0.32 else "#"
                )
            row.append(cell)
        grid.append(row)
    points = sum(row.count("o") for row in grid)
    if not points:
        grid[0][0] = "o"
        points = 1
    targets = [1, points]
    if mode == 5:
        targets += [w, points - w + 1]
    elif mode == 6:
        targets += [min(w, points), min(w + 1, points), min(w + 2, points)]
    targets += [rng.randint(1, points) for _ in range(TESTS - len(targets))]
    print(w, h)
    for row in grid:
        print("".join(row))
    print(TESTS)
    print("\n".join(map(str, targets)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (5, 6, 7):
        rectangle(seed, mode)
        return
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
