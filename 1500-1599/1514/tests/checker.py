"""Checker: the printed perimeter must equal the expected minimum within
1e-4, and the three printed trees must be distinct and form a triangle
of that perimeter."""

import math
import sys

EPS = 1e-4


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    pts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    want = float(open(expected).read().split()[0])
    try:
        values = open(output).read().split()
        got = float(values[0])
        ids = [int(v) for v in values[1:]]
    except (ValueError, IndexError):
        fail("cannot read the answer")
    if abs(got - want) > EPS:
        fail("perimeter %.6f, expected %.6f" % (got, want))
    if len(ids) != 3 or len(set(ids)) != 3 or not all(1 <= i <= n for i in ids):
        fail("expected three distinct trees")
    a, b, c = (pts[i - 1] for i in ids)
    real = math.dist(a, b) + math.dist(b, c) + math.dist(c, a)
    if abs(real - want) > EPS:
        fail("the trees %s give %.6f, expected %.6f" % (ids, real, want))


main()
