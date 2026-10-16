"""One test file from a seed and a mode: mode 1 5000 random tests with
coordinates up to 10, mode 2 5000 tests with coordinates up to 3, mode 3
5000 tests where A, B and C lie on one line, so that the ravine is
straight or folds back on itself."""

import random
import sys

TESTS = 5000
LIMIT = 10
SMALL = 3


def on_segment(p, a, b):
    if (b[0] - a[0]) * (p[1] - a[1]) != (b[1] - a[1]) * (p[0] - a[0]):
        return False
    return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 2 else LIMIT
    lines = []
    while len(lines) < TESTS:
        pts = [(rng.randint(-top, top), rng.randint(-top, top)) for _ in range(5)]
        if mode == 3:
            b = pts[3]
            dx, dy = rng.randint(-2, 2), rng.randint(-2, 2)
            pts[2] = (b[0] + dx * rng.randint(1, 4), b[1] + dy * rng.randint(1, 4))
            pts[4] = (b[0] + dx * rng.randint(-4, 4), b[1] + dy * rng.randint(-4, 4))
        if len(set(pts)) < len(pts) or any(abs(x) > LIMIT for p in pts for x in p):
            continue
        s, t, a, b, c = pts
        if any(on_segment(p, a, b) or on_segment(p, b, c) for p in (s, t)):
            continue
        lines.append(" ".join("%d %d" % p for p in pts))
    print(len(lines))
    print("\n".join(lines))


main()
