"""Checker: N points with coordinates within 1000 in absolute value, every
two farther apart than 1, and the wires of the tree drawn as segments
that meet only at a shared end."""

import sys

LIMIT = 1000
EPS = 1e-9


def fail(reason):
    print(reason)
    sys.exit(1)


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def on_segment(p, a, b):
    return (
        abs(cross(a, b, p)) <= EPS
        and min(a[0], b[0]) - EPS <= p[0] <= max(a[0], b[0]) + EPS
        and min(a[1], b[1]) - EPS <= p[1] <= max(a[1], b[1]) + EPS
    )


def meet(a, b, c, d):
    """True if segments ab and cd have a common point."""
    d1, d2 = cross(c, d, a), cross(c, d, b)
    d3, d4 = cross(a, b, c), cross(a, b, d)
    if ((d1 > EPS and d2 < -EPS) or (d1 < -EPS and d2 > EPS)) and (
        (d3 > EPS and d4 < -EPS) or (d3 < -EPS and d4 > EPS)
    ):
        return True
    return on_segment(a, c, d) or on_segment(b, c, d) or on_segment(c, a, b) or on_segment(d, a, b)


def main():
    inp, _, output = sys.argv[1:4]
    words = open(inp).read().split()
    n = int(words[0])
    edges = [(int(words[1 + 2 * i]) - 1, int(words[2 + 2 * i]) - 1) for i in range(n - 1)]
    got = open(output).read().split()
    if len(got) != 2 * n:
        fail("expected %d numbers, got %d" % (2 * n, len(got)))
    try:
        pts = [(float(got[2 * i]), float(got[2 * i + 1])) for i in range(n)]
    except ValueError:
        fail("not a number")
    for i, (x, y) in enumerate(pts):
        if abs(x) > LIMIT or abs(y) > LIMIT:
            fail("point %d is out of bounds" % (i + 1))
    for i in range(n):
        xi, yi = pts[i]
        for j in range(i + 1, n):
            dx, dy = xi - pts[j][0], yi - pts[j][1]
            if dx * dx + dy * dy <= 1 + EPS:
                fail("points %d and %d are too close" % (i + 1, j + 1))
    for i in range(len(edges)):
        a, b = edges[i]
        for j in range(i + 1, len(edges)):
            c, d = edges[j]
            shared = {a, b} & {c, d}
            if shared:
                # the other ends must not lie on the other wire
                s = shared.pop()
                p = b if a == s else a
                q = d if c == s else c
                if on_segment(pts[p], pts[s], pts[q]) or on_segment(pts[q], pts[s], pts[p]):
                    fail("wires %d and %d overlap" % (i + 1, j + 1))
            elif meet(pts[a], pts[b], pts[c], pts[d]):
                fail("wires %d and %d cross" % (i + 1, j + 1))


if __name__ == "__main__":
    main()
