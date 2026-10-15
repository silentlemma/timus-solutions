"""One test from a seed: a random number of trees from 1 to 50."""

import random
import sys

MOST = 50


def main():
    print(random.Random(int(sys.argv[1])).randint(1, MOST))


main()
