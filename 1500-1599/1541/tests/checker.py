"""Checker: -1 exactly when expected; otherwise K < 20 speeds, decreasing,
whole and at most 100000, whose unit fractions add up to exactly M / N."""

import sys
from fractions import Fraction

MOST = 19
FASTEST = 100000


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    m, n = map(int, open(source).read().split())
    want = open(expected).read().split()
    try:
        got = [int(v) for v in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if not got:
        fail("empty output")
    if (want[0] == "-1") != (got[0] == -1):
        fail("got %d, expected %s" % (got[0], want[0]))
    if got[0] == -1:
        return
    k, speeds = got[0], got[1:]
    if not 1 <= k <= MOST or len(speeds) != k:
        fail("K = %d with %d speeds" % (k, len(speeds)))
    if any(not 1 <= v <= FASTEST for v in speeds):
        fail("a speed is out of range")
    if any(a <= b for a, b in zip(speeds, speeds[1:])):
        fail("the speeds do not decrease")
    if sum(Fraction(1, v) for v in speeds) != Fraction(m, n):
        fail("the time is not %d/%d" % (m, n))


main()
