"""A convex polygon and a distance from a seed and a mode: mode 1 a small
polygon, 2 the most vertices close to a large circle, 3 a long thin
needle, 4 a random polygon with d at half the perimeter, 5 a random
polygon with d just over the longest side, 6 a polygon with a few
vertices and the largest coordinates. d is an integer over the longest
side and at most half the perimeter."""

import math
import random
import sys

MOST = 10000
LIMIT = 10 ** 6


def hull(points):
    # the convex hull, counter-clockwise, without collinear vertices
    points = sorted(set(points))
    if len(points) < 3:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            points = [(rng.randint(-6, 6), rng.randint(-6, 6)) for _ in range(rng.randint(3, 8))]
        elif mode == 2:
            points = []
            for _ in range(5 * MOST):
                t = rng.uniform(0, 2 * math.pi)
                points.append((round((LIMIT - 1) * math.cos(t)), round((LIMIT - 1) * math.sin(t))))
        elif mode == 3:
            points = [(rng.randint(-LIMIT, LIMIT), rng.randint(-3, 3)) for _ in range(40)]
        elif mode == 6:
            points = [(rng.choice((-LIMIT, LIMIT, rng.randint(-LIMIT, LIMIT))),
                       rng.choice((-LIMIT, LIMIT, rng.randint(-LIMIT, LIMIT))))
                      for _ in range(6)]
        else:
            points = [(rng.randint(-1000, 1000), rng.randint(-1000, 1000)) for _ in range(60)]
        polygon = hull(points)[:MOST]
        polygon = hull(polygon)
        if len(polygon) < 3:
            continue
        sides = [math.dist(polygon[i], polygon[(i + 1) % len(polygon)]) for i in range(len(polygon))]
        low, high = math.floor(max(sides)) + 1, math.floor(sum(sides) / 2)
        if low > high:
            continue
        d = {4: high, 5: low}.get(mode, rng.randint(low, high))
        break
    start = rng.randrange(len(polygon))
    polygon = polygon[start:] + polygon[:start]
    print(len(polygon))
    print("\n".join("%d %d" % p for p in polygon))
    print(d)


main()
