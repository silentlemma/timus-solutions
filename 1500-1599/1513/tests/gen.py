"""One test from a seed and a mode: mode 1 takes a random N up to 10000
and a random K, mode 2 takes N = 10000 and a small K, mode 3 takes a small
N and a random K."""

import random
import sys

LARGEST = 10000
SMALL = 12


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = {1: rng.randint(1, LARGEST), 2: LARGEST}.get(mode, rng.randint(1, SMALL))
    k = rng.randint(0, SMALL) if mode == 2 else rng.randint(0, n)
    print(n, k)


main()
