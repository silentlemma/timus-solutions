"""Checker: the time must equal the stored minimum, and the point must be L
away from the origin, have positive coordinates and give that time along
its direction, recomputed here rectangle by rectangle."""

import math
import sys

# the printed values have six decimals and times reach about 10^9
REL = 1e-7
ABS = 1e-3
DIST = 1e-3
ROUND = 0.5e-6
EPS = 1e-10


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
    if not all(map(math.isfinite, (told, x, y))):
        fail("not finite numbers")
    tol = REL * max(1.0, best) + ABS
    if abs(told - best) > tol:
        fail("time %.6f instead of %.6f" % (told, best))
    if x <= 0 or y <= 0 or abs(math.hypot(x, y) - length) > DIST:
        fail("the point is not L away with positive coordinates")

    def time(dx, dy):
        norm = math.hypot(dx, dy)
        ux, uy = dx / norm, dy / norm
        real = c0 * length
        for x1, y1, x2, y2, c in rects:
            enter, leave = max(x1 / ux, y1 / uy), min(x2 / ux, y2 / uy)
            if leave > enter:
                real += (c - c0) * (leave - enter)
        return real

    real = time(x, y)
    if abs(real - told) <= 10 * tol:
        return

    def matches(dx, dy):
        if dx <= 0 or dy <= 0:
            return False
        scale = length / math.hypot(dx, dy)
        return (abs(dx * scale - x) <= ROUND + EPS
                and abs(dy * scale - y) <= ROUND + EPS
                and abs(time(dx, dy) - told) <= 10 * tol)

    # Six-decimal coordinates represent a box, not a single exact direction.
    # A global optimum is at a corner ray or on a constant interval; test
    # rays and circle-arc endpoints instead of enlarging the time tolerance.
    rays = {(rx, ry) for x1, y1, x2, y2, _ in rects
            for rx in (x1, x2) for ry in (y1, y2)}
    if any(matches(dx, dy) for dx, dy in rays):
        return
    for coordinate in (x - ROUND, x + ROUND):
        if 0 < coordinate < length:
            other = math.sqrt((length - coordinate) * (length + coordinate))
            if matches(coordinate, other):
                return
    for coordinate in (y - ROUND, y + ROUND):
        if 0 < coordinate < length:
            other = math.sqrt((length - coordinate) * (length + coordinate))
            if matches(other, coordinate):
                return
    fail("the point gives time %.6f, not %.6f" % (real, told))


if __name__ == "__main__":
    main()
