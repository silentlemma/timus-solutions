"""One test from a seed and a mode: mode 1 takes random N and M, mode 2
N = 50 and a random M, mode 3 N = 1 and M up to 26."""

import random
import sys

TOP = 50
LETTERS = 26


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        n, m = 1, rng.randint(1, LETTERS)
    else:
        n = TOP if mode == 2 else rng.randint(2, TOP)
        m = rng.randint(1, TOP)
    print(n, m)


main()
