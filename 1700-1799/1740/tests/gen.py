"""One test from a seed: random l, k and h."""

import random
import sys

LIMIT = 1000


def main():
    rng = random.Random(int(sys.argv[1]))
    l = rng.randint(1, LIMIT)
    print(l, rng.randint(1, l), rng.randint(1, LIMIT))


main()
