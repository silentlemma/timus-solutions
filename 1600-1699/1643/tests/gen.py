"""One test from a seed and a mode: a random map (mode 1 small, mode 2
100 by 100), with walls, teleports of a few letters and the three marks;
mode 3 is a 100 by 100 maze of walls with long corridors."""

import random
import sys

SIDE = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(1, 8), rng.randint(3, 8)
        if n * m < 3:
            n = 3
    else:
        n = m = SIDE
    wall = rng.uniform(0.1, 0.5) if mode != 3 else 0.0
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[: rng.randint(1, 26)]
    grid = []
    for r in range(n):
        row = []
        for c in range(m):
            if mode == 3:
                row.append("#" if r % 2 and c % (m // 2) != (r // 2) % 2 * 5 else ".")
                continue
            x = rng.random()
            if x < wall:
                row.append("#")
            elif x < wall + 0.03:
                row.append(rng.choice(letters))
            else:
                row.append(".")
        grid.append(row)
    cells = rng.sample([(r, c) for r in range(n) for c in range(m)], 3)
    for (r, c), mark in zip(cells, "$!*"):
        grid[r][c] = mark
    if mode == 3:
        for _ in range(4):
            r, c = rng.randrange(n), rng.randrange(m)
            if grid[r][c] in ".#":
                grid[r][c] = "Q"
    print(n, m)
    for row in grid:
        print("".join(row))


main()
