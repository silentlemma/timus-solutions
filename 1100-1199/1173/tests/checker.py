"""Checker: 0, every friend once, 0 again, and no two sides of the closed
walk that are not neighbours may touch; a walk always exists, so -1 is
rejected. Coordinates are compared exactly in thousandths."""

import sys

SCALE = 1000


def fail(reason):
    print(reason)
    sys.exit(1)


def exact(token):
    return round(float(token) * SCALE)


def turn(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (v > 0) - (v < 0)


def meet(a, b, c, d):
    # segments ab and cd share a point; no three points are collinear
    return turn(a, b, c) != turn(a, b, d) and turn(c, d, a) != turn(c, d, b)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    where = {0: (exact(data[0]), exact(data[1]))}
    n = int(data[2])
    for i in range(n):
        x, y, ident = data[3 + 3 * i : 6 + 3 * i]
        where[int(ident)] = (exact(x), exact(y))
    try:
        walk = [int(t) for t in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(walk) != n + 2 or walk[0] != 0 or walk[-1] != 0:
        fail("expected 0, the friends, then 0")
    if sorted(walk[1:-1]) != list(range(1, n + 1)):
        fail("not every friend exactly once")
    pts = [where[i] for i in walk[:-1]]
    sides = [(pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts))]
    m = len(sides)
    for i in range(m):
        for j in range(i + 2, m):
            if i == 0 and j == m - 1:
                continue
            if meet(*sides[i], *sides[j]):
                fail("sides %d and %d cross" % (i + 1, j + 1))


if __name__ == "__main__":
    main()
