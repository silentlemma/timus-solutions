"""Rooms: a seed, N and a mode. Mode 1 is a spiky star around a centre
with the lamp elsewhere inside, mode 2 a comb whose teeth hide each
other, mode 3 a star on whole coordinates (many corners in line with the
lamp). Stars are sorted by the exact angle around their centre, so they
are always simple polygons."""

import random
import sys
from functools import cmp_to_key

TOP = 1000
CENTRE = 500
RADIUS = 490
TEETH_BASE = 100
SCALE = 10**4  # coordinates have four decimals


def inside(px, py, poly):
    # the even-odd rule, the lamp never lies on the border
    hit = False
    for (ax, ay), (bx, by) in zip(poly, poly[1:] + poly[:1]):
        if (ay > py) != (by > py) and px < ax + (py - ay) * (bx - ax) / (by - ay):
            hit = not hit
    return hit


def on_border(px, py, poly):
    for (ax, ay), (bx, by) in zip(poly, poly[1:] + poly[:1]):
        cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
        if cross == 0 and min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by):
            return True
    return False


def star(rng, n, unit):
    # whole points on a grid of step 1 / unit, sorted by angle around the centre
    c = CENTRE * unit
    seen = {}
    while len(seen) < n:
        x, y = (
            rng.randint(-RADIUS * unit, RADIUS * unit),
            rng.randint(-RADIUS * unit, RADIUS * unit),
        )
        if (x or y) and x * x + y * y <= (RADIUS * unit) ** 2:
            seen[(x, y)] = (x, y)

    def half(p):
        return 0 if p[1] > 0 or (p[1] == 0 and p[0] > 0) else 1

    def cmp(p, q):
        if half(p) != half(q):
            return half(p) - half(q)
        return q[0] * p[1] - q[1] * p[0]

    pts = sorted(seen.values(), key=cmp_to_key(cmp))
    keep = []
    for p in pts:
        if keep and half(keep[-1]) == half(p) and keep[-1][0] * p[1] == keep[-1][1] * p[0]:
            continue  # one corner per direction
        keep.append(p)
    return [((c + x) / unit, (c + y) / unit) for x, y in keep]


def gaps_ok(poly):
    # every turn between neighbouring corners, seen from the centre, below half a turn
    for (ax, ay), (bx, by) in zip(poly, poly[1:] + poly[:1]):
        if (ax - CENTRE) * (by - CENTRE) - (ay - CENTRE) * (bx - CENTRE) <= 0:
            return False
    return True


def comb(n):
    teeth = (n - 2) // 4
    width = TOP / (2 * teeth + 1)
    poly = [(0.0, 0.0), (TOP, 0.0)]
    for t in range(teeth, 0, -1):
        right, left = (2 * t) * width, (2 * t - 1) * width
        poly += [(round(right, 4), TOP - 1.0), (round(right, 4), TEETH_BASE)]
        poly += [(round(left, 4), TEETH_BASE), (round(left, 4), TOP - 1.0)]
    return poly


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 2:
        poly = comb(n)
    else:
        while True:
            poly = star(rng, n, 1 if mode == 3 else SCALE)
            if gaps_ok(poly):
                break
    while True:
        if mode == 3:
            px, py = rng.randint(1, TOP - 1), rng.randint(1, TOP - 1)
        else:
            px, py = round(rng.uniform(1, TOP - 1), 4), round(rng.uniform(1, TOP - 1), 4)
        if mode == 2:
            py = round(rng.uniform(1, TEETH_BASE - 1), 4)
        if inside(px, py, poly) and not on_border(px, py, poly):
            break
    fmt = "%d %d" if mode == 3 else "%.4f %.4f"
    lines = [fmt % (px, py), str(len(poly))] + [fmt % p for p in poly]
    print("\n".join(lines))


main()
