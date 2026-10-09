"""A random pair: a seed and the largest N. M is random below N."""

import random
import sys


def main():
    seed, top = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = rng.randint(2, top)
    m = rng.randint(1, n - 1)
    sys.stdout.write("%d %d\n" % (n, m))


if __name__ == "__main__":
    main()
