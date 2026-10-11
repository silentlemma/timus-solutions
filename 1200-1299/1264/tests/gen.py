"""N and M: a seed. Both up to 40000."""

import random
import sys

TOP = 40000


def main():
    rng = random.Random(int(sys.argv[1]))
    sys.stdout.write("%d %d\n" % (rng.randint(0, TOP), rng.randint(0, TOP)))


if __name__ == "__main__":
    main()
