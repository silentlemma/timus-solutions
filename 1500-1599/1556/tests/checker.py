"""Checker: the line has the expected shape, the direction is a unit
vector, and shooting along it scores the expected average within 1e-4,
the printed average too. A ray touching a cow up to the rounding of the
ten printed digits counts as a hit."""

import math
import re
import sys

MOST_HITS = 5
TOLERANCE = 1e-4
UNIT = 1e-8
SHAPE = re.compile(r"The best shot at \((\S+);(\S+)\) gives Vasya (\S+) average hits\.$")


def score(data, dx, dy):
    n, k, p = int(data[0]), int(data[1]), int(data[2])
    r, vx, vy = float(data[3]), float(data[4]), float(data[5])
    cows = [(float(data[6 + 2 * j]) - vx, float(data[7 + 2 * j]) - vy) for j in range(n)]
    main = math.atan2(dy, dx)
    total = 0.0
    for i in range(k):
        a = main + math.atan(i / (k - 1) - 0.5)
        ux, uy = math.cos(a), math.sin(a)
        hits = 0
        for cx, cy in cows:
            along = cx * ux + cy * uy
            if along > 0 and abs(cx * uy - cy * ux) <= r + 2e-10 * along + 1e-9:
                hits += 1
        total += sum((p / 100) ** j for j in range(min(hits, MOST_HITS)))
    return total


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    want = SHAPE.match(open(expected).read().strip())
    got = SHAPE.match(open(output).read().strip())
    if not got:
        fail("the line does not have the required shape")
    dx, dy, value = (float(v) for v in got.groups())
    if abs(dx * dx + dy * dy - 1) > UNIT:
        fail("the direction is not a unit vector")
    best = float(want.group(3))
    actual = score(data, dx, dy)
    if abs(actual - best) > TOLERANCE or abs(value - best) > TOLERANCE:
        fail("the shot scores %.6f and claims %.6f, the best is %.6f" % (actual, value, best))


main()
