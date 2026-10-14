"""Print one seeded rectangle.

Mode: random SEED LMIN LMAX WMIN WMAX selects each dimension uniformly
from its inclusive range, with all range endpoints between 1 and 100.
"""

import random
import sys


def main():
    if len(sys.argv) != 7 or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED LMIN LMAX WMIN WMAX")
    seed, lmin, lmax, wmin, wmax = map(int, sys.argv[2:])
    if not (1 <= lmin <= lmax <= 100 and 1 <= wmin <= wmax <= 100):
        raise SystemExit("dimension ranges must be within [1, 100]")
    rng = random.Random(seed)
    print(rng.randint(lmin, lmax), rng.randint(wmin, wmax))


if __name__ == "__main__":
    main()
