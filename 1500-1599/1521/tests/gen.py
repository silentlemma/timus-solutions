"""One test from a seed and a mode: mode 1 takes N = 100000 and a random K,
mode 2 a random N and K, mode 3 a small N, mode 4 takes N = 100000 with
K = N for an even seed and K = 1 for an odd one."""

import random
import sys

LARGEST = 100000
SMALL = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        print(LARGEST, 1 if seed % 2 else LARGEST)
        return
    n = {1: LARGEST, 2: rng.randint(1, LARGEST)}.get(mode, rng.randint(1, SMALL))
    print(n, rng.randint(1, n))


main()
