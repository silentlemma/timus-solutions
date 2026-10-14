"""One test from a seed and a mode: mode 1 is the largest N, mode 2 a
random N up to the largest, mode 3 a random N up to 1000."""

import random
import sys

MOST = 250000
SMALL = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(MOST)
    elif mode == 2:
        print(rng.randint(1, MOST))
    else:
        print(rng.randint(1, SMALL))


main()
