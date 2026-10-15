"""Checker: "No solution" exactly when the expected answer says so;
otherwise a point outside the bed, within R of every vertex and at least
r from the bed, within 1e-5."""

import math
import sys

EPS = 1e-5
NONE = "No solution"


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    pts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    small, big = int(data[1 + 2 * n]), int(data[2 + 2 * n])
    want = open(expected).read().strip()
    got = open(output).read().strip()
    if want == NONE or got == NONE:
        if want != got:
            fail("expected %r, got %r" % (want if want == NONE else "a point", got))
        return
    words = got.split()
    if len(words) != 2:
        fail("expected two numbers")
    try:
        x, y = (float(w) for w in words)
    except ValueError:
        fail("not a number")
    if not (math.isfinite(x) and math.isfinite(y)):
        fail("not a finite number")
    for vx, vy in pts:
        if math.hypot(x - vx, y - vy) > big + EPS:
            fail("the goat cannot reach vertex (%d, %d)" % (vx, vy))
    turn = sum(pts[i - 1][0] * pts[i][1] - pts[i][0] * pts[i - 1][1] for i in range(n))
    side = 1 if turn > 0 else -1
    nearest = math.inf
    outside = False
    for i in range(n):
        (ax, ay), (bx, by) = pts[i - 1], pts[i]
        ex, ey = bx - ax, by - ay
        if side * (ex * (y - ay) - ey * (x - ax)) < 0:
            outside = True
        t = min(1.0, max(0.0, ((x - ax) * ex + (y - ay) * ey) / (ex * ex + ey * ey)))
        nearest = min(nearest, math.hypot(x - ax - t * ex, y - ay - t * ey))
    if not outside:
        fail("the stake is inside the bed")
    if nearest < small - EPS:
        fail("the kid reaches the bed")


main()
