"""One test from a seed and a mode. Mode 1 takes K, L and N up to 10^9,
mode 2 up to 10, mode 3 more matches than goals, mode 4 equal K and L."""

import random
import sys

TOP = 10**9
SMALL = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 2 else TOP
    scored, conceded, n = rng.randint(0, top), rng.randint(0, top), rng.randint(1, top)
    if mode == 3:
        scored, conceded = rng.randint(0, SMALL), rng.randint(0, SMALL)
    if mode == 4:
        conceded = scored
    print(scored, conceded, n)


main()
