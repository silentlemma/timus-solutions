"""One page from a seed and a mode: mode 1 a few arcs and points in a
small box, mode 2 a hundred arcs under one wide band of ten thousand
points, so nearly every point counts for every arc, mode 3 random arcs
and points over the whole plane, mode 4 like mode 2 with points on a
coarse lattice, so many of them line up with an end of an arc."""

import random
import sys

LIMIT = 10000
ARCS = 100
POINTS = 10000
SMALL = 8


def arc_ok(p, q, r):
    # three distinct points not on a line, q between p and r on an arc of
    # at most half a circle: the angle at q is not acute
    if len({p, q, r}) < 3:
        return False
    cross = (r[0] - p[0]) * (q[1] - p[1]) - (r[1] - p[1]) * (q[0] - p[0])
    dot = (p[0] - q[0]) * (r[0] - q[0]) + (p[1] - q[1]) * (r[1] - q[1])
    return cross != 0 and dot <= 0


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m, box = rng.randint(1, 4), rng.randint(1, 30), SMALL
    else:
        n, m, box = ARCS, POINTS, LIMIT
    arcs = set()
    while len(arcs) < n:
        if mode in (2, 4):
            # chords near y = -6000 across the plane, bulging downwards
            half = rng.randint(4000, 9000)
            shift = rng.randint(-500, 500)
            p = (shift - half, -6000 + rng.randint(-200, 200))
            r = (shift + half, -6000 + rng.randint(-200, 200))
            q = (shift + rng.randint(-100, 100), -6000 - rng.randint(half // 2, half))
        else:
            p, q, r = ((rng.randint(-box, box), rng.randint(-box, box)) for _ in range(3))
        if arc_ok(p, q, r):
            arcs.add(p + q + r)
    points = set()
    while len(points) < m:
        if mode == 2:
            points.add((rng.randint(-3500, 3500), rng.randint(-5000, LIMIT)))
        elif mode == 4:
            points.add((rng.randint(-35, 35) * 100, rng.randint(-50, 100) * 100))
        else:
            points.add((rng.randint(-box, box), rng.randint(-box, box)))
    print(n, m)
    for a in sorted(arcs):
        print(*a)
    points = sorted(points)
    rng.shuffle(points)
    for p in points:
        print(*p)


main()
