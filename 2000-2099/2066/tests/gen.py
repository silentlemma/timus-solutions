"""Three random values from 0 to 100 in nondecreasing order, from a seed."""

import random
import sys

TOP = 100


def main():
    rng = random.Random(int(sys.argv[1]))
    for v in sorted(rng.randint(0, TOP) for _ in range(3)):
        print(v)


main()
