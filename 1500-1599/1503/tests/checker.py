"""Checker: the same number of real roots as expected, counted with their
multiplicity, in increasing order, each within 1e-6 of the expected one."""

import sys

EPS = 1e-6


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    _, expected, output = sys.argv[1:4]
    want = [float(x) for x in open(expected).read().split()]
    try:
        got = [float(x) for x in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(got) != len(want):
        fail("expected %d roots, got %d" % (len(want), len(got)))
    if got != sorted(got):
        fail("the roots must be in increasing order")
    for w, g in zip(want, got):
        if abs(w - g) > EPS:
            fail("root %.9f, expected %.9f" % (g, w))


main()
