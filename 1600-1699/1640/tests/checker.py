"""Checker: a centre on no demon, a radius up to 10000, every demon inside
or on the circle and at least one on it, within 1e-6."""

import math
import sys

EPS = 1e-6
MOST = 10000


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    demons = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    got = open(output).read().split()
    if len(got) != 3:
        fail("expected three numbers")
    try:
        x, y, r = (float(w) for w in got)
    except ValueError:
        fail("not a number")
    if not all(math.isfinite(v) for v in (x, y, r)):
        fail("not a finite number")
    if r > MOST + EPS or r < 0:
        fail("radius %s is out of range" % got[2])
    if any(math.hypot(x - dx, y - dy) < EPS for dx, dy in demons):
        fail("the centre is on a demon")
    dists = [math.hypot(x - dx, y - dy) for dx, dy in demons]
    if max(dists) > r + EPS:
        fail("a demon stays outside the ring")
    if min(abs(d - r) for d in dists) > EPS:
        fail("no demon is hit by the ring")


main()
