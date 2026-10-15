"""One test from a seed and a mode: the piece is the triangle moved by a
random lattice isometry (mode 1 any, mode 2 a single reflection, mode 3
a glide reflection, mode 4 a rotation or translation), with its corners
listed in random order; mode 5 changes one coordinate so that no isometry
fits; mode 6 uses isosceles right triangles, which match themselves."""

import random
import sys

LIMIT = 2000
SPAN = 300


def reflect(p, kind, k):
    x, y = p
    if kind == 0:
        return (2 * k - x, y)  # the line x = k
    if kind == 1:
        return (x, 2 * k - y)  # the line y = k
    if kind == 2:
        return (y - k, x + k)  # the line y = x + k
    return (k - y, k - x)  # the line x + y = k


def rotate(p, c, quarter):
    x, y = p[0] - c[0], p[1] - c[1]
    for _ in range(quarter):
        x, y = -y, x
    return (x + c[0], y + c[1])


def triangle(rng, isosceles):
    while True:
        if isosceles:
            x, y, a, b = (rng.randint(-SPAN, SPAN) for _ in range(4))
            pts = [(x, y), (x + a, y + b), (x - b, y + a)]
        else:
            pts = [(rng.randint(-SPAN, SPAN), rng.randint(-SPAN, SPAN)) for _ in range(3)]
        (x1, y1), (x2, y2), (x3, y3) = pts
        if (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1):
            return pts


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    target = triangle(rng, mode == 6)
    kind = mode if mode in (2, 3, 4) else rng.choice([2, 3, 4])
    cur = list(target)
    if kind in (2, 3):
        how, k = rng.randrange(4), rng.randint(-SPAN, SPAN)
        cur = [reflect(p, how, k) for p in cur]
        if kind == 3:  # slide along the mirror
            t = rng.randint(1, SPAN)
            dx, dy = [(0, t), (t, 0), (t, t), (t, -t)][how]
            cur = [(x + dx, y + dy) for x, y in cur]
    else:
        c = (rng.randint(-SPAN, SPAN), rng.randint(-SPAN, SPAN))
        quarter = rng.randrange(4)
        cur = [rotate(p, c, quarter) for p in cur]
        dx, dy = rng.randint(-SPAN, SPAN), rng.randint(-SPAN, SPAN)
        cur = [(x + dx, y + dy) for x, y in cur]
    if mode == 5:
        i = rng.randrange(3)
        cur[i] = (cur[i][0] + rng.choice([-1, 1]), cur[i][1])
    rng.shuffle(cur)
    assert all(abs(v) <= LIMIT for p in target + cur for v in p)
    print(*[v for p in target for v in p])
    print(*[v for p in cur for v in p])


main()
