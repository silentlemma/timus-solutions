"""Checker: a moment t in [0, 10^12] at which the point
(sin(sqrt(t)), cos(t)) lies within eps of the given dot. The curve comes
that close to every dot of the square, so FAIL is always wrong."""

import math
import sys

LAST = 10**12
SLACK = 1e-9


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    x0, y0, eps = map(float, open(inp).read().split()[:3])
    got = open(output).read().split()
    if len(got) != 1:
        fail("expected one number")
    try:
        t = float(got[0])
    except ValueError:
        fail("%s is not a moment" % got[0])
    if not 0 <= t <= LAST:
        fail("t = %s is out of range" % got[0])
    gap = math.hypot(math.sin(math.sqrt(t)) - x0, math.cos(t) - y0)
    if gap > eps + SLACK:
        fail("at t = %s the curve is %.6f away, more than %s" % (got[0], gap, eps))


if __name__ == "__main__":
    main()
