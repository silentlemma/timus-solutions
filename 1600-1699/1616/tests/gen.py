"""One test from a seed and a mode: mode 1 a random map and angle, mode 2
the largest map with few owners in blocks, mode 3 an angle of 0 or 90,
mode 4 the largest map full of owners at a random angle, mode 5 a small
map at an angle with a short decimal form."""

import random
import sys

MOST = 30
RIGHT = 90
OWNERS = "abcdefghijklmnopqrstuvwxyz"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = MOST if mode in (2, 4) else rng.randint(1, MOST if mode == 1 else 6)
    side = 2 * n
    if mode == 3:
        alpha = "%d" % rng.choice([0, RIGHT])
    elif mode == 5:
        alpha = "%.1f" % rng.choice([15, 30, 45, 60, 22.5, 67.5])
    else:
        alpha = "%.6f" % rng.uniform(0, RIGHT)
    if mode == 2:
        # a few owners, each a block of cells
        grid = [["."] * side for _ in range(side)]
        for k in range(rng.randint(1, 5)):
            r0, c0 = rng.randrange(side), rng.randrange(side)
            h, w = rng.randint(1, side - r0), rng.randint(1, side - c0)
            for r in range(r0, r0 + h):
                for c in range(c0, c0 + w):
                    grid[r][c] = OWNERS[k]
    else:
        fill = 1.0 if mode == 4 else rng.random()
        letters = OWNERS[: rng.randint(1, len(OWNERS))]
        grid = [
            [rng.choice(letters) if rng.random() < fill else "." for _ in range(side)]
            for _ in range(side)
        ]
    print(n, alpha)
    for row in grid:
        print("".join(row))


main()
