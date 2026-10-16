"""One test file from a seed and a mode, with 5000 tests per mode.

1: random points with coordinates up to 10.
2: random points with coordinates up to 3.
3: the original straight/folded-gully sampling scheme.
4: noncollinear gullies with S, B and T on one line and B between S and T.
5: all five points on the boundary of the coordinate square.
6: long, nearly folded arms with absolute direction determinant one.
"""

import random
import sys

TESTS = 5000
LIMIT = 10
SMALL = 3


def on_segment(p, a, b):
    if (b[0] - a[0]) * (p[1] - a[1]) != (b[1] - a[1]) * (p[0] - a[0]):
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def area(a, b, c):
    return (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 2 else LIMIT
    lines = []
    seen = set()
    boundary = [(x, y) for x in range(-LIMIT, LIMIT + 1)
                for y in range(-LIMIT, LIMIT + 1) if max(abs(x), abs(y)) == LIMIT]
    while len(lines) < TESTS:
        pts = [(rng.randint(-top, top), rng.randint(-top, top)) for _ in range(5)]
        if mode == 3:
            b = pts[3]
            dx, dy = rng.randint(-2, 2), rng.randint(-2, 2)
            pts[2] = (b[0] + dx * rng.randint(1, 4), b[1] + dy * rng.randint(1, 4))
            pts[4] = (b[0] + dx * rng.randint(-4, 4), b[1] + dy * rng.randint(-4, 4))
        elif mode == 4:
            b = pts[3]
            dx, dy = rng.randint(-2, 2), rng.randint(-2, 2)
            left, right = rng.randint(1, 4), rng.randint(1, 4)
            pts[0] = (b[0] + left * dx, b[1] + left * dy)
            pts[1] = (b[0] - right * dx, b[1] - right * dy)
            if area(*pts[2:]) == 0:
                continue
        elif mode == 5:
            pts = rng.sample(boundary, 5)
        elif mode == 6:
            m = rng.randint(10, 20)
            u, v = (m, m - 1), (m - 1, m - 2)
            if rng.randrange(2):
                u, v = (-u[0], u[1]), (-v[0], v[1])
            for _ in range(rng.randrange(4)):
                u, v = (-u[1], u[0]), (-v[1], v[0])
            b = tuple(rng.randint(-LIMIT - min(0, u[i], v[i]),
                                  LIMIT - max(0, u[i], v[i])) for i in range(2))
            pts[2] = (b[0] + u[0], b[1] + u[1])
            pts[3] = b
            pts[4] = (b[0] + v[0], b[1] + v[1])
        if len(set(pts)) < len(pts) or any(abs(x) > LIMIT for p in pts for x in p):
            continue
        s, t, a, b, c = pts
        if any(on_segment(p, a, b) or on_segment(p, b, c) for p in (s, t)):
            continue
        line = " ".join("%d %d" % p for p in pts)
        if mode >= 4:
            if line in seen:
                continue
            seen.add(line)
        lines.append(line)
    print(len(lines))
    print("\n".join(lines))


main()
