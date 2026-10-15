"""One test from a seed and a mode: mode 1 any valid R, r, d, mode 2
concentric circles, mode 3 a ring as thin as the integers allow, mode 4
small numbers."""

import random
import sys

MOST = 100
SMALL = 20


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    big = rng.randint(2, SMALL if mode == 4 else MOST)
    d = 0 if mode == 2 else rng.randint(0, big - 2)
    small = big - d - 1 if mode == 3 else rng.randint(1, big - d - 1)
    print(big, small, d)


main()
