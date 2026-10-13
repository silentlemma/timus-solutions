"""Checker: two numbers whose total distance to the three houses exceeds
the total of the reference point by at most 10^-6."""

import math
import sys

EPS = 1e-6


def fail(reason):
    print(reason)
    sys.exit(1)


def total(p, houses):
    return sum(math.hypot(p[0] - x, p[1] - y) for x, y in houses)


def main():
    inp, expected, output = sys.argv[1:4]
    v = [float(x) for x in open(inp).read().split()]
    houses = list(zip(v[0::2], v[1::2]))
    want = total([float(x) for x in open(expected).read().split()], houses)
    got = open(output).read().split()
    if len(got) != 2:
        fail("expected two numbers")
    try:
        point = [float(x) for x in got]
    except ValueError:
        fail("not a number")
    if not all(math.isfinite(c) for c in point):
        fail("not a finite number")
    have = total(point, houses)
    if have > want + EPS:
        fail("total %.9f, the best is %.9f" % (have, want))


main()
