"""A fence: a seed, N, a shape and a direction (1 counterclockwise, 0
clockwise). Shape 1 is a star around the origin, vertices at equal angle
steps and random distances; shape 2 is a staircase of unit steps closed
by one corner, N even, far from convex."""

import math
import random
import sys

TOP = 50000
NEAR = 1000


def main():
    seed, n, shape, ccw = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if shape == 1:
        points = []
        for k in range(n):
            r = rng.uniform(NEAR, TOP - 1)
            a = 2 * math.pi * k / n
            points.append((round(r * math.cos(a)), round(r * math.sin(a))))
    else:
        x = y = -TOP
        points = [(x, y)]
        for _ in range((n - 2) // 2):
            x += 1
            points.append((x, y))
            y += 1
            points.append((x, y))
        points.append((-TOP, y))
    if not ccw:
        points.reverse()
    lines = [str(len(points))] + ["%d %d" % p for p in points]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
