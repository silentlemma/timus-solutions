"""One test file from a seed and a mode: up to 10^4 cases. Mode 1 small
coordinates and costs, so that cities coincide or line up, mode 2 any
coordinates and costs up to 1000, mode 3 equal costs, mode 4 one cost
far above the others."""

import random
import sys

TESTS = 10000
LIMIT = 1000
SMALL = 3
CITIES = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else LIMIT
    lines = [str(TESTS)]
    for _ in range(TESTS):
        for _ in range(CITIES):
            lines.append("%d %d" % (rng.randint(-top, top), rng.randint(-top, top)))
        if mode == 3:
            costs = [rng.randint(1, LIMIT)] * CITIES
        elif mode == 4:
            costs = [rng.randint(1, 10) for _ in range(CITIES)]
            costs[rng.randrange(CITIES)] = rng.randint(LIMIT // 2, LIMIT)
        else:
            costs = [rng.randint(1, top * 3) for _ in range(CITIES)]
        lines.append(" ".join(map(str, costs)))
    print("\n".join(lines))


main()
