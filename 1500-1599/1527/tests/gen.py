"""One test from a seed and a mode, with 100 cities and 10000 roads unless
small. Mode 1 is random with a tight time limit, mode 2 makes half the
roads toll roads and gives a small budget, mode 3 makes every road free
of toll with zero time, mode 4 is small, mode 5 leaves no way through."""

import random
import sys

CITIES = 100
ROADS = 10000
TOP_TIME = 10**4
TOP_HEIGHT = 10**6
SMALL = 6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 4 else CITIES
    m = rng.randint(1, SMALL * 2) if mode == 4 else ROADS
    s, f = rng.sample(range(1, n + 1), 2)
    budget = rng.randint(0, 3) if mode in (2, 4) else rng.randint(0, CITIES)
    roads = []
    for _ in range(m):
        u, v = rng.randint(1, n), rng.randint(1, n)
        toll = rng.randint(0, 1) if mode != 3 else 0
        time = 0 if mode == 3 else rng.randint(0, TOP_TIME if mode != 4 else SMALL)
        height = rng.randint(0, TOP_HEIGHT if mode != 4 else SMALL)
        if mode == 5 and v == f:
            v = s  # no road enters the finish
        roads.append((u, v, toll, time, height))
    limit = rng.randint(TOP_TIME, 3 * TOP_TIME) if mode in (1, 2, 5) else rng.randint(0, 10**6)
    if mode == 4:
        limit = rng.randint(0, 4 * SMALL)
    print(n, m, s, f)
    print(budget, limit)
    print("\n".join("%d %d %d %d %d" % r for r in roads))


main()
