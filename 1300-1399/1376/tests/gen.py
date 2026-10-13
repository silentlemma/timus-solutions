"""A pyramid and a point from a seed and a mode. The base edge is from 0.1 to
10, the side edge 0.9 to 1.9 times it, the point at least 20.05 base edges
away. Mode 1 is random with any N, mode 2 has N = 32, mode 3 the flattest
pyramid with N = 32, mode 4 the tallest with N = 32, mode 5 a small N,
mode 6 the point on an axis."""

import math
import random
import sys

SMALLEST, LARGEST = 0.1, 10.0
FLAT, TALL = 0.9, 1.9
NEAR, FAR = 20.05, 40.0  # the distance to the point, in base edges
MOST_ROLLS = 32
DIGITS = 4
SCALE = 10**DIGITS


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    ratio = {3: FLAT, 4: TALL}.get(mode, rng.uniform(FLAT, TALL))
    # both edges from SMALLEST to LARGEST
    s = round(rng.uniform(max(SMALLEST, SMALLEST / ratio), min(LARGEST, LARGEST / ratio)), DIGITS)
    side = round(s * ratio, DIGITS)
    side = max(side, math.ceil(s * FLAT * SCALE) / SCALE, SMALLEST)
    side = min(side, math.floor(s * TALL * SCALE) / SCALE, LARGEST)
    n = (
        MOST_ROLLS
        if mode in (2, 3, 4)
        else rng.randint(2, 5)
        if mode == 5
        else rng.randint(2, MOST_ROLLS)
    )
    angle = (
        rng.choice([0, math.pi / 2, math.pi, -math.pi / 2])
        if mode == 6
        else rng.uniform(0, 2 * math.pi)
    )
    far = rng.uniform(NEAR + 0.01, FAR) * s
    x, y = round(far * math.cos(angle), 3), round(far * math.sin(angle), 3)
    print(s, side, x, y, n)


main()
