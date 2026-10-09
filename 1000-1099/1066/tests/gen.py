"""A random garland: a seed, the largest N and the largest A (N >= 3,
A >= 10, A with two decimals)."""

import random
import sys


def main():
    seed, top_n, top_a = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    n = rng.randint(3, top_n)
    hundredths = rng.randint(1000, top_a * 100)
    sys.stdout.write("%d %d.%02d\n" % (n, hundredths // 100, hundredths % 100))


if __name__ == "__main__":
    main()
