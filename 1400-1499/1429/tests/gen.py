"""Cuts: a seed and a mode. Mode 1 is 500 large overlapping circles,
mode 2 500 small circles, mostly apart, mode 3 nested and repeated
circles around a few centres, mode 4 circles that all pass through the
origin, with centres at whole points whose distance to the origin is
whole. A circle whose crossings would come closer than 0.002 to another
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
    else:
        circles = build(rng, lambda: pythagorean(rng))
    print(len(circles))
    print("\n".join("%d %d %d" % c for c in circles))


main()
