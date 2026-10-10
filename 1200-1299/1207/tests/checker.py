"""Checker: two different point numbers whose line leaves as many of the
other points on one side as on the other. No three points are collinear,
so no other point lies on the line."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    pts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    try:
        a, b = (int(t) for t in open(output).read().split())
    except ValueError:
        fail("expected two point numbers")
    if not (1 <= a <= n and 1 <= b <= n) or a == b:
        fail("not two different points")
    (ax, ay), (bx, by) = pts[a - 1], pts[b - 1]
    left = sum((bx - ax) * (y - ay) - (by - ay) * (x - ax) > 0 for x, y in pts)
    if 2 * left != n - 2:
        fail("%d points on one side and %d on the other" % (left, n - 2 - left))


if __name__ == "__main__":
    main()
