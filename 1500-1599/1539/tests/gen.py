"""One test from a seed and a mode: the report of a group of q goblins,
every average rounded half up to d places. Mode 1 takes random d, q and
totals, mode 2 d = 5 and q near 10^5, mode 3 100 averages with small
totals, mode 4 a small q, mode 5 averages that are whole numbers but
one, mode 6 d = 1."""

import random
import sys

TOP_D = 5
MOST = 100
TOP_AVERAGE = 1000
BASE = 10
NEAR = 1000
SMALL = 30


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    d = 1 if mode == 6 else (TOP_D if mode == 2 else rng.randint(1, TOP_D))
    one = BASE**d
    if mode == 2:
        q = one - rng.randint(0, NEAR)
    elif mode == 4:
        q = rng.randint(1, SMALL)
    else:
        q = rng.randint(1, one)
    n = MOST if mode in (2, 3) else rng.randint(1, MOST)
    lines = []
    while len(lines) < n:
        if mode == 3:
            p = rng.randint(1, q)
        elif mode == 5 and lines:
            p = q * rng.randint(1, TOP_AVERAGE)
        else:
            p = rng.randint(1, TOP_AVERAGE * q)
        # p / q rounded half up to d places, as an integer number of 10^-d
        units = (2 * p * one + q) // (2 * q)
        if 0 < units <= TOP_AVERAGE * one:
            lines.append("%d.%0*d" % (units // one, d, units % one))
    print(d, n)
    print("\n".join(lines))


main()
