"""Candles from a seed and a mode: mode 1 a few candles near the centre,
2 the most candles anywhere on the cake, 3 the most candles in a few
columns, 4 the most candles in the leftmost columns, next to the edge,
5 the most candles in one column; 6 a descending diagonal with k=1;
7 a tightly packed grid near the upper-right corner with k=n-1.
The count k is random in modes 1 through 5."""

import random
import sys

MOST = 1000
FEW = 8
INNER = 10 ** 9 - 1


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7):
        if mode == 6:
            points = [(-INNER + i, INNER - i) for i in range(MOST)]
            k = 1
        else:
            points = [(INNER - x, INNER - y) for x in range(20) for y in range(50)]
            k = MOST - 1
        rng.shuffle(points)
        print(MOST, k)
        print("\n".join("%d %d" % p for p in points))
        return
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
