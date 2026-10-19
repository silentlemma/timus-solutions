"""Cities from a seed and a mode, joined by a minimum spanning tree: mode
1 a few cities on a small grid, 2 the most cities at random, 3 a long
spine with a city beside every spine city, 4 the most cities as a full
grid, so that many trees are minimal, 5 the most cities near a line,
6 five-armed stars around stars, so that many cities have five
neighbours. Cities and roads come in random order, so the palace is a
random city of the tree."""

import math
import random
import sys

MOST = 1000
LIMIT = 10000
SMALL = 8


def spanning_tree(points):
    # Prim's algorithm on the complete graph
    n = len(points)
    best = [math.inf] * n
    link = [-1] * n
    done = [False] * n
    best[0] = 0
    edges = []
    for _ in range(n):
        u = min((i for i in range(n) if not done[i]), key=best.__getitem__)
        done[u] = True
        if link[u] >= 0:
            edges.append((link[u], u))
        ux, uy = points[u]
        for v in range(n):
            if not done[v]:
                d = (points[v][0] - ux) ** 2 + (points[v][1] - uy) ** 2
                if d < best[v]:
                    best[v], link[v] = d, u
    return edges


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    points = set()
    if mode == 1:
        size = rng.randint(2, SMALL)
        while len(points) < size:
            points.add((rng.randint(0, 4), rng.randint(0, 4)))
    elif mode == 2:
        while len(points) < MOST:
            points.add((rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)))
    elif mode == 3:
        for i in range(MOST // 2):
            x = 2 * LIMIT * i // (MOST // 2) - LIMIT
            points.add((x, 0))
            points.add((x, rng.choice((-1, 1)) * (LIMIT // MOST)))
    elif mode == 4:
        side = int(math.isqrt(MOST))
        points = {(i, j) for i in range(side) for j in range(side)}
    elif mode == 5:
        while len(points) < MOST:
            x = rng.randint(-LIMIT, LIMIT)
            points.add((x, x // 7 + rng.randint(-3, 3)))
    else:
        arms = 5
        todo = [(0, 0, LIMIT // 3)]
        points.add((0, 0))
        while todo and len(points) < MOST:
            x, y, r = todo.pop(0)
            turn = rng.random()
            for a in range(arms):
                angle = 2 * math.pi * (a + turn) / arms
                p = (x + round(r * math.cos(angle)), y + round(r * math.sin(angle)))
                if p not in points and len(points) < MOST and r > 1:
                    points.add(p)
                    todo.append((p[0], p[1], r * 2 // 5))
    points = sorted(points)
    rng.shuffle(points)
    edges = spanning_tree(points)
    rng.shuffle(edges)
    print(len(points))
    print("\n".join("%d %d" % p for p in points))
    print()
    print("\n".join("%d %d" % (a + 1, b + 1) if rng.random() < 0.5 else "%d %d" % (b + 1, a + 1)
                    for a, b in edges))


main()
