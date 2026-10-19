"""Generate from seed and mode: 1 small hulls, 2 rectangles, 3 thin
triangles, 4 identical maximal symmetric polygons, 5 maximal shear,
6 triangle versus maximum polygon, 7 translated small polygons,
8 a random small triangle straddling one vertex of a maximum polygon."""

from functools import lru_cache
import math
import random
import sys

MAX_COORDINATE = 100_000_000
MAX_VERTICES = 50_000
QUADRANTS = 4
QUARTER_VERTICES = MAX_VERTICES // QUADRANTS
VECTOR_LIMIT = 150
SMALL_RADIUS = 10_000
SMALL_POINTS = 12
RECTANGLE_SIZE = 1000
THIN_HEIGHT = 200
COMMON_SHIFT = 90_000_000
SMALL_MODE = 1
RECTANGLE_MODE = 2
THIN_MODE = 3
SYMMETRIC_MODE = 4
SHEAR_MODE = 5
TRIANGLE_MODE = 6
TRANSLATED_MODE = 7
CORNER_MODE = 8


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    lower, upper = [], []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def small_polygon(rng):
    radius = rng.randint(1, SMALL_RADIUS)
    points = [
        (-radius, -radius),
        (radius, -radius),
        (radius, radius),
        (-radius, radius),
    ]
    points.extend(
        (rng.randint(-2 * radius, 2 * radius), rng.randint(-2 * radius, 2 * radius))
        for _ in range(SMALL_POINTS)
    )
    return hull(points)


def rectangle(width, height):
    return [(-width, -height), (width, -height), (width, height), (-width, height)]


@lru_cache(maxsize=1)
def maximal_polygon():
    vectors = [
        (x, y)
        for x in range(1, VECTOR_LIMIT + 1)
        for y in range(1, VECTOR_LIMIT + 1)
        if math.gcd(x, y) == 1
    ]
    vectors.sort(key=lambda vector: math.atan2(vector[1], vector[0]))
    quarter = [
        vectors[i * len(vectors) // QUARTER_VERTICES] for i in range(QUARTER_VERTICES)
    ]
    edges = quarter + [(-y, x) for x, y in quarter]
    edges += [(-x, -y) for x, y in quarter] + [(y, -x) for x, y in quarter]
    points = []
    x = y = 0
    for dx, dy in edges:
        points.append((x, y))
        x, y = x + dx, y + dy
    assert (x, y) == (0, 0)
    opposite_x, opposite_y = points[MAX_VERTICES // 2]
    return tuple((2 * x - opposite_x, 2 * y - opposite_y) for x, y in points)


def cyclic_shift(points, rng):
    start = rng.randrange(len(points))
    return points[start:] + points[:start]


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == RECTANGLE_MODE:
        airport = rectangle(
            rng.randint(1, RECTANGLE_SIZE), rng.randint(1, RECTANGLE_SIZE)
        )
        cloud = rectangle(
            rng.randint(1, RECTANGLE_SIZE), rng.randint(1, RECTANGLE_SIZE)
        )
    elif mode == THIN_MODE:
        length = MAX_COORDINATE - rng.randrange(RECTANGLE_SIZE)
        height = rng.randint(1, THIN_HEIGHT)
        airport = [(-length, -height), (length, -height), (0, height)]
        cloud = rectangle(length, rng.randint(1, THIN_HEIGHT))
    elif mode in (SYMMETRIC_MODE, SHEAR_MODE, TRIANGLE_MODE):
        airport = list(maximal_polygon())
        cloud = airport.copy()
        if mode == SHEAR_MODE:
            cloud = [(x + y, y) for x, y in cloud]
        elif mode == TRIANGLE_MODE:
            cloud = [
                (-MAX_COORDINATE, -MAX_COORDINATE),
                (MAX_COORDINATE, -MAX_COORDINATE),
                (0, MAX_COORDINATE),
            ]
            if seed % 2:
                airport, cloud = cloud, airport
    elif mode == CORNER_MODE:
        airport = list(maximal_polygon())
        x, y = airport[rng.randrange(len(airport))]
        width = rng.randint(500, 5000)
        height = rng.randint(500, 5000)
        # This vertex of A is strictly inside B, guaranteeing positive overlap.
        cloud = [(x - width, y - height), (x + width, y - height), (x, y + 2 * height)]
    else:
        airport, cloud = small_polygon(rng), small_polygon(rng)
        if mode == TRANSLATED_MODE:
            airport = [(x + COMMON_SHIFT, y - COMMON_SHIFT) for x, y in airport]
            cloud = [(x + COMMON_SHIFT, y - COMMON_SHIFT) for x, y in cloud]
    return cyclic_shift(airport, rng), cyclic_shift(cloud, rng)


def render(airport, cloud):
    lines = [f"{len(airport)} {len(cloud)}"]
    lines.extend(f"{x} {y}" for x, y in airport)
    lines.extend(f"{x} {y}" for x, y in cloud)
    return "\n".join(lines) + "\n"


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode not in range(SMALL_MODE, CORNER_MODE + 1):
        raise ValueError("mode must be from 1 to 8")
    sys.stdout.write(render(*generate(seed, mode)))


if __name__ == "__main__":
    main()
