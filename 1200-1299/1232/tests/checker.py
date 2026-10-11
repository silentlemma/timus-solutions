"""Checker: the number of moves must match the reference answer (-1 when no
landing is possible). Otherwise the n points must form a path from the
station (0, 0, h) of moves of length d, each one lower than the last, inside
the cone of half-angle alpha / 2 around the vertical axis below the station,
and the last point must lie on the surface z = 0.
"""

import math
import sys

TOL = 1e-4


def fail(message):
    print(message)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    h, d, alpha = (float(x) for x in open(inp).read().split())
    want = int(open(ans).read().split()[0])
    tokens = open(output).read().split()
    if not tokens or not tokens[0].lstrip("-").isdigit():
        fail("the first token must be the number of moves")
    n = int(tokens[0])
    if n != want:
        fail("expected %d moves, got %d" % (want, n))
    if n == -1:
        if len(tokens) != 1:
            fail("extra output after -1")
        return
    if len(tokens) != 1 + 3 * n:
        fail("expected %d coordinates, got %d" % (3 * n, len(tokens) - 1))
    try:
        values = [float(x) for x in tokens[1:]]
    except ValueError:
        fail("a coordinate is not a number")
    tg = math.tan(alpha / 2)
    prev = (0.0, 0.0, h)
    for i in range(n):
        p = tuple(values[3 * i : 3 * i + 3])
        if abs(math.dist(prev, p) - d) > TOL:
            fail("move %d has length %.6f, not %.4f" % (i + 1, math.dist(prev, p), d))
        if p[2] >= prev[2]:
            fail("move %d does not go down" % (i + 1))
        if math.hypot(p[0], p[1]) > (h - p[2]) * tg + TOL:
            fail("point %d is outside the cone" % (i + 1))
        if p[2] < -TOL:
            fail("point %d is below the surface" % (i + 1))
        prev = p
    if abs(prev[2]) > TOL:
        fail("the last point is not on the surface")


if __name__ == "__main__":
    main()
