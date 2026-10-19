"""Candles from a seed and a mode: mode 1 a few candles near the centre,
2 the most candles anywhere on the cake, 3 the most candles in a few
columns, 4 the most candles in the leftmost columns, next to the edge,
5 the most candles in one column. The count k is random."""

import random
import sys

MOST = 1000
FEW = 8
INNER = 10 ** 9 - 1


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    points = set()
    columns = [rng.randint(-INNER, INNER) for _ in range(FEW)]
    while len(points) < n:
        if mode == 1:
            p = (rng.randint(-FEW, FEW), rng.randint(-FEW, FEW))
        elif mode == 2:
            p = (rng.randint(-INNER, INNER), rng.randint(-INNER, INNER))
        elif mode == 3:
            p = (rng.choice(columns), rng.randint(-INNER, INNER))
        elif mode == 4:
            p = (-INNER + rng.randint(0, 1), rng.randint(-INNER, INNER))
        else:
            p = (columns[0], rng.randint(-INNER, INNER))
        points.add(p)
    k = rng.randint(1, n - 1)
    print(n, k)
    print("\n".join("%d %d" % p for p in rng.sample(sorted(points), n)))


main()
