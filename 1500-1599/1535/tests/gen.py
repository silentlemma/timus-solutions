"""One test from a seed and a mode: mode 1 takes a random N up to 50000,
mode 2 an N up to 12, mode 3 an even N near 50000, mode 4 an odd one,
mode 5 N = 50000 and mode 6 N = 49999."""

import random
import sys

LARGEST = 50000
SMALL = 12
NEAR = 100


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, LARGEST)
    elif mode == 2:
        n = rng.randint(2, SMALL)
    elif mode == 5:
        n = LARGEST
    elif mode == 6:
        n = LARGEST - 1
    else:
        n = LARGEST - rng.randint(0, NEAR)
        n -= n % 2 if mode == 3 else 1 - n % 2
    print(n)


main()
