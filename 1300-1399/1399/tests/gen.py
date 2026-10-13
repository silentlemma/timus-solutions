"""Delivery plans: a seed and a mode, always 20 clients and 50 items with
distances from points in the plane rounded up and closed under shortest
paths. Mode 1 has a small truck, mode 2 a truck for about a third of the
load, mode 3 a truck for everything at once, mode 4 heavy items for
few clients near each other, mode 5 random distances instead of points,
mode 6 items of one client heavier than the truck together."""

import math
import random
import sys

M, N = 20, 50


def closed(d):
    k = len(d)
    for t in range(k):
        for i in range(k):
            for j in range(k):
                d[i][j] = min(d[i][j], d[i][t] + d[t][j])
    return d


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        d = [[0 if i == j else rng.randint(1, 100) for j in range(M + 1)] for i in range(M + 1)]
        for i in range(M + 1):
            for j in range(i):
                d[i][j] = d[j][i]
    else:
        spread = 25 if mode == 4 else 70
        pts = [(rng.uniform(0, spread), rng.uniform(0, spread)) for _ in range(M + 1)]
        d = [
            [
                0 if i == j else min(100, max(1, math.ceil(math.dist(p, q))))
                for j, q in enumerate(pts)
            ]
            for i, p in enumerate(pts)
        ]
    d = closed(d)
    if mode == 6:
        items = [(rng.randint(60, 100), rng.randint(1, 3)) for _ in range(N)]
    elif mode == 4:
        items = [(rng.randint(50, 100), rng.randint(1, M)) for _ in range(N)]
    else:
        items = [(rng.randint(1, 100), rng.randint(1, M)) for _ in range(N)]
    total = sum(w for w, _ in items)
    cap = {1: 150, 2: total // 3, 3: max(total, 100), 4: 250, 5: 300, 6: 400}[mode]
    cap = max(cap, max(w for w, _ in items))
    print(M, N, min(cap, 3000))
    for row in d:
        print(" ".join(map(str, row)))
    for w, c in items:
        print(w, c)


main()
