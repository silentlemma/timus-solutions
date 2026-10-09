"""A random arc: a seed, the mode and a size.
random S: three points in [-S, S]^2;
lattice R: three integer points of a circle of radius R around an integer
center (its extremes are integers);
near S: of many random triples in [-S, S]^2, the one whose extreme on the
arc is closest to an integer without being one.
The circle center lies in the hall and the arc inside the square."""

import math
import random
import sys

LIMIT = 1000
TRIES = 20000


def circle(a, b, c):
    d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    if d == 0:
        return None
    a2, b2, c2 = (p[0] ** 2 + p[1] ** 2 for p in (a, b, c))
    ox = (a2 * (b[1] - c[1]) + b2 * (c[1] - a[1]) + c2 * (a[1] - b[1])) / d
    oy = (a2 * (c[0] - b[0]) + b2 * (a[0] - c[0]) + c2 * (b[0] - a[0])) / d
    return ox, oy, math.hypot(a[0] - ox, a[1] - oy)


def extremes(a, b, c):
    """The circle and the axis extremes that lie on the arc, or None."""
    got = circle(a, b, c)
    if got is None:
        return None
    ox, oy, r = got

    def side(p):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

    sc = side(c)
    on = [p for p in ((ox + r, oy), (ox - r, oy), (ox, oy + r), (ox, oy - r)) if side(p) * sc > 0]
    return ox, oy, r, on


def valid(a, b, c):
    got = extremes(a, b, c)
    if got is None:
        return False
    ox, oy, r, on = got
    inside = all(abs(v) <= LIMIT - 1e-6 for p in on for v in p)
    return inside and abs(ox) <= LIMIT and abs(oy) <= LIMIT


def main():
    seed, mode, size = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    rng = random.Random(seed)

    def point():
        return (rng.randint(-size, size), rng.randint(-size, size))

    if mode == "lattice":
        ox, oy = (rng.randint(-LIMIT + size, LIMIT - size) for _ in range(2))
        ring = [
            (ox + x, oy + y)
            for x in range(-size, size + 1)
            for y in (math.isqrt(size * size - x * x),)
            for y in {y, -y}
            if x * x + y * y == size * size
        ]
        while True:
            pts = rng.sample(ring, 3)
            if valid(*pts):
                break
    elif mode == "near":
        best = None
        for _ in range(TRIES):
            pts = [point() for _ in range(3)]
            if not valid(*pts):
                continue
            for p in extremes(*pts)[3]:
                for v in p:
                    gap = abs(v - round(v))
                    if 1e-12 < gap and (best is None or gap < best[0]):
                        best = (gap, pts)
        pts = best[1]
    else:
        while True:
            pts = [point() for _ in range(3)]
            if valid(*pts):
                break
    sys.stdout.write("\n".join("%d %d" % p for p in pts) + "\n")


if __name__ == "__main__":
    main()
