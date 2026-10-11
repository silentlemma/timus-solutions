"""Four distances AD, AC, BD and BC: a seed and a mode. Mode 1 rounds the
distances of four points placed in order on a random circle, mode 2
takes any four numbers, mode 3 makes AD * AC = BD * BC."""

import math
import random
import sys

TOP = 10000
POINTS = 4


def on_circle(rng):
    while True:
        r = rng.uniform(1, TOP / 2)
        angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(POINTS))
        a, b, c, d = ((r * math.cos(t), r * math.sin(t)) for t in angles)
        values = [round(math.dist(p, q)) for p, q in ((a, d), (a, c), (b, d), (b, c))]
        if min(values) >= 1:
            return values


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        values = on_circle(rng)
    elif mode == 2:
        values = [rng.randint(1, TOP) for _ in range(POINTS)]
    else:
        # AD * AC = p * q * r * s = BD * BC
        p, q, r, s = (rng.randint(1, int(TOP**0.5)) for _ in range(POINTS))
        values = [p * q, r * s, p * r, q * s]
    print(*values)


main()
