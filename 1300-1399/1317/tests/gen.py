"""A fenced lot, a laser and hailstones: a seed and a mode. The lot is a
random convex polygon with its vertices on a circle and the laser near
its centre. Mode 1 gives a small lot, mode 2 hailstones around the
distance where the laser stops reaching them, mode 3 100 hailstones over
the whole range of coordinates."""

import math
import random
import sys

TOP = 1000.0
STONES = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(3, 10)
    while True:
        cx, cy = rng.uniform(-200, 200), rng.uniform(-200, 200)
        radius = rng.uniform(1, 20 if mode == 1 else 300)
        angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(n))
        poly = [
            (round(cx + radius * math.cos(a), 2), round(cy + radius * math.sin(a), 2))
            for a in angles
        ]
        lx = round(sum(p[0] for p in poly) / n, 2)
        ly = round(sum(p[1] for p in poly) / n, 2)
        # keep the laser strictly inside
        cross = [
            (b[0] - a[0]) * (ly - a[1]) - (b[1] - a[1]) * (lx - a[0])
            for a, b in zip(poly, poly[1:] + poly[:1])
        ]
        if all(c > 1e-6 for c in cross):
            break
    if rng.random() < 0.5:
        poly.reverse()
    h = round(rng.uniform(1, 100), 2)
    d = round(rng.uniform(h + 1, 999), 2)
    stones = []
    for _ in range(rng.randint(1, 20) if mode == 1 else STONES):
        if mode == 2:
            angle = rng.uniform(0, 2 * math.pi)
            dist = rng.uniform(0.5, 1.5) * math.sqrt(max(d * d - h * h, 1))
            x, y = lx + dist * math.cos(angle), ly + dist * math.sin(angle)
        elif mode == 1:
            x, y = lx + rng.uniform(-60, 60), ly + rng.uniform(-60, 60)
        else:
            x, y = rng.uniform(-TOP, TOP), rng.uniform(-TOP, TOP)
        stones.append((max(-TOP, min(TOP, x)), max(-TOP, min(TOP, y))))
    print(n, "%.2f" % h)
    for x, y in poly:
        print("%.2f %.2f" % (x, y))
    print("%.2f %.2f %.2f" % (d, lx, ly))
    print(len(stones))
    for x, y in stones:
        print("%.2f %.2f" % (x, y))


main()
