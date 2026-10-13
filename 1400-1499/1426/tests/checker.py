"""Checker: for each painting "-" exactly when the reference says so;
otherwise "+" and four vertices in order around a rectangle with no two
vertices equal, inside the square from -10000 to 10000, with every one
of the four points on one of its sides."""

import math
import sys

SIDE = 10000
EPS = 1e-6
CORNERS = 4


def fail(reason):
    print(reason)
    sys.exit(1)


def check(points, nums, k):
    v = [(nums[2 * i], nums[2 * i + 1]) for i in range(CORNERS)]
    if any(abs(c) > SIDE + EPS for c in nums):
        fail("painting %d: the rectangle leaves the canvas" % k)
    for i in range(CORNERS):
        a, b, c = v[i], v[(i + 1) % CORNERS], v[(i + 2) % CORNERS]
        e1 = (b[0] - a[0], b[1] - a[1])
        e2 = (c[0] - b[0], c[1] - b[1])
        len1, len2 = math.hypot(*e1), math.hypot(*e2)
        if len1 < EPS:
            fail("painting %d: two vertices coincide" % k)
        # Six or more decimal places round each coordinate by at most EPS / 2.
        # Each edge can move by sqrt(2) * EPS; propagate this into the dot product.
        edge_error = math.sqrt(2) * EPS
        tolerance = EPS * (1 + len1 * len2) + edge_error * (len1 + len2 + edge_error)
        if abs(e1[0] * e2[0] + e1[1] * e2[1]) > tolerance:
            fail("painting %d: not a rectangle" % k)
    for p in points:
        on_side = False
        for i in range(CORNERS):
            a, b = v[i], v[(i + 1) % CORNERS]
            ab = (b[0] - a[0], b[1] - a[1])
            ap = (p[0] - a[0], p[1] - a[1])
            length = math.hypot(*ab)
            off = abs(ab[0] * ap[1] - ab[1] * ap[0]) / length
            along = (ab[0] * ap[0] + ab[1] * ap[1]) / length
            if off < EPS and -EPS <= along <= length + EPS:
                on_side = True
        if not on_side:
            fail("painting %d: point %s is not on a side" % (k, p))


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    want = [line.split()[0] for line in open(expected).read().splitlines() if line.strip()]
    got = [line.split() for line in open(output).read().splitlines() if line.strip()]
    if len(got) != n:
        fail("expected %d lines" % n)
    for k in range(n):
        base = 1 + 8 * k
        points = [(int(data[base + 2 * i]), int(data[base + 2 * i + 1])) for i in range(CORNERS)]
        if got[k][0] != want[k]:
            fail("painting %d: expected %s" % (k + 1, want[k]))
        if want[k] == "-":
            if len(got[k]) != 1:
                fail("painting %d: nothing may follow -" % (k + 1))
            continue
        if len(got[k]) != 1 + 2 * CORNERS:
            fail("painting %d: expected eight coordinates" % (k + 1))
        check(points, [float(x) for x in got[k][1:]], k + 1)


main()
