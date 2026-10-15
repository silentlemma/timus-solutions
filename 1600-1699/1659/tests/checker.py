"""Checker: three points strictly inside the triangle and three strictly
outside, at least 0.1 from its sides, all nine points at least 1 apart,
and at least nine regular triangles on them (sides equal within 1e-6)."""

import itertools
import math
import sys

EPS = 1e-6
SIDE_EPS = 1e-6
GAP = 1
MARGIN = 0.1
POINTS = 6
TRIANGLES = 9


def fail(reason):
    print(reason)
    sys.exit(1)


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def segment_distance(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
    t = min(1.0, max(0.0, t))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def main():
    source, _, output = sys.argv[1:4]
    data = [float(w) for w in open(source).read().split()]
    corners = [(data[0], data[1]), (data[2], data[3]), (data[4], data[5])]
    got = open(output).read().split()
    if len(got) != 2 * POINTS:
        fail("expected six points")
    try:
        values = [float(w) for w in got]
    except ValueError:
        fail("not a number")
    if not all(math.isfinite(v) for v in values):
        fail("not a finite number")
    marked = [(values[2 * i], values[2 * i + 1]) for i in range(POINTS)]
    sides = [(corners[i], corners[(i + 1) % 3]) for i in range(3)]
    turn = 1 if cross(*corners) > 0 else -1
    for i, p in enumerate(marked):
        inside = all(cross(a, b, p) * turn > 0 for a, b in sides)
        if inside != (i < 3):
            fail("point %d is on the wrong side of the triangle" % (i + 1))
        if min(segment_distance(p, a, b) for a, b in sides) < MARGIN - EPS:
            fail("point %d is too close to a side" % (i + 1))
    points = corners + marked
    for p, q in itertools.combinations(points, 2):
        if math.dist(p, q) < GAP - EPS:
            fail("two points are closer than 1")
    count = 0
    for p, q, r in itertools.combinations(points, 3):
        lengths = (math.dist(p, q), math.dist(q, r), math.dist(r, p))
        if max(lengths) - min(lengths) <= SIDE_EPS:
            count += 1
    if count < TRIANGLES:
        fail("only %d regular triangles" % count)


main()
