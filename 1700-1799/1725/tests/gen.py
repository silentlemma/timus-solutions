"""One test from a seed: an even row of up to 50 seats and a random seat."""

import random
import sys

MOST = 50


def main():
    rng = random.Random(int(sys.argv[1]))
    n = 2 * rng.randint(1, MOST // 2)
    print(n, rng.randint(1, n))


main()
