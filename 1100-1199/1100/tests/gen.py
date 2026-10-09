"""A random results table: a seed, N and the largest number of problems."""

import random
import sys

TOP_ID = 10**7


def main():
    seed, n, most = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    ids = rng.sample(range(1, TOP_ID + 1), n)
    lines = [str(n)] + ["%d %d" % (i, rng.randint(0, most)) for i in ids]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
