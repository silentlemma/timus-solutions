"""One test from a seed and a mode: mode 1 a random size, mode 2 a large
size."""

import random
import sys

MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(1, MOST) if mode == 1 else rng.randint(MOST - 10, MOST))


main()
