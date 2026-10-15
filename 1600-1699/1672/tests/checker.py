"""Checker: three unit vectors at right angles, along which the swarm has
the same width (the box they span around it is a cube), within 1e-6."""

import math
import sys

EPS = 1e-6


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    pts = [tuple(int(w) for w in data[1 + 3 * i:4 + 3 * i]) for i in range(n)]
    words = open(output).read().split()
    if len(words) != 9:
        fail("expected nine numbers")
    try:
        v = [float(w) for w in words]
    except ValueError:
        fail("not a number")
    if not all(math.isfinite(x) for x in v):
        fail("not a finite number")
    axes = [v[0:3], v[3:6], v[6:9]]
    for i in range(3):
        if abs(math.sqrt(sum(c * c for c in axes[i])) - 1) > EPS:
            fail("vector %d is not of length 1" % (i + 1))
        for j in range(i):
            if abs(sum(a * b for a, b in zip(axes[i], axes[j]))) > EPS:
                fail("vectors %d and %d are not at right angles" % (j + 1, i + 1))
    widths = []
    for u in axes:
        proj = [sum(a * b for a, b in zip(p, u)) for p in pts]
        widths.append(max(proj) - min(proj))
    if max(widths) - min(widths) > EPS * max(1.0, max(widths)):
        fail("the widths %s differ" % ", ".join("%.9f" % w for w in widths))


main()
