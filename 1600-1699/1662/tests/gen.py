"""One test from a seed and a mode: mode 1 a small polygon with small
ropes, mode 2 up to 50 vertices near a circle with R close to the
diameter, mode 3 a triangle or quadrilateral, mode 4 a polygon anywhere in
the field with any ropes."""

import math
import random
import sys

FIELD = 1000
MOST = 50
LONGEST = 1000


def hull(points):
    points = sorted(set(points))

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 2:
            radius = rng.randint(50, 400)
            cx, cy = rng.randint(-500, 500), rng.randint(-500, 500)
            pts = []
            for _ in range(rng.randint(10, 80)):
                a = rng.uniform(0, 2 * math.pi)
                pts.append((round(cx + radius * math.cos(a)), round(cy + radius * math.sin(a))))
        else:
            span = {1: 10, 3: 30, 4: rng.randint(100, 400)}[mode]
            count = {1: 8, 3: 4, 4: 30}[mode]
            cx, cy = rng.randint(-FIELD + span, FIELD - span), rng.randint(-FIELD + span, FIELD - span)
            pts = [(cx + rng.randint(-span, span), cy + rng.randint(-span, span))
                   for _ in range(count)]
            pts = [(min(FIELD, max(-FIELD, x)), min(FIELD, max(-FIELD, y))) for x, y in pts]
        poly = hull(pts)
        if 3 <= len(poly) <= MOST and (mode != 3 or len(poly) <= 4):
            break
    if rng.random() < 0.5:
        poly.reverse()
    shift = rng.randrange(len(poly))
    poly = poly[shift:] + poly[:shift]
    diameter = max(math.dist(p, q) for p in poly for q in poly)
    small = rng.randint(1, max(1, round(diameter * rng.uniform(0.05, 0.6))))
    big = round(diameter * rng.uniform(0.6, 1.1) + small * rng.uniform(0.5, 1.5))
    big = max(small + 1, min(LONGEST, big))
    small = min(small, big - 1)
    print(len(poly))
    for x, y in poly:
        print(x, y)
    print(small, big)


main()
