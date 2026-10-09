"""A random N: a seed and the largest value."""

import random
import sys


def main():
    seed, top = (int(x) for x in sys.argv[1:3])
    sys.stdout.write("%d\n" % random.Random(seed).randint(1, top))


if __name__ == "__main__":
    main()
