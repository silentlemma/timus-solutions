"""One test from a seed: random thicknesses and two random volumes."""

import random
import sys

LARGEST = 100


def main():
    rng = random.Random(int(sys.argv[1]))
    print(*(rng.randint(1, LARGEST) for _ in range(4)))


main()
