"""A random valid date: a seed."""

import random
import sys

LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    rng = random.Random(int(sys.argv[1]))
    y, m = rng.randint(1600, 2400), rng.randint(1, 12)
    leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    days = LENGTHS[m - 1] + (m == 2 and leap)
    print(rng.randint(1, days), m, y)


if __name__ == "__main__":
    main()
