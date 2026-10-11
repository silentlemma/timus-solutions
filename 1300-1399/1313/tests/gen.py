"""An N x N image: a seed and a mode. Mode 1 gives a small N, mode 2 the
largest N = 100, mode 3 an N = 99 minimum-colour background with sparse
random pixels of other colours."""

import random
import sys

TOP = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = TOP - 1 if mode == 3 else rng.randint(1, 8) if mode == 1 else TOP
    print(n)
    for _ in range(n):
        if mode == 3:
            print(*(rng.randint(2, TOP) if rng.randrange(20) == 0 else 1 for _ in range(n)))
        else:
            print(*(rng.randint(1, TOP) for _ in range(n)))


main()
