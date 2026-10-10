"""Prices and a quota: a seed, the largest K and a mode. Mode 1 draws any
prices, mode 2 equal whole prices that make ties, mode 3 prices of either
sign near zero and mode 4 prices at the ends of the range."""

import random
import sys

TOP = 1000000


def main():
    seed, kmax, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    k = rng.randint(1, kmax)
    if mode == 1:
        a, b = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
    elif mode == 2:
        a = b = 100 * rng.randint(1, 2 * kmax + 1)
    elif mode == 3:
        a, b = rng.randint(-300, 300), rng.randint(-300, 300)
    else:
        a, b = rng.choice([TOP, -TOP, TOP - 1]), rng.choice([TOP, -TOP, 1])
    sys.stdout.write("%.2f %.2f\n%d\n" % (a / 100, b / 100, k))


if __name__ == "__main__":
    main()
