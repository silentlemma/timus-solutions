"""Flies and swatter marks from a seed and a mode: mode 1 a few small
polygons on a small grid with a fly on every point of it, 2 many
star-shaped polygons with long sides and the most flies, 3 polygons
with horizontal, vertical and diagonal sides, flies on a dense grid, so
that many sit on the borders, 4 the most marks, all triangles, 5 one
mark with the most vertices, 6 thin strips across the whole wall, so
that many sides are crossed by one vertical line. Every polygon lies in
its own cell and goes counter-clockwise."""

import math
import random
import sys

MOST = 100000
MARKS = 30000
LIMIT = 10 ** 7


def star(rng, cx, cy, r, k):
    # k corners at increasing angles around (cx, cy), at least r / 3 away:
    # one in the first quarter of each of k equal sectors, so every gap is
    # below a half turn and the polygon is star-shaped and counter-clockwise
    sector = r / k
    points = []
    for i in range(k):
        t = 2 * math.pi * int(sector * (i + rng.random() / 4)) / r
        d = rng.randint(r // 3, r)
        p = (cx + round(d * math.cos(t)), cy + round(d * math.sin(t)))
        if not points or p != points[-1]:
            points.append(p)
    if len(points) > 2 and points[0] == points[-1]:
        points.pop()
    return points


def octagon(rng, cx, cy, r):
    # a convex polygon with sides at multiples of 45 degrees
    a, b, c, d = (rng.randint(0, r // 2) for _ in range(4))
    ring = [(cx - r + a, cy - r), (cx + r - b, cy - r), (cx + r, cy - r + b),
            (cx + r, cy + r - c), (cx + r - c, cy + r), (cx - r + d, cy + r),
            (cx - r, cy + r - d), (cx - r, cy - r + a)]
    out = []
    for p in ring:
        if not out or p != out[-1]:
            out.append(p)
    if out[0] == out[-1]:
        out.pop()
    return out


def cells(count, size):
    side = math.isqrt(count - 1) + 1
    return [(-LIMIT + size * (2 * i + 1), -LIMIT + size * (2 * j + 1))
            for i in range(side) for j in range(side)][:count]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    marks, flies = [], set()
    if mode == 1:
        for cx, cy in rng.sample([(x, y) for x in (4, 14, 24) for y in (4, 14)], rng.randint(1, 4)):
            marks.append(star(rng, cx, cy, 4, rng.randint(3, 4)) if rng.random() < 0.5
                         else octagon(rng, cx, cy, 4))
        flies = {(x, y) for x in range(-1, 30) for y in range(-1, 20)}
    elif mode in (2, 4):
        count = 2000 if mode == 2 else MARKS
        size = LIMIT // (math.isqrt(count) + 1)
        for cx, cy in cells(count, size):
            marks.append(star(rng, cx, cy, size - 2, 40 if mode == 2 else 3))
    elif mode == 3:
        size = 40
        for cx, cy in cells(2000, size):
            marks.append(octagon(rng, cx, cy, size - 2))
        while len(flies) < MOST:
            cx, cy = rng.choice(marks)[0]
            flies.add((cx + rng.randint(-3 * size, 3 * size), cy + rng.randint(-3 * size, 3 * size)))
    elif mode == 5:
        marks.append(star(rng, 0, 0, LIMIT - 1, MOST - 1))
    else:
        # from the top down, so that each new strip goes below all others
        for i in reversed(range(MOST // 4)):
            marks.append([(-LIMIT, 3 * i), (LIMIT, 3 * i + 1), (LIMIT, 3 * i + 2),
                          (-LIMIT, 3 * i + 1)])
        while len(flies) < MOST:
            flies.add((rng.randint(-LIMIT, LIMIT), rng.randint(-1, 3 * len(marks))))
    corners = [p for mark in marks for p in mark]
    while mode != 1 and len(flies) < MOST:
        if rng.random() < 0.1:
            flies.add(rng.choice(corners))
        elif rng.random() < 0.5:
            mark = rng.choice(marks)
            a, b = rng.sample(mark, 2)
            flies.add(((a[0] + b[0]) // 2, (a[1] + b[1]) // 2))
        else:
            flies.add((rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)))
    flies = sorted(flies)
    rng.shuffle(flies)
    print(len(flies))
    print("\n".join("%d %d" % p for p in flies))
    print(len(marks))
    print("\n".join(" ".join([str(len(mark))] + ["%d %d" % p for p in mark]) for mark in marks))


main()
