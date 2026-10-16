"""One test from a seed and a mode: mode 1 four points with coordinates
up to 6, mode 2 coordinates up to 10^9 in absolute value, mode 3 two
walks inside one shared box."""

import random
import sys

FEW = 6
MOST = 10**9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = FEW if mode == 1 else MOST
    if mode == 3:
        lo, hi = rng.randint(-MOST, 0), rng.randint(0, MOST)
        pts = [(rng.choice((lo, hi)), rng.choice((lo, hi))) for _ in range(4)]
    else:
        pts = [(rng.randint(-top, top), rng.randint(-top, top)) for _ in range(4)]
    for x, y in pts:
        print(x, y)


main()
