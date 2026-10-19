"""7000 tests from a seed, mixing points, lines, rays and parabolas.

Mode 1: coordinates up to 6 in absolute value. Mode 2: coordinates up to 10^20.
Mode 3: coordinates up to 10^20 with the radius within one of the distance
from P to C, which decides the answer for a point.
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


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else BIG
    print(TESTS)
    for _ in range(TESTS):
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
