"""One test from a seed: a random odd n from 3 to 99."""

import random
import sys

HALF = 49


def main():
    rng = random.Random(int(sys.argv[1]))
    print(2 * rng.randint(1, HALF) + 1)


main()
