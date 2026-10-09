"""A random query: a seed."""

import random
import sys

TOP_N = 10
TOP_K = 20


def main():
    rng = random.Random(int(sys.argv[1]))
    sys.stdout.write("%d %s\n" % (rng.randint(1, TOP_N), "!" * rng.randint(1, TOP_K)))


if __name__ == "__main__":
    main()
