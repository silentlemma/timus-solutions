"""A seed and a mode. Modes 1-4 use a 512 by 512 board: mode 1 removes
the top right cell, mode 2 a cell in the middle, mode 3 a random cell,
and mode 4 the bottom left cell. Mode 5 uses a 256 by 256 board with a
random cell removed."""

import random
import sys

N = 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = 8 if mode == 5 else N
    size = 1 << n
    random_cell = (rng.randint(1, size), rng.randint(1, size))
    x, y = {
        1: (1, size),
        2: (size // 2, size // 2 + 1),
        3: random_cell,
        4: (size, 1),
        5: random_cell,
    }[mode]
    print(n)
    print(x, y)


main()
