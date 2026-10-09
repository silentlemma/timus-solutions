"""A random N: a seed and the largest absolute value."""

import random
import sys


def main():
    seed, top = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    sys.stdout.write("%d\n" % rng.randint(-top, top))


if __name__ == "__main__":
    main()
