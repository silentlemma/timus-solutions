"""Checker: YES exactly when expected; otherwise NO and a triangle A2 B2
C2 with |A2B2| = |A1B1|, |B2C2| = |B1C1| and the same angle at A, not
congruent to the given one, not degenerate, coordinates within 1000."""

import math
import sys

EPS = 1e-6
LIMIT = 1000
POINTS = 3


class Bad(Exception):
    pass


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def angle(a, b, c):
    u = (b[0] - a[0], b[1] - a[1])
    v = (c[0] - a[0], c[1] - a[1])
    return math.atan2(abs(u[0] * v[1] - u[1] * v[0]), u[0] * v[0] + u[1] * v[1])


def check(source, expected, output):
    w = [int(x) for x in open(source).read().split()]
    a1, b1, c1 = (w[0], w[1]), (w[2], w[3]), (w[4], w[5])
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if not got or got[0] != want:
        raise Bad("expected %s" % want)
    if want == "YES":
        if len(got) != 1:
            raise Bad("extra output after YES")
        return
    if len(got) != 1 + 2 * POINTS:
        raise Bad("expected three points after NO")
    v = [float(x) for x in got[1:]]
    if any(abs(x) > LIMIT + EPS for x in v):
        raise Bad("a coordinate is beyond 1000")
    a2, b2, c2 = (v[0], v[1]), (v[2], v[3]), (v[4], v[5])
    if abs(dist(a2, b2) - dist(a1, b1)) > EPS or abs(dist(b2, c2) - dist(b1, c1)) > EPS:
        raise Bad("the sides differ")
    if abs(angle(a2, b2, c2) - angle(a1, b1, c1)) > EPS:
        raise Bad("the angles at A differ")
    area = abs((b2[0] - a2[0]) * (c2[1] - a2[1]) - (b2[1] - a2[1]) * (c2[0] - a2[0]))
    if area < EPS:
        raise Bad("the triangle is degenerate")
    if abs(dist(a2, c2) - dist(a1, c1)) < EPS:
        raise Bad("the triangle is congruent to the given one")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
