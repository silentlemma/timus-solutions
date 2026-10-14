"""One test from a seed and a mode: mode 1 a random n up to 10000, mode 2 a
random small n, mode 3 the largest n."""

import random
import sys

MOST = 10000
SMALL = 50


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.randint(2, MOST))
    elif mode == 2:
        print(rng.randint(2, SMALL))
    else:
        print(MOST)


main()
