"""One test from a seed and a mode: x up to 10^6 that is not a square
and k; mode 1 small x and k, mode 2 any x and k up to 10^9, mode 3 x
just below a square, which gives a short period, and a large k."""

import random
import sys
from math import isqrt

LIMIT_X = 10 ** 6
LIMIT_K = 10 ** 9
SMALL = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            x, k = rng.randint(2, SMALL), rng.randint(0, SMALL)
        elif mode == 2:
            x, k = rng.randint(2, LIMIT_X), rng.randint(0, LIMIT_K)
        else:
            r = rng.randint(2, isqrt(LIMIT_X))
            x, k = r * r - rng.randint(1, 2), rng.randint(0, LIMIT_K)
        if isqrt(x) ** 2 != x and x >= 2:
            break
    print(x, k)


main()
