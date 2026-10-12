"""A gun and the gnusmases: a seed and a mode.

Mode 1: random sector and points.
Mode 2: points on the borders and near the circle of range.
Mode 3: largest count with a wide sector.
Mode 4: largest count on, behind and beside a scaled zero-width ray.
Mode 5: largest range and count, exact integer circle neighbors facing west.
"""

import math
import random
import sys

TOP = 30000
COUNT = 30000


def border(rng):
    return rng.choice((-1, 1)) * rng.randint(1, TOP), rng.choice((-1, 1)) * rng.randint(1, TOP)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (4, 5):
        header = (TOP, 22500, -30000, 18000, -24000) if mode == 4 else (TOP, -1, 1, -1, -1)
        print(*header)
        print(COUNT)
        for i in range(COUNT):
            if mode == 4:
                k = rng.randint(1, 7499)
                kind = i % 5
                x, y = 3 * k, -4 * k
                if kind == 1:
                    x, y = -x, -y
                elif kind == 2:
                    x += 1
                elif kind == 3:
                    y += 1
                elif kind == 4:
                    x, y = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
            else:
                y = rng.randint(-TOP, TOP)
                edge = math.isqrt(TOP * TOP - y * y)
                # The negative root is on/inside the disk; one step farther
                # west is outside. Clamping keeps coordinates within limits.
                x = max(-TOP, min(TOP, -edge + (i % 3) - 1))
            if x == 0 and y == 0:
                x = 1
            print(x, y)
        return
    while True:
        (rx, ry), (lx, ly) = border(rng), border(rng)
        if rx * ly - ry * lx > 0:  # counterclockwise and narrower than a half turn
            break
    if mode == 3:
        while rx * ly - ry * lx < TOP * TOP:  # make the sector wide
            (rx, ry), (lx, ly) = border(rng), border(rng)
    reach = rng.randint(1, TOP)
    points = []
    for _ in range(COUNT if mode == 3 else 2000):
        kind = rng.randint(0, 2) if mode == 2 else 0
        if kind == 1:  # a multiple of a border vector
            bx, by = rng.choice(((rx, ry), (lx, ly)))
            g = math.gcd(bx, by)
            k = rng.randint(1, TOP // max(abs(bx), abs(by)) * g)
            x, y = bx // g * k, by // g * k
        elif kind == 2:  # near the circle of range
            a = rng.uniform(0, 2 * math.pi)
            x, y = round(reach * math.cos(a)), round(reach * math.sin(a))
        else:
            x, y = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
        if x == 0 and y == 0:
            x = 1
        points.append(f"{x} {y}")
    print(reach, rx, ry, lx, ly)
    print(len(points))
    print("\n".join(points))


main()
