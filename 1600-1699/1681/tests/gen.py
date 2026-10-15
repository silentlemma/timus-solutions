"""One test from a seed and a mode: mode 1 a small polygon and any k,
mode 2 a large polygon near a circle, mode 3 a large polygon and k close
to n / 2, mode 4 a long thin polygon, mode 5 k = 1 or k = n - 1, mode 6
the hull of random points, an irregular polygon."""

import math
import random
import sys

MOST_N = 300
LIMIT = 10000


def hull(points):
    points = sorted(set(points))

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and ((out[-1][0] - out[-2][0]) * (p[1] - out[-2][1]) -
                                     (out[-1][1] - out[-2][1]) * (p[0] - out[-2][0])) <= 0:
                out.pop()
            out.append(p)
        return out

    lower, upper = half(points), half(points[::-1])
    return lower[:-1] + upper[:-1]


def polygon(rng, n, sx, sy):
    """A strictly convex polygon of n vertices, counterclockwise, from
    points near an ellipse with half-axes sx and sy."""
    while True:
        angles = [rng.uniform(0, 2 * math.pi) for _ in range(3 * n)]
        cloud = [(round(sx * math.cos(a)), round(sy * math.sin(a))) for a in angles]
        h = hull(cloud)
        if len(h) >= n:
            keep = sorted(rng.sample(range(len(h)), n))
            # a subset of the vertices of a strictly convex polygon stays strictly convex
            start = rng.randrange(n)
            pts = [h[i] for i in keep]
            return pts[start:] + pts[:start]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(3, 10)
        pts = polygon(rng, n, rng.randint(5, 50), rng.randint(5, 50))
        k = rng.randint(1, n - 1)
    elif mode == 6:
        pts = []
        while len(pts) < 4:
            pts = hull([(rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT))
                        for _ in range(rng.randint(10, 2000))])
        n = len(pts)
        k = rng.randint(2, n - 2)
    elif mode == 4:
        n = rng.randint(50, 150)
        pts = polygon(rng, n, LIMIT, rng.randint(200, 1000))
        k = rng.randint(2, n - 2)
    else:
        n = rng.randint(MOST_N - 20, MOST_N)
        pts = polygon(rng, n, LIMIT, LIMIT)
        if mode == 2:
            k = rng.randint(2, n - 2)
        elif mode == 3:
            k = n // 2 + rng.randint(-2, 2)
        else:
            k = rng.choice((1, n - 1))
    print(n, k)
    for x, y in pts:
        print(x, y)


main()
