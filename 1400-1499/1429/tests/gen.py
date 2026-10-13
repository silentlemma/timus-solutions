"""Cuts: a seed and a mode. Mode 1 is 500 large overlapping circles,
mode 2 500 small circles, mostly apart, mode 3 nested and repeated
circles around a few centres, mode 4 circles that all pass through the
origin, with centres at whole points whose distance to the origin is
whole. Mode 5 shuffles 500 cuts in separated tiles, combining two-point
pencils, closed tangency cycles, crossing pairs, enclosing circles,
isolated cuts and duplicates. Mode 6 shuffles 500 distinct nested circles
internally tangent at one common point, reaching radius 10000.
A circle whose crossings would come closer than 0.002 to another
crossing without meeting it is drawn again, as the statement promises."""

import math
import random
import sys

N = 500
SIDE = 10000


def crossings(a, b):
    (x1, y1, r1), (x2, y2, r2) = a, b
    dx, dy = x2 - x1, y2 - y1
    d2 = dx * dx + dy * dy
    if d2 == 0 or d2 > (r1 + r2) ** 2 or d2 < (r1 - r2) ** 2:
        return []
    m = d2 + r1 * r1 - r2 * r2
    root = math.sqrt(4 * d2 * r1 * r1 - m * m)
    return [
        (x1 + (m * dx - s * root * dy) / (2 * d2), y1 + (m * dy + s * root * dx) / (2 * d2))
        for s in (1, -1)
    ]


def build(rng, draw):
    circles, grid = [], {}

    def near(p):
        # a crossing closer than 0.002 to another one without being the same point
        cx, cy = int(p[0] // 2e-3), int(p[1] // 2e-3)
        for gx in (cx - 1, cx, cx + 1):
            for gy in (cy - 1, cy, cy + 1):
                if any(1e-6 < math.dist(p, q) < 2e-3 for q in grid.get((gx, gy), ())):
                    return True
        return False

    tries = 0
    while len(circles) < N and tries < 50 * N:
        tries += 1
        c = draw()
        new = [p for other in circles for p in crossings(c, other)]
        if any(near(p) for p in new) or any(
            1e-6 < math.dist(p, q) < 2e-3 for i, p in enumerate(new) for q in new[:i]
        ):
            continue
        circles.append(c)
        for p in new:
            cell = grid.setdefault((int(p[0] // 2e-3), int(p[1] // 2e-3)), [])
            if all(math.dist(p, q) > 1e-6 for q in cell):
                cell.append(p)  # each point is kept once, however many circles meet there
    return circles


def pythagorean(rng):
    while True:
        x, y = rng.randint(-SIDE // 2, SIDE // 2), rng.randint(-SIDE // 2, SIDE // 2)
        r = math.isqrt(x * x + y * y)
        if r * r == x * x + y * y and 0 < r <= SIDE:
            return x, y, r


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        circles = build(
            rng,
            lambda: (rng.randint(-3000, 3000), rng.randint(-3000, 3000), rng.randint(2000, 6000)),
        )
    elif mode == 2:
        circles = build(
            rng, lambda: (rng.randint(-SIDE, SIDE), rng.randint(-SIDE, SIDE), rng.randint(1, 600))
        )
    elif mode == 3:
        centres = [(rng.randint(-50, 50), rng.randint(-50, 50)) for _ in range(5)]
        circles = build(rng, lambda: (*rng.choice(centres), rng.randint(1, 120)))
    elif mode == 5:
        circles = []
        pencil = [(x, 0, math.isqrt(x * x + 60 * 60))
                  for x in (0, -11, 11, -25, 25, -45, 45, -80, 80, -144, 144)]
        tile = pencil + [
            (500, 0, 20), (560, 0, 40), (500, 80, 60),
            (-500, 0, 50), (-440, 0, 50), (0, -500, 1), (0, 0, 1000),
        ]
        for tx in range(-8000, 8001, 4000):
            for ty in range(-8000, 8001, 4000):
                shift_x, shift_y = tx + rng.randint(-100, 100), ty + rng.randint(-100, 100)
                turns, reflect = rng.randrange(4), rng.choice((-1, 1))
                cuts = tile + [rng.choice(tile), rng.choice(tile)]
                for x, y, r in cuts:
                    x *= reflect
                    for _ in range(turns):
                        x, y = -y, x
                    circles.append((x + shift_x, y + shift_y, r))
        rng.shuffle(circles)
    elif mode == 6:
        axis, sign = rng.randrange(2), rng.choice((-1, 1))
        circles = [(0 if axis else sign * r, sign * r if axis else 0, r)
                   for r in range(20, SIDE + 1, 20)]
        rng.shuffle(circles)
    else:
        circles = build(rng, lambda: pythagorean(rng))
    print(len(circles))
    print("\n".join("%d %d %d" % c for c in circles))


main()
