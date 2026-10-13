"""Up to 4000 posts: a seed and a mode. Mode 1 is random points on the
whole field, mode 2 nested triangles, 1333 hulls deep, mode 3 a 63 by 63
grid where every hull has many points on its edges, mode 4 498 nested
squares with a line of posts in the middle that makes no fence."""

import math
import random
import sys

N = 4000
SIDE = 10000
CENTRE = 5000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        points = set()
        while len(points) < N:
            points.add((rng.randint(0, SIDE), rng.randint(0, SIDE)))
        points = list(points)
    elif mode == 2:
        points = []
        r = CENTRE
        while len(points) + 3 <= N:
            for j in range(3):
                a = 2 * math.pi * j / 3 + math.pi / 2
                points.append((CENTRE + round(r * math.cos(a)), CENTRE + round(r * math.sin(a))))
            r -= 3
    elif mode == 3:
        step = SIDE // 63
        points = [(x * step, y * step) for x in range(63) for y in range(63)]
    else:
        # corners and edge middles of 499 squares, then a line of posts inside
        points = []
        r = CENTRE - 10
        while r > 10:
            for dx, dy in ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)):
                points.append((CENTRE + dx * r, CENTRE + dy * r))
            r -= 10
        points += [(CENTRE + t, CENTRE) for t in range(-4, 4)]
    rng.shuffle(points)
    print(len(points))
    print("\n".join("%d %d" % p for p in points))


main()
