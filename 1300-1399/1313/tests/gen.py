"""An N x N image: a seed and a mode. Mode 1 gives a small N, mode 2 the
largest N = 100."""

import random
import sys

TOP = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 8) if mode == 1 else TOP
    print(n)
    for _ in range(n):
        print(*(rng.randint(1, TOP) for _ in range(n)))


main()
