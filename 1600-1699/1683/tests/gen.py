"""One test from a seed and a mode: mode 1 a small n, mode 2 a large n,
mode 3 a power of two or one more."""

import random
import sys

MOST_N = 10 ** 9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, 100)
    elif mode == 2:
        n = rng.randint(1, MOST_N)
    else:
        n = 2 ** rng.randint(0, 29) + rng.randint(0, 1)
    print(n)


main()
