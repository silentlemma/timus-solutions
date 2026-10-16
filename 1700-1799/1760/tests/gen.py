"""One test from a seed and a mode: mode 1 small numbers, mode 2 any
numbers up to 25 000 000, mode 3 page sizes near the square root of
n, mode 4 page sizes with a large common divisor."""

import random
import sys

FEW = 60
MOST = 25000000
ROOT = 5000
SPREAD = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, FEW)
        a, b = rng.randint(1, n), rng.randint(1, n)
    elif mode == 2:
        n = rng.randint(MOST // 2, MOST)
        a, b = rng.randint(1, n), rng.randint(1, n)
    elif mode == 3:
        n = MOST
        a, b = rng.randint(ROOT - SPREAD, ROOT + SPREAD), rng.randint(ROOT - SPREAD, ROOT + SPREAD)
    else:
        n = MOST
        g = rng.randint(1, ROOT)
        a, b = g * rng.randint(1, SPREAD), g * rng.randint(1, SPREAD)
    print(a, b, n)


main()
