"""Corridors: N b prints those values unchanged; random SEED draws N
uniformly from 1 through 1000000 and b from 0 through 100."""

import random
import sys


def main():
    if sys.argv[1] == "random":
        rng = random.Random(int(sys.argv[2]))
        n, b = rng.randint(1, 10**6), rng.randint(0, 100)
    else:
        n, b = (int(a) for a in sys.argv[1:3])
    print(n)
    print(b)


main()
