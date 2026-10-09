"""Checker: three different input points whose circle has exactly (N-3)/2
of the other points strictly inside and (N-3)/2 strictly outside, counted
with the exact integer in-circle determinant. A solution always exists, so
"No solution" is never accepted."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def side(a, b, c, p):
    """Positive inside the circle through a, b, c (taken counterclockwise)."""
    rows = []
    for q in (a, b, c):
        dx, dy = q[0] - p[0], q[1] - p[1]
        rows.append((dx, dy, dx * dx + dy * dy))
    (a1, a2, a3), (b1, b2, b3), (c1, c2, c3) = rows
    det = a1 * (b2 * c3 - b3 * c2) - a2 * (b1 * c3 - b3 * c1) + a3 * (b1 * c2 - b2 * c1)
    orient = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return det if orient > 0 else -det


def main():
    inp, _, output = sys.argv[1:4]
    tok = list(map(int, open(inp).read().split()))
    n = tok[0]
    pts = list(zip(tok[1::2], tok[2::2]))[:n]
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("expected six integers")
    if len(got) != len(pts[0]) * 3:
        fail("expected six integers")
    chosen = list(zip(got[0::2], got[1::2]))
    if len(set(chosen)) != len(chosen) or any(p not in pts for p in chosen):
        fail("the three points must be different input points")
    a, b, c = chosen
    inside = outside = 0
    for p in pts:
        if p in chosen:
            continue
        s = side(a, b, c, p)
        if s > 0:
            inside += 1
        elif s < 0:
            outside += 1
        else:
            fail("point %s lies on the circle" % (p,))
    if inside != outside:
        fail("%d points inside and %d outside" % (inside, outside))


main()
