"""Checker: "Yes", then the bends of the even part and of the odd part,
each list with increasing x (a new list starts where x drops). Both lists
must match the expected ones point by point within 1e-4; the split is
unique, and neither list may keep a point where nothing bends."""

import sys

EPS = 1e-4


def fail(reason):
    print(reason)
    sys.exit(1)


def split(tokens):
    if not tokens or tokens[0] != "Yes":
        fail("expected Yes")
    try:
        values = [float(t) for t in tokens[1:]]
    except ValueError:
        fail("not numbers")
    if len(values) % 2:
        fail("an odd number of coordinates")
    points = list(zip(values[0::2], values[1::2]))
    for k in range(1, len(points)):
        if points[k][0] < points[k - 1][0]:
            return points[:k], points[k:]
    fail("the odd part is missing")


def main():
    _, expected, output = sys.argv[1:4]
    want = split(open(expected).read().split())
    got = split(open(output).read().split())
    for name, a, b in zip(("even", "odd"), want, got):
        if len(a) != len(b):
            fail("the %s part has %d bends, expected %d" % (name, len(b), len(a)))
        for (x1, y1), (x2, y2) in zip(a, b):
            if abs(x1 - x2) > EPS or abs(y1 - y2) > EPS:
                fail("the %s part differs near x = %.4f" % (name, x1))


main()
