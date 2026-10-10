"""A kitchen: a seed, a mode, the number of pieces of furniture, the most
corners per piece and a size in metres. Mode 1 puts the pieces in a grid
of cells of that size, mode 2 in a row with small gaps so that the best
path visits all of them, mode 3 is the grid near the corner of the allowed
range, mode 4 scatters them over a square of that size and mode 5 is
the grid with the mouse and the cheese far away on either side. Corners are
listed clockwise or counterclockwise, and in mode 4 shuffled."""

import math
import random
import sys

SLOTS = 36
JITTER = 0.03


def polygon(rng, cx, cy, radius, kmax):
    k = rng.randint(3, kmax)
    slots = sorted(rng.sample(range(SLOTS), k))
    pts = []
    for s in slots:
        a = 2 * math.pi * s / SLOTS + rng.uniform(-JITTER, JITTER)
        pts.append((round(cx + radius * math.cos(a), 3), round(cy + radius * math.sin(a), 3)))
    if rng.random() < 0.5:
        pts.reverse()
    return pts


def inside(p, poly):
    k = len(poly)
    signs = set()
    for i in range(k):
        (ax, ay), (bx, by) = poly[i], poly[(i + 1) % k]
        c = (bx - ax) * (p[1] - ay) - (by - ay) * (p[0] - ax)
        signs.add(c > 0)
    return len(signs) == 1


def free_point(rng, lo_x, hi_x, lo_y, hi_y, polys):
    while True:
        p = (round(rng.uniform(lo_x, hi_x), 3), round(rng.uniform(lo_y, hi_y), 3))
        if not any(inside(p, poly) for poly in polys):
            return p


def main():
    seed, mode, n, kmax = (int(x) for x in sys.argv[1:5])
    size = float(sys.argv[5])
    rng = random.Random(seed)
    polys = []
    if mode in (1, 3, 5):
        side = math.ceil(math.sqrt(n))
        base = 99990.0 - side * size if mode == 3 else 0.0
        cells = rng.sample(range(side * side), n)
        for c in cells:
            cx = base + (c % side + 0.5) * size
            cy = base + (c // side + 0.5) * size
            radius = rng.uniform(0.3, size / 2 - 0.12)
            polys.append(polygon(rng, cx, cy, radius, kmax))
        span = (base - 1, base + side * size + 1)
        mouse = free_point(rng, *span, *span, polys)
        cheese = free_point(rng, *span, *span, polys)
        if mode == 5:
            mouse, cheese = (-99999.0, 0.0), (99999.0, 1.0)
    elif mode == 2:
        x = 0.0
        for _ in range(n):
            radius = rng.uniform(0.3, size)
            x += radius
            polys.append(polygon(rng, x, rng.uniform(-0.05, 0.05), radius, kmax))
            x += radius + rng.uniform(0.25, 0.5)
        mouse = (-1.0, 0.0)
        cheese = (round(x + 0.5, 3), 0.0)
    else:
        centres = []
        while len(polys) < n:
            radius = rng.uniform(0.3, 2.0)
            cx, cy = rng.uniform(0, size), rng.uniform(0, size)
            if all(math.hypot(cx - x, cy - y) > radius + r + 0.25 for x, y, r in centres):
                centres.append((cx, cy, radius))
                pts = polygon(rng, cx, cy, radius, kmax)
                rng.shuffle(pts)
                polys.append(pts)
        mouse = free_point(rng, -1, size + 1, -1, size + 1, polys)
        cheese = free_point(rng, -1, size + 1, -1, size + 1, polys)
    lines = ["%.3f %.3f %.3f %.3f" % (mouse + cheese), str(n)]
    for poly in polys:
        lines.append(str(len(poly)))
        lines += ["%.3f %.3f" % p for p in poly]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
