"""Checker: OK when the expected answer is OK; otherwise ALARM!, a time
within about 10^-3 of the expected one and a pair of objects that reaches
distance d at that time (any pair is accepted when several do)."""

import math
import sys

TOLERANCE = 1.1e-3  # two roundings to three decimals may differ by one unit
COORDS = 6


def fail(reason):
    print(reason)
    sys.exit(1)


def meet(a, b, d):
    """The time the two objects first come within d, or None."""
    p = [b[k] - a[k] for k in range(3)]
    v = [b[k + 3] - a[k + 3] for k in range(3)]
    qa = sum(c * c for c in v)
    if qa == 0:
        return None
    qb = sum(p[k] * v[k] for k in range(3))
    qc = sum(c * c for c in p) - d * d
    disc = qb * qb - qa * qc
    if disc < 0:
        return None
    t = (-qb - math.sqrt(disc)) / qa
    return t if t >= 0 else None


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n, d = int(data[0]), float(data[1])
    obj = [[float(v) for v in data[2 + COORDS * i : 2 + COORDS * (i + 1)]] for i in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["OK"] or got == ["OK"]:
        if got != want:
            fail("expected %s" % want[0])
        return
    if len(got) != 4 or got[0] != "ALARM!":
        fail("expected ALARM! and a time with a pair")
    t, a, b = float(got[1]), int(got[2]), int(got[3])
    if abs(t - float(want[1])) > TOLERANCE:
        fail("time %s instead of %s" % (got[1], want[1]))
    if not (1 <= a <= n and 1 <= b <= n and a != b):
        fail("bad pair")
    when = meet(obj[a - 1], obj[b - 1], d)
    if when is None or abs(when - t) > TOLERANCE:
        fail("objects %d and %d do not meet at that time" % (a, b))


main()
