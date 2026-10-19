"""A convex polygon and a distance from a seed and a mode: mode 1 a small
polygon, 2 the most vertices close to a large circle, 3 a long thin
needle, 4 a random polygon with d at half the perimeter, 5 a random
polygon with d just over the longest side, 6 a polygon with a few
vertices and the largest coordinates. d is an integer over the longest
side and at most half the perimeter. Mode 7 has exactly 10000 lattice
vertices and the shortest valid d; 8 removes one vertex from that polygon
and uses the largest valid d; 9 has random integer-length sides and starts
both endpoints at vertices; 10 is a sheared lattice polygon with 1000
vertices and very small turning angles."""

import math
import random
import sys

MOST = 10000
LIMIT = 10 ** 6


def lattice_polygon(rng, count, shear=False):
    bound = 70 if count >= MOST - 1 else 30
    directions = [(x, y) for y in range(bound + 1) for x in range(-bound, bound + 1)
                  if (y > 0 or x > 0) and math.gcd(x, y) == 1]
    directions = rng.sample(directions, (count + 1) // 2)
    if shear:
        directions = [(40 * x + 39 * y, x + y) for x, y in directions]
    directions += [(-x, -y) for x, y in directions]
    directions.sort(key=lambda p: math.atan2(p[1], p[0]))
    polygon, x, y = [], 0, 0
    for dx, dy in directions:
        polygon.append((x, y))
        x, y = x + dx, y + dy
    if count % 2:
        polygon.pop(rng.randrange(len(polygon)))
    cx = (min(x for x, y in polygon) + max(x for x, y in polygon)) // 2
    cy = (min(y for x, y in polygon) + max(y for x, y in polygon)) // 2
    return [(x - cx, y - cy) for x, y in polygon]


def integer_sides(rng):
    directions = set()
    for m in range(2, 22):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a, b = m * m - n * n, 2 * m * n
            directions.update(((a, b), (-a, b), (b, a), (-b, a)))
    chosen = rng.sample(sorted(directions), 100)
    chosen += [(-x, -y) for x, y in chosen]
    chosen.sort(key=lambda p: math.atan2(p[1], p[0]))
    polygon, x, y = [], 0, 0
    for dx, dy in chosen:
        polygon.append((x, y))
        x, y = x + dx, y + dy
    return polygon


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
        elif mode in (7, 8, 10):
            count = {7: MOST, 8: MOST - 1, 10: 1000}[mode]
            points = lattice_polygon(rng, count, shear=mode == 10)
        elif mode == 9:
            points = integer_sides(rng)
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
        d = {4: high, 5: low, 7: low, 8: high, 10: low}.get(mode, rng.randint(low, high))
        break
    start = rng.randrange(len(polygon))
    polygon = polygon[start:] + polygon[:start]
    if mode == 9:
        d = 0
        for i, p in enumerate(polygon):
            d += round(math.dist(p, polygon[(i + 1) % len(polygon)]))
            if d >= (low + high) // 2:
                break
    print(len(polygon))
    print("\n".join("%d %d" % p for p in polygon))
    print(d)


main()
