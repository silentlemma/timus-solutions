"""Checker: the time must equal the stored minimum, and the point must be L
away from the origin, have positive coordinates and give that time along
its direction, recomputed here rectangle by rectangle."""

import math
import sys

# the printed values have six decimals and times reach about 10^9
REL = 1e-7
ABS = 1e-3
DIST = 1e-3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    rects = [[int(v) for v in data[1 + 5 * i : 6 + 5 * i]] for i in range(n)]
    c0, length = int(data[1 + 5 * n]), int(data[2 + 5 * n])
    best = float(open(ans).read().split()[0])
    got = open(output).read().split()
    if len(got) != 3:
        fail("expected the time and a point")
    try:
        told, x, y = map(float, got)
    except ValueError:
        fail("not numbers")
    tol = REL * max(1.0, best) + ABS
    if abs(told - best) > tol:
        fail("time %.6f instead of %.6f" % (told, best))
    if x <= 0 or y <= 0 or abs(math.hypot(x, y) - length) > DIST:
        fail("the point is not L away with positive coordinates")
    ux, uy = x / math.hypot(x, y), y / math.hypot(x, y)
    real = c0 * length
    for x1, y1, x2, y2, c in rects:
        enter, leave = max(x1 / ux, y1 / uy), min(x2 / ux, y2 / uy)
        if leave > enter:
            real += (c - c0) * (leave - enter)
    # the point is rounded, so its time may drift a little more
    if abs(real - told) > 10 * tol:
        fail("the point gives time %.6f, not %.6f" % (real, told))


if __name__ == "__main__":
    main()
