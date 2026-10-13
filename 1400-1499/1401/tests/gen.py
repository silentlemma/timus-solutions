"""Boards of 512 by 512: a seed and a mode. Mode 1 removes the top right
cell, mode 2 a cell in the middle, mode 3 a random cell, mode 4 the bottom
left cell."""

import random
import sys

N = 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    size = 1 << N
    x, y = {
        1: (1, size),
        2: (size // 2, size // 2 + 1),
        3: (rng.randint(1, size), rng.randint(1, size)),
        4: (size, 1),
    }[mode]
    print(N)
    print(x, y)


main()
