"""Checker: N heights within 10^6 such that, in exact arithmetic, every
laser named higher is strictly above the other one where their vertical
projections cross."""

import sys
from fractions import Fraction

LIMIT = 10**6
FIELDS = 5  # X, Y, u, v, w


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    lasers = [[int(w) for w in data[1 + FIELDS * i : 1 + FIELDS * (i + 1)]] for i in range(n)]
    pos = 1 + FIELDS * n
    m = int(data[pos])
    pairs = [(int(data[pos + 1 + 2 * k]) - 1, int(data[pos + 2 + 2 * k]) - 1) for k in range(m)]
    got = open(output).read().split()
    if len(got) != n:
        fail("expected %d numbers, got %d" % (n, len(got)))
    try:
        z = [Fraction(w) for w in got]
    except (ValueError, ZeroDivisionError):
        fail("not a number")
    for i, value in enumerate(z):
        if abs(value) > LIMIT:
            fail("height %d is outside 10^6" % (i + 1))
    for i, j in pairs:
        xi, yi, ui, vi, wi = lasers[i]
        xj, yj, uj, vj, wj = lasers[j]
        det = ui * vj - vi * uj
        dx, dy = xj - xi, yj - yi
        ti = Fraction(dx * vj - dy * uj, det)
        tj = Fraction(vi * dx - ui * dy, det)
        if not z[i] + wi * ti > z[j] + wj * tj:
            fail("laser %d is not above laser %d" % (i + 1, j + 1))


main()
