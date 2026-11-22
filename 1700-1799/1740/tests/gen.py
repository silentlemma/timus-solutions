"""One test from a seed: random l, k and h."""

import random
import sys

LIMIT = 1000


def main():
    rng = random.Random(int(sys.argv[1]))
    length = rng.randint(1, LIMIT)
    print(length, rng.randint(1, length), rng.randint(1, LIMIT))


main()
