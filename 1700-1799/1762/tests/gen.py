"""One test from a seed and a mode: mode 1 a small hall, mode 2 any hall
up to 1 000 000 tiles a side, mode 3 a hall whose sides less one share
a large common divisor."""

import random
import sys

FEW = 30
MOST = 1000000
SPREAD = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(2, FEW), rng.randint(2, FEW)
    elif mode == 2:
        n, m = rng.randint(2, MOST), rng.randint(2, MOST)
    else:
        g = rng.randint(1, MOST // SPREAD)
        n, m = g * rng.randint(1, SPREAD) + 1, g * rng.randint(1, SPREAD) + 1
    print(n, m)


main()
