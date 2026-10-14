"""One test from a seed and a mode: mode 1 takes a random N from 4 to
100000, mode 2 a random N with N mod 6 = 2, mode 3 one with N mod 6 = 3,
mode 4 takes N = 100000 minus the seed."""

import random
import sys

LARGEST = 100000
PERIOD = 6
SMALLEST = 4


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.randint(SMALLEST, LARGEST))
    elif mode == 4:
        print(LARGEST - seed)
    else:
        rest = mode  # mode 2 wants the remainder 2, mode 3 the remainder 3
        print(PERIOD * rng.randint(1, LARGEST // PERIOD - 1) + rest)


main()
