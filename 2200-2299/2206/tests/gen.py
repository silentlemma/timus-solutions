"""Print a deterministic convex polygon: python gen.py MODE SEED."""

import math
import random
import sys
from functools import cmp_to_key

SCALE = 1000
DECIMAL_PLACES = 3
MAX_COORDINATE = 2_000_000 * SCALE
MAX_VERTICES = 200_000
MIN_VERTICES = 3
SMALL_POOL = 40
SMALL_SPAN = 30 * SCALE
DIRECTION_BOUND = 300
QUADRANTS = 4
HALF = 500
NEAR_LIMIT_SPAN = 100 * SCALE


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def maximum_polygon():
    directions = [
        (x, y)
        for x in range(1, DIRECTION_BOUND + 1)
        for y in range(1, DIRECTION_BOUND + 1)
        if math.gcd(x, y) == 1
    ]
    directions.sort(key=cmp_to_key(lambda a, b: a[1] * b[0] - a[0] * b[1]))
    directions = directions[: MAX_VERTICES // QUADRANTS]
    edges = []
    for _ in range(QUADRANTS):
        edges.extend(directions)
        directions = [(-y, x) for x, y in directions]
    points = []
    x = y = 0
    for dx, dy in edges:
        points.append((x, y))
        x += dx
        y += dy
    xmin = min(x for x, _ in points)
    ymin = min(y for _, y in points)
    extent = max(max(x for x, _ in points) - xmin, max(y for _, y in points) - ymin)
    factor = (MAX_COORDINATE - SCALE) // extent
    return [(SCALE + (x - xmin) * factor, SCALE + (y - ymin) * factor) for x, y in points]


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "max_vertices":
        points = maximum_polygon()
    elif mode == "max_square":
        points = [(SCALE, SCALE), (MAX_COORDINATE, SCALE)]
        points += [(MAX_COORDINATE, MAX_COORDINATE), (SCALE, MAX_COORDINATE)]
    elif mode == "triangle":
        points = [(SCALE, SCALE), (MAX_COORDINATE, SCALE)]
        points += [(rng.randrange(SCALE, MAX_COORDINATE), MAX_COORDINATE)]
    elif mode == "thin":
        points = [(SCALE, SCALE), (MAX_COORDINATE, MAX_COORDINATE - 1)]
        points += [(MAX_COORDINATE - 1, MAX_COORDINATE), (SCALE, SCALE + 1)]
    elif mode == "strip":
        bottom = MAX_COORDINATE // 2 + rng.randrange(1, SCALE)
        points = [(SCALE, bottom), (MAX_COORDINATE, bottom + SCALE)]
        points += [(MAX_COORDINATE, MAX_COORDINATE), (SCALE, MAX_COORDINATE - 1)]
    elif mode in ("small", "integer", "high", "fractional"):
        while True:
            points = [
                (rng.randrange(SCALE, SMALL_SPAN), rng.randrange(SCALE, SMALL_SPAN))
                for _ in range(SMALL_POOL)
            ]
            if mode == "integer":
                points = [(x // SCALE * SCALE, y // SCALE * SCALE) for x, y in points]
            elif mode == "fractional":
                points = [
                    (x // SCALE * SCALE + 1, y // SCALE * SCALE + SCALE - 1) for x, y in points
                ]
            points = hull(points)
            if len(points) >= MIN_VERTICES:
                break
        if mode == "high":
            shift = MAX_COORDINATE - NEAR_LIMIT_SPAN
            points = [(x + shift, y + shift) for x, y in points]
    elif mode == "empty":
        x = rng.randrange(SCALE, MAX_COORDINATE // 2) // SCALE * SCALE + 1
        y = rng.randrange(SCALE, MAX_COORDINATE // 2) // SCALE * SCALE + 1
        points = [(x, y), (x + HALF, y), (x, y + HALF)]
    else:
        raise SystemExit("unknown mode")
    rotation = rng.randrange(len(points))
    return points[rotation:] + points[:rotation]


def main():
    points = generate(sys.argv[1], int(sys.argv[2]))
    print(len(points))
    for x, y in points:
        sx = f"{x // SCALE}.{x % SCALE:0{DECIMAL_PLACES}d}"
        sy = f"{y // SCALE}.{y % SCALE:0{DECIMAL_PLACES}d}"
        print(sx, sy)


if __name__ == "__main__":
    main()
