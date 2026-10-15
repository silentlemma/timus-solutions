"""Checker: YES, then two coast points S and T whose chord splits the
triangle into two parts of equal area and equal coast length, within a
relative 1e-7."""

import math
import sys

EPS = 1e-7
CORNERS = 3


def fail(reason):
    print(reason)
    sys.exit(1)


def shoelace(poly):
    twice = 0.0
    for i in range(len(poly)):
        (ax, ay), (bx, by) = poly[i - 1], poly[i]
        twice += ax * by - bx * ay
    return abs(twice) / 2


def main():
    source, _, output = sys.argv[1:4]
    nums = list(map(int, open(source).read().split()))
    pts = list(zip(nums[0::2], nums[1::2]))
    got = open(output).read().split()
    if not got or got[0] != "YES":
        fail("a dividing chord always exists")
    if len(got) != 5:
        fail("expected YES and four coordinates")
    try:
        sx, sy, tx, ty = (float(w) for w in got[1:])
    except ValueError:
        fail("not a number")
    sides = [math.dist(pts[i], pts[(i + 1) % CORNERS]) for i in range(CORNERS)]
    perimeter = sum(sides)
    scale = max(perimeter, 1.0)

    def arc(x, y):
        """arc position of a coast point, or None when it is off the coast"""
        pos = 0.0
        for i in range(CORNERS):
            (ax, ay), (bx, by) = pts[i], pts[(i + 1) % CORNERS]
            dx, dy = bx - ax, by - ay
            u = ((x - ax) * dx + (y - ay) * dy) / (sides[i] ** 2)
            u = min(1.0, max(0.0, u))
            if math.dist((ax + u * dx, ay + u * dy), (x, y)) <= EPS * scale:
                return pos + u * sides[i]
            pos += sides[i]
        return None

    ends = [(arc(sx, sy), (sx, sy)), (arc(tx, ty), (tx, ty))]
    if ends[0][0] is None or ends[1][0] is None:
        fail("a point is not on the coast")
    (s, first), (t, last) = sorted(ends)
    if abs((t - s) - perimeter / 2) > EPS * scale:
        fail("coast lengths %.9f and %.9f differ" % (t - s, perimeter - (t - s)))
    corners = []
    pos = 0.0
    for i in range(CORNERS):
        corners.append((pos, pts[i]))
        pos += sides[i]
    part = shoelace([first] + [p for at, p in corners if s < at < t] + [last])
    total = shoelace(pts)
    if abs(part - total / 2) > EPS * max(total, 1.0):
        fail("areas %.9f and %.9f differ" % (part, total - part))


main()
