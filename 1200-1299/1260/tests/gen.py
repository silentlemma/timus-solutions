"""N: a seed. Any N from 1 to 55."""

import random
import sys

TOP = 55


def main():
    rng = random.Random(int(sys.argv[1]))
    sys.stdout.write("%d\n" % rng.randint(1, TOP))


if __name__ == "__main__":
    main()
