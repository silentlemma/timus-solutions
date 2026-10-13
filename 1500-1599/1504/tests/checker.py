"""Checker: the seat must lie on the table edge, and the heaviest of the
pieces nearest to it must weigh as much as at the expected seat. Distances
are compared with a tolerance of 1e-6."""

import math
import sys

EPS = 1e-6


def fail(reason):
    print(reason)
    sys.exit(1)


def taken(pieces, x, y):
    """The weight of the heaviest piece among the nearest ones to (x, y)."""
    dist = [math.hypot(px - x, py - y) for px, py, _ in pieces]
    best = min(dist)
    return max(w for d, (_, _, w) in zip(dist, pieces) if d <= best + EPS)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    r, k = float(data[0]), int(data[1])
    pieces = [
        (float(data[2 + 3 * i]), float(data[3 + 3 * i]), int(data[4 + 3 * i])) for i in range(k)
    ]
    ex, ey = (float(v) for v in open(expected).read().split())
    try:
        values = [float(v) for v in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(values) != 2:
        fail("expected two coordinates, got %d numbers" % len(values))
    x, y = values
    if abs(math.hypot(x, y) - r) > EPS:
        fail("(%.9f, %.9f) is not on the table edge" % (x, y))
    want, got = taken(pieces, ex, ey), taken(pieces, x, y)
    if got != want:
        fail("the seat gives a piece of %d grams, expected %d" % (got, want))


main()
