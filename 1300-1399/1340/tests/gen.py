"""A cockroach and a crumb: a seed and a mode. Mode 1 gives any place in
the kitchen, mode 2 a crumb close to the cockroach compared with the
radius, mode 3 a crumb on one of the two turning circles, mode 4 real
numbers with two decimals, mode 5 a crumb one millionth inside a turning
circle, mode 6 a nearly straight run crossing the zero-degree heading."""

import math
import random
import sys

TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    x, y = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
    angle = rng.randint(0, 360)
    radius = rng.randint(1, TOP)
    if mode == 5:
        x, y = rng.randint(-1000, 1000), rng.randint(-1000, 1000)
        radius = rng.randint(100, 2000)
        side = rng.choice([1, -1])
        h = math.radians(angle)
        cx, cy = x - side * radius * math.sin(h), y + side * radius * math.cos(h)
        turn = rng.uniform(0, 2 * math.pi)
        kx = cx + (radius - 0.000001) * math.cos(turn)
        ky = cy + (radius - 0.000001) * math.sin(turn)
        print(x, y, angle, radius)
        print("%.10f %.10f" % (kx, ky))
        return
    if mode == 6:
        x, y = rng.randint(-1000, 1000), rng.randint(-1000, 1000)
        angle = 360 - rng.uniform(0.000001, 0.00001)
        radius = TOP
        kx = x + rng.randint(100, 1000)
        ky = y + rng.uniform(0.001, 0.01)
        print("%d %d %.10f %d" % (x, y, angle, radius))
        print("%.10f %.10f" % (kx, ky))
        return
    if mode == 2:
        kx, ky = x + rng.randint(-radius, radius) // 2, y + rng.randint(-radius, radius) // 2
    elif mode == 3:
        side = rng.choice([1, -1])
        h = math.radians(angle)
        cx, cy = x - side * radius * math.sin(h), y + side * radius * math.cos(h)
        turn = rng.uniform(0, 2 * math.pi)
        kx, ky = round(cx + radius * math.cos(turn)), round(cy + radius * math.sin(turn))
    else:
        kx, ky = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
    kx, ky = max(-TOP, min(TOP, kx)), max(-TOP, min(TOP, ky))
    if mode == 4:
        print("%.2f %.2f %.2f %.2f" % (x / 3, y / 7, angle * 0.97, radius / 9))
        print("%.2f %.2f" % (kx / 3, ky / 7))
    else:
        print(x, y, angle, radius)
        print(kx, ky)


main()
