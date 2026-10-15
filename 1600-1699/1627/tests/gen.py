"""One test from a seed and a mode: mode 1 a random size and a few
pantries, mode 2 the full 9 x 9 house, mode 3 many pantries (often split
into parts), mode 4 a single row or column."""

import random
import sys

SIDE = 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        n = m = SIDE
    elif mode == 4:
        n, m = (1, rng.randint(1, SIDE)) if rng.random() < 0.5 else (rng.randint(1, SIDE), 1)
    else:
        n, m = rng.randint(1, SIDE), rng.randint(1, SIDE)
    chance = {1: 0.1, 2: 0.0, 3: 0.4, 4: 0.1}[mode]
    grid = [["*" if rng.random() < chance else "." for _ in range(m)] for _ in range(n)]
    if all(c == "*" for row in grid for c in row):
        grid[rng.randrange(n)][rng.randrange(m)] = "."
    print(n, m)
    for row in grid:
        print("".join(row))


main()
