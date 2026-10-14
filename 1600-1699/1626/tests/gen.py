"""One test from a seed and a mode: a star-shaped polygon around the origin
(vertices at jittered, evenly spread angles with random radii) and a
segment near the origin. Mode 1 up to 40 vertices, mode 2 800 vertices
with a short segment, mode 3 800 vertices with a long segment, mode 4 a
convex lattice polygon of up to 800 vertices, mode 5 up to 12 vertices,
mode 6 a small convex polygon and a long segment (often impossible)."""

import math
import random
import sys
from math import gcd

LIMIT = 10**4
MOST = 800
JITTER = 0.4  # keeps every angular gap below a half turn


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def meets(a, b, c, d):
    """segments ab and cd share a point"""
    d1, d2, d3, d4 = cross(a, b, c), cross(a, b, d), cross(c, d, a), cross(c, d, b)
    if (d1 > 0 and d2 > 0) or (d1 < 0 and d2 < 0) or (d3 > 0 and d4 > 0) or (d3 < 0 and d4 < 0):
        return False
    return (
        min(a[0], b[0]) <= max(c[0], d[0])
        and min(c[0], d[0]) <= max(a[0], b[0])
        and min(a[1], b[1]) <= max(c[1], d[1])
        and min(c[1], d[1]) <= max(a[1], b[1])
    )


def star(rng, n):
    while True:
        pts = []
        for i in range(n):
            t = 2 * math.pi * (i + rng.uniform(0, JITTER)) / n
            r = rng.uniform(0.2, 0.95) * LIMIT
            pts.append((round(r * math.cos(t)), round(r * math.sin(t))))
        if len(set(pts)) == n and all(cross(pts[i - 1], pts[i], pts[(i + 1) % n]) for i in range(n)):
            return pts


def convex(rng, n):
    """primitive lattice vectors sorted by angle sum to zero and make a
    strictly convex polygon; adjacent ones are merged down to n edges"""
    reach = 1
    while True:
        vecs = [
            (dx, dy)
            for dx in range(-reach, reach + 1)
            for dy in range(-reach, reach + 1)
            if (dx or dy) and gcd(abs(dx), abs(dy)) == 1 and abs(dx) + abs(dy) <= reach
        ]
        if len(vecs) >= n:
            break
        reach += 1
    vecs.sort(key=lambda v: math.atan2(v[1], v[0]))
    while len(vecs) > n:
        i = rng.randrange(len(vecs))
        j = (i + 1) % len(vecs)
        merged = (vecs[i][0] + vecs[j][0], vecs[i][1] + vecs[j][1])
        vecs[i] = merged
        del vecs[j]
    pts, x, y = [], 0, 0
    for dx, dy in vecs:
        pts.append((x, y))
        x, y = x + dx, y + dy
    cx = (min(p[0] for p in pts) + max(p[0] for p in pts)) // 2
    cy = (min(p[1] for p in pts) + max(p[1] for p in pts)) // 2
    pts = [(px - cx, py - cy) for px, py in pts]
    # stretched to fill the coordinate range: still strictly convex
    scale = max(1, LIMIT * 9 // 10 // max(max(abs(x), abs(y)) for x, y in pts))
    return [(px * scale, py * scale) for px, py in pts]


def inside(pts, p):
    hit = False
    n = len(pts)
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        if (a[1] > p[1]) != (b[1] > p[1]):
            x = a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1])
            if p[0] < x:
                hit = not hit
    return hit


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    sizes = {1: (3, 40), 2: (MOST, MOST), 3: (MOST, MOST), 4: (3, MOST), 5: (3, 12), 6: (4, 10)}
    n = rng.randint(*sizes[mode])
    pts = convex(rng, n) if mode in (4, 6) else star(rng, n)
    span = max(max(abs(x), abs(y)) for x, y in pts)
    reach = max(1, span // {3: 6, 4: 6, 6: 1}.get(mode, 40))
    while True:
        s = [rng.randint(-reach, reach) for _ in range(4)]
        a, b = (s[0], s[1]), (s[2], s[3])
        if a == b or not inside(pts, a):
            continue
        if not any(meets(a, b, pts[i], pts[(i + 1) % n]) for i in range(n)):
            break
    print(n)
    for x, y in pts:
        print(x, y)
    print(*s)


main()
