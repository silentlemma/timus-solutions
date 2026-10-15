"""One test from a seed and a mode: mode 1 a small random calendar, mode 2
the largest calendar with the most black days, mode 3 a dense small
calendar (many single white cells), mode 4 a single row or column."""

import random
import sys

SIDE = 30000
MOST = 60000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        m = n = SIDE
        k = MOST
    elif mode == 4:
        m, n = (1, rng.randint(1, 50)) if rng.random() < 0.5 else (rng.randint(1, 50), 1)
        k = rng.randint(0, m * n)
    else:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        k = rng.randint(0, m * n) if mode == 1 else (m * n) * 2 // 3
    cells = set()
    while len(cells) < k:
        cells.add((rng.randint(1, m), rng.randint(1, n)))
    print(m, n, k)
    for x, y in sorted(cells, key=lambda c: rng.random()):
        print(x, y)


main()
