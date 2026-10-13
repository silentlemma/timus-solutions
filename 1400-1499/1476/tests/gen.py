"""One test from a seed: M and N from 1 to 40 and K from 0 to M."""

import random
import sys

LARGEST = 40


def main():
    rng = random.Random(int(sys.argv[1]))
    m, n = rng.randint(1, LARGEST), rng.randint(1, LARGEST)
    print(m, n, rng.randint(0, m))


main()
