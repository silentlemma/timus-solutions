"""7000 tests from a seed, mixing points, lines, rays and parabolas.

Mode 1: coordinates up to 6 in absolute value. Mode 2: coordinates up to 10^20.
Mode 3: coordinates up to 10^20 with the radius within one of the distance
from P to C, which decides the answer for a point.
Mode 4: 7000 huge, nearly parallel A and B vectors with determinant one.
Mode 5: 7000 rotated parabolas on and one unit either side of disk tangency.
Mode 6: 7000 huge rays with fractional endpoints and near-tangent disks.
Mode 7: 7000 small oblique parabolas near the nearest-point branch transition.
"""

import math
import random
import sys

TESTS = 7000
SMALL = 6
BIG = 10 ** 20
KINDS = 4  # a point, a line, a ray, a parabola


def curve(rng, top):
    a, b, c, d, e, f = (rng.randint(-top, top) for _ in range(6))
    kind = rng.randrange(KINDS)
    if kind < 2:
        a = d = 0
    if kind == 0:
        b = e = 0
    if kind == 2:
        # B parallel to A: both multiples of one small direction
        ux, uy = rng.randint(-SMALL, SMALL), rng.randint(1, SMALL)
        k = top // SMALL
        s, m = rng.randint(1, k), rng.randint(-k, k)
        a, d, b, e = ux * s, uy * s, ux * m, uy * m
    if (a, d) == (0, 0) and kind > 1:
        a = 1
    return a, b, c, d, e, f


def transform(row, rng):
    a, b, c, d, e, f, px, py, r = row
    if rng.randrange(2):
        a, b, c, d, e, f, px, py = d, e, f, a, b, c, py, px
    sx, sy = rng.choice([-1, 1]), rng.choice([-1, 1])
    return a * sx, b * sx, c * sx, d * sy, e * sy, f * sy, px * sx, py * sy, r


def targeted(mode, rng):
    if mode == 4:
        n = rng.randint(BIG // 2, BIG - 1)
        c, f, px, py = (rng.randint(-BIG, BIG) for _ in range(4))
        row = (n, n + 1, c, n - 1, n, f, px, py, rng.randint(1, SMALL))
    elif mode == 5:
        q = rng.randint(1, 10 ** 8)
        m = rng.randint(q + 1, 10 ** 9)
        c, f = (rng.randint(-BIG // 4, BIG // 4) for _ in range(2))
        row = (0, 2 * q, c, 1, 0, f, rng.randint(-BIG, BIG),
               f + m * m + q * q + rng.choice([-1, 0, 1]), 2 * q * m)
    elif mode == 6:
        n = rng.randint(BIG // 2, BIG)
        m = 2 * rng.randint(-BIG // 4, BIG // 4) + 1
        c, f = (rng.randint(-BIG // 4, BIG // 4) for _ in range(2))
        r = rng.randint(1, BIG // 8)
        endpoint_floor = c - (m * m + 4 * n - 1) // (4 * n)
        px = endpoint_floor - r + rng.choice([-1, 0, 1, 2])
        row = (n, m, c, 0, 0, f, px, rng.randint(-BIG, BIG), r)
    else:
        # Solve the branch-transition equation for the nonzero quadratic y coefficient.
        a = rng.randint(-SMALL, SMALL)
        d = rng.randint(1, SMALL) * rng.choice([-1, 1])
        b, e = rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL)
        while a * e == d * b:
            b, e = rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL)
        c, f, px = (rng.randint(-SMALL, SMALL) for _ in range(3))
        norm = a * a + d * d
        target = 2 * (a * e - d * b) ** 2 - (a * b + d * e) ** 2
        py = f + (target - 4 * norm * (px - c) * a) // (4 * norm * d)
        row = (a, b, c, d, e, f, px, py + rng.choice([-1, 0, 1]), rng.randint(1, SMALL))
    return transform(row, rng)


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else BIG
    print(TESTS)
    for _ in range(TESTS):
        if mode in (4, 5, 6, 7):
            row = targeted(mode, rng)
            for i in (0, 3, 6):
                print(*row[i:i + 3])
            continue
        a, b, c, d, e, f = curve(rng, top)
        px, py = rng.randint(-top, top), rng.randint(-top, top)
        if mode == 3:
            r = max(1, math.isqrt((px - c) ** 2 + (py - f) ** 2) + rng.randint(-1, 1))
        else:
            r = rng.randint(1, top)
        print(a, b, c)
        print(d, e, f)
        print(px, py, min(r, top))


main()
