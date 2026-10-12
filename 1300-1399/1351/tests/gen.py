"""A gun and the gnusmases: a seed and a mode. Mode 1 gives a random
sector and points, mode 2 points on the borders and on the circle of
range, mode 3 the largest count with a wide sector."""

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
