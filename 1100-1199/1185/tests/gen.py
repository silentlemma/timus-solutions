"""A castle given clockwise: a seed, N, L and a mode. Mode 0 sorts random
points by angle around the middle of the field, which gives a star-shaped
simple polygon, mode 1 puts the points on a circle, mode 2 puts them on
the sides of a rectangle, many of them in a line."""

import math
import random
import sys

LIMIT = 10000


def main():
    seed, n, gap, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    pts = set()
    while len(pts) < n:
        if mode == 1:
            a = rng.uniform(0, 2 * math.pi)
            p = (round(LIMIT * math.cos(a)), round(LIMIT * math.sin(a)))
        elif mode == 2:
            t = rng.randint(-LIMIT, LIMIT)
            p = rng.choice([(t, -LIMIT // 2), (t, LIMIT // 2), (-LIMIT, t // 2), (LIMIT, t // 2)])
        else:
            p = (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT))
        if p != (0, 0):
            pts.add(p)
    # clockwise by angle around the origin; equal angles keep the nearer
    # point first so the outline does not cross itself
    order = sorted(pts, key=lambda p: (-math.atan2(p[1], p[0]), p[0] ** 2 + p[1] ** 2))
    lines = ["%d %d" % (n, gap)] + ["%d %d" % p for p in order]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
