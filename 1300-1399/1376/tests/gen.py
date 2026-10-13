"""A pyramid and a point from a seed and a mode. The base edge is from 0.1 to
10, the side edge 0.9 to 1.9 times it, the point at least 20.05 base edges
away. Mode 1 is random with any N, mode 2 has N = 32, mode 3 the flattest
pyramid with N = 32, mode 4 the tallest with N = 32, mode 5 a small N,
mode 6 the point on an axis. Mode 7 has N = 9 and a point exactly at the
minimum distance on a 3:4 ray; mode 8 has both edges maximal and N = 32;
mode 9 has the minimum edge ratio, N = 31 and a distant almost axial point;
mode 10 has the minimum lateral edge, N = 12 and a point just off -y,
just above the minimum allowed radius."""

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
    if mode == 7:
        units = rng.randint(12, 500)
        side = rng.randint(max(10, (9 * units + 9) // 10), min(1000, 19 * units // 10))
        x = rng.choice([-1, 1]) * 1203 * units
        y = rng.choice([-1, 1]) * 1604 * units
        print(f"{units / 100:.2f} {side / 100:.2f} {x / 10000:.4f} {y / 10000:.4f} 9")
        return
    if mode == 8:
        x, y = -rng.randint(115000, 130000), -rng.randint(165000, 180000)
        print(f"10 10 {x / 1000:.3f} {y / 1000:.3f} 32")
        return
    if mode == 9:
        units = rng.randint(20, 100)
        x, y = -rng.randint(1000000, 2000000), rng.randint(1, 10000)
        print(f"{units / 10:.1f} {9 * units / 100:.2f} {x / 1000:.3f} {y / 1000:.3f} 31")
        return
    if mode == 10:
        print(f"0.11 0.1 {rng.randint(1, 9) / 100000:.5f} -2.2055 12")
        return
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
