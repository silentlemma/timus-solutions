"""Checker: Impossible exactly when expected; otherwise three distinct
vertices whose sides are polygon edges or diagonals (inside the polygon,
touching no other vertex), with no other vertex inside or on the triangle
and both ends of S strictly inside it."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def on_segment(p, a, b):
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and (
        min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
    )


def proper_cross(a, b, c, d):
    d1, d2 = cross(a, b, c), cross(a, b, d)
    d3, d4 = cross(c, d, a), cross(c, d, b)
    return ((d1 > 0 > d2) or (d1 < 0 < d2)) and ((d3 > 0 > d4) or (d3 < 0 < d4))


def inside_polygon(poly, p):
    """strictly inside, by the crossing number; p is never on the boundary here"""
    hit = False
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        if (a[1] > p[1]) != (b[1] > p[1]):
            x = a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1])
            if p[0] < x:
                hit = not hit
    return hit


def is_side(poly, i, j):
    """i j is an edge, or a diagonal inside the polygon touching no other vertex"""
    n = len(poly)
    if (i - j) % n in (1, n - 1):
        return True
    a, b = poly[i], poly[j]
    for k in range(n):
        if k not in (i, j) and on_segment(poly[k], a, b):
            return False
        kn = (k + 1) % n
        if proper_cross(a, b, poly[k], poly[kn]):
            return False
    mid2 = (a[0] + b[0], a[1] + b[1])  # twice the midpoint, to stay in integers
    scaled = [(2 * x, 2 * y) for x, y in poly]
    return inside_polygon(scaled, mid2)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    poly = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    s1 = (int(data[2 * n + 1]), int(data[2 * n + 2]))
    s2 = (int(data[2 * n + 3]), int(data[2 * n + 4]))
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["Impossible"] or got == ["Impossible"]:
        if got != want:
            fail("expected %s" % ("Impossible" if want == ["Impossible"] else "a triangle"))
        return
    if len(got) != 3 or not all(w.isdigit() for w in got):
        fail("expected three vertex numbers")
    idx = [int(w) - 1 for w in got]
    if len(set(idx)) != 3 or not all(0 <= i < n for i in idx):
        fail("three distinct vertices are needed")
    a, b, c = (poly[i] for i in idx)
    if cross(a, b, c) < 0:
        b, c = c, b
        idx[1], idx[2] = idx[2], idx[1]
    if cross(a, b, c) == 0:
        fail("the triangle is flat")
    for p in (s1, s2):
        if not (cross(a, b, p) > 0 and cross(b, c, p) > 0 and cross(c, a, p) > 0):
            fail("S is not strictly inside the triangle")
    for k in range(n):
        if k in idx:
            continue
        p = poly[k]
        if cross(a, b, p) >= 0 and cross(b, c, p) >= 0 and cross(c, a, p) >= 0:
            fail("vertex %d lies inside or on the triangle" % (k + 1))
    for i, j in ((idx[0], idx[1]), (idx[1], idx[2]), (idx[2], idx[0])):
        if not is_side(poly, i, j):
            fail("%d-%d is neither an edge nor a diagonal" % (i + 1, j + 1))


main()
