"""A random query: a seed."""

import random
import sys

TOP = 50


def main():
    rng = random.Random(int(sys.argv[1]))
    s = rng.randint(2, TOP)
    sys.stdout.write("%d %d\n" % (rng.randint(2, s), s))


if __name__ == "__main__":
    main()
