"""A convex polygon with n vertices in counter-clockwise order and three
decimals: a seed, n and a mode. Mode 0 takes random points of a circle,
mode 1 of a long thin ellipse, mode 2 a regular polygon, mode 3 a few
points spread over a circle and the rest crowded on a short arc."""

import math
import random
import sys

RADIUS = 1000.0
THIN = 0.05
CROWD = 0.3


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 2:
        angles = [2 * math.pi * k / n for k in range(n)]
    elif mode == 3:
        few = max(1, n // 10)
        angles = [rng.uniform(0, 2 * math.pi) for _ in range(few)]
        angles += [rng.uniform(0, CROWD) for _ in range(n - few)]
    else:
        angles = [rng.uniform(0, 2 * math.pi) for _ in range(n)]
    angles.sort()
    squash = THIN if mode == 1 else 1.0
    pts = []
    for a in angles:
        p = (round(RADIUS * math.cos(a), 3), round(RADIUS * squash * math.sin(a), 3))
        if p not in pts:
            pts.append(p)
    shift = rng.randrange(len(pts))
    pts = pts[shift:] + pts[:shift]
    lines = [str(len(pts))] + ["%.3f %.3f" % p for p in pts]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
