"""One test from a seed: two random odd sides between 7 and 499."""

import random
import sys

SMALLEST, LARGEST = 7, 499


def main():
    rng = random.Random(int(sys.argv[1]))
    m, n = (rng.randrange(SMALLEST, LARGEST + 1, 2) for _ in range(2))
    print(m, n)


main()
