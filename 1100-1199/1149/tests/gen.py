"""Inputs for nested sine expressions. Modes:

N: print the given N (legacy mode, used for large expressions).
random SEED: choose N uniformly from 1 through 200 using the given seed.
"""

import random
import sys


def main():
    if sys.argv[1] == "random":
        rng = random.Random(int(sys.argv[2]))
        sys.stdout.write("%d\n" % rng.randint(1, 200))
        return
    sys.stdout.write("%d\n" % int(sys.argv[1]))


if __name__ == "__main__":
    main()
