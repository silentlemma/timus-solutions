"""One test from a seed: a random bar of up to 50 by 50 pieces."""

import random
import sys

LARGEST = 50


def main():
    rng = random.Random(int(sys.argv[1]))
    print(rng.randint(1, LARGEST), rng.randint(1, LARGEST))


main()
