"""One test from a seed and a mode: mode 1 any base and a few hundred
rifles, mode 2 any base and up to 50000 rifles, mode 3 the largest
count in a random base, mode 4 the largest count in base `seed`."""

import random
import sys

LIMIT = 50000
SMALL = 300
TOP_BASE = 10


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    k = rng.randint(2, TOP_BASE)
    if mode == 1:
        n = rng.randint(3, SMALL)
    elif mode == 2:
        n = rng.randint(3, LIMIT)
    elif mode == 3:
        n = LIMIT
    else:
        k, n = seed, LIMIT
    print(k, n)


main()
