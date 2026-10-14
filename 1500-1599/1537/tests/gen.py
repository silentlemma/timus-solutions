"""One test from a seed and a mode: mode 1 takes random K and P, mode 2 a
K near 10^7 and P near 10^9, mode 3 a small K and a small P."""

import random
import sys

TOP_K = 10**7
TOP_P = 10**9
NEAR = 1000
SMALL = 100


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        k, p = rng.randint(1, TOP_K), rng.randint(1, TOP_P)
    elif mode == 2:
        k, p = TOP_K - rng.randint(0, NEAR), TOP_P - rng.randint(0, NEAR)
    else:
        k, p = rng.randint(1, SMALL), rng.randint(1, SMALL)
    print(k, p)


main()
