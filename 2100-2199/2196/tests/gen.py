"""Deterministic convex polygons and settlements: python gen.py MODE SEED.

Modes:
1: translated random strict convex hull.
2: rectangle with collinear boundary vertices.
3: skinny large triangle.
4: maximum strict convex vertices and queries.
5: maximum queries around a small square.
6: edge and corner probes around day boundaries.
7: maximum outside normals at scattered vertices.
8: maximum vertices with a collinear run crossing the input seam.
"""

import math
import random
import sys

MODE_SMALL = 1
MODE_COLLINEAR = 2
MODE_SKINNY = 3
MODE_MAX_POLYGON = 4
MODE_MAX_QUERIES = 5
MODE_THRESHOLDS = 6
MODE_MAX_NORMALS = 7
MODE_MAX_COLLINEAR = 8
COORDINATE_LIMIT = 10**9
MAX_COUNT = 10**5
SMALL_BOUND = 30
SMALL_POINTS = 80
SMALL_QUERIES = 80
MIN_VERTICES = 3
RECTANGLE_SIDES = 4
MAX_PARTS = 25
QUERY_PADDING = 100
SAFE_MARGIN = 10**-3
FAR_DISTANCE = 4 * COORDINATE_LIMIT
LENS_HALF_WIDTH = MAX_COUNT // RECTANGLE_SIDES
LENS_HEIGHT = LENS_HALF_WIDTH**2
FAR_X_MIN = COORDINATE_LIMIT // 10
FAR_Y_MIN = LENS_HEIGHT + QUERY_PADDING
TIP_Y_BOUND = 1000
THRESHOLD_SEARCH = 10**5
THRESHOLD_DAYS = 24
THRESHOLD_OFFSETS = (-2, -1, 0, 1, 2)


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points):
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


def boundary_radii(polygon):
    area_twice = 0
    perimeter = 0.0
    origin = polygon[0]
    for index, first in enumerate(polygon):
        second = polygon[(index + 1) % len(polygon)]
        area_twice += cross(origin, first, second)
        perimeter += math.hypot(second[0] - first[0], second[1] - first[1])
    area = area_twice / 2
    radii = []
    multiplier = 2
    while not radii or radii[-1] <= FAR_DISTANCE:
        added_area = area * (multiplier - 1)
        root = math.sqrt(perimeter * perimeter + RECTANGLE_SIDES * math.pi * added_area)
        radii.append(2 * added_area / (perimeter + root))
        multiplier *= 2
    return radii


def distance(polygon, point):
    inside = True
    best_squared = math.inf
    for index, first in enumerate(polygon):
        second = polygon[(index + 1) % len(polygon)]
        dx, dy = second[0] - first[0], second[1] - first[1]
        px, py = point[0] - first[0], point[1] - first[1]
        determinant = dx * py - dy * px
        inside &= determinant >= 0
        length_squared = dx * dx + dy * dy
        projection = px * dx + py * dy
        if projection <= 0:
            candidate = px * px + py * py
        elif projection >= length_squared:
            candidate = (point[0] - second[0]) ** 2 + (point[1] - second[1]) ** 2
        else:
            candidate = determinant * determinant / length_squared
        best_squared = min(best_squared, candidate)
    return 0.0 if inside else math.sqrt(best_squared)


def safe_distance(value, radii):
    return all(abs(value - radius) >= SAFE_MARGIN for radius in radii)


def safe_queries(polygon, candidates, radii):
    return [point for point in candidates if safe_distance(distance(polygon, point), radii)]


def random_queries(polygon, rng, count, bound):
    radii = boundary_radii(polygon)
    queries = safe_queries(polygon, polygon, radii)
    while len(queries) < count:
        point = (rng.randint(-bound, bound), rng.randint(-bound, bound))
        if safe_distance(distance(polygon, point), radii):
            queries.append(point)
    rng.shuffle(queries)
    return queries[:count]


def small_case(rng):
    polygon = []
    while len(polygon) < MIN_VERTICES:
        points = [
            (rng.randint(-SMALL_BOUND, SMALL_BOUND), rng.randint(-SMALL_BOUND, SMALL_BOUND))
            for _ in range(SMALL_POINTS)
        ]
        polygon = convex_hull(points)
    scale = rng.randint(1, SMALL_BOUND)
    shift_x = rng.randint(-COORDINATE_LIMIT // 2, COORDINATE_LIMIT // 2)
    shift_y = rng.randint(-COORDINATE_LIMIT // 2, COORDINATE_LIMIT // 2)
    queries = random_queries(polygon, rng, SMALL_QUERIES, SMALL_BOUND * 2)
    polygon = [(x * scale + shift_x, y * scale + shift_y) for x, y in polygon]
    queries = [(x * scale + shift_x, y * scale + shift_y) for x, y in queries]
    return polygon, queries


def collinear_case(rng):
    parts = rng.randint(2, MAX_PARTS)
    step = rng.randint(1, SMALL_BOUND)
    side = parts * step
    polygon = [(i * step, 0) for i in range(parts)]
    polygon += [(side, i * step) for i in range(parts)]
    polygon += [(side - i * step, side) for i in range(parts)]
    polygon += [(0, side - i * step) for i in range(parts)]
    queries = random_queries(polygon, rng, SMALL_QUERIES * 2, side * 2)
    return polygon, queries


def skinny_case(rng):
    width = rng.randint(COORDINATE_LIMIT // 2, COORDINATE_LIMIT)
    height = rng.randint(1, 2)
    if rng.randrange(2):
        polygon = [(0, 0), (width, width - height), (width - height, width)]
    else:
        polygon = [(0, 0), (width, 0), (width, height)]
    queries = random_queries(polygon, rng, SMALL_QUERIES, COORDINATE_LIMIT)
    queries += safe_queries(
        polygon, [(width // 2, y) for y in range(-2, MIN_VERTICES)], boundary_radii(polygon)
    )
    return polygon, queries


def lens_polygon():
    width, height = LENS_HALF_WIDTH, LENS_HEIGHT
    polygon = [(x, x * x - height) for x in range(-width, width + 1)]
    polygon += [(x, height - x * x) for x in range(width - 1, -width, -1)]
    return polygon


def maximum_polygon(rng):
    width, height = LENS_HALF_WIDTH, LENS_HEIGHT
    polygon = lens_polygon()
    radii = boundary_radii(polygon)
    queries = []
    while len(queries) < MAX_COUNT:
        kind = rng.randrange(RECTANGLE_SIDES)
        if kind == 0:
            x = rng.randint(-width, width)
            vertical_limit = height - x * x
            point = (x, rng.randint(-vertical_limit, vertical_limit))
            value = 0.0
        elif kind == 1:
            sign = rng.choice((-1, 1))
            x = sign * rng.randint(FAR_X_MIN, COORDINATE_LIMIT)
            y = rng.randint(-TIP_Y_BOUND, TIP_Y_BOUND)
            point = (x, y)
            value = math.hypot(x - sign * width, y)
        elif kind == 2:
            y = rng.choice((-1, 1)) * rng.randint(FAR_Y_MIN, COORDINATE_LIMIT)
            point = (0, y)
            value = abs(y) - height
        else:
            point = rng.choice(polygon)
            value = 0.0
        if safe_distance(value, radii):
            queries.append(point)
    return polygon, queries


def maximum_normals(rng):
    polygon = lens_polygon()
    radii = boundary_radii(polygon)
    queries = []
    while len(queries) < MAX_COUNT:
        index = rng.randrange(len(polygon))
        first, second = polygon[index], polygon[(index + 1) % len(polygon)]
        dx, dy = second[0] - first[0], second[1] - first[1]
        normal = (dy, -dx)
        limits = []
        for coordinate, direction in zip(first, normal):
            if direction > 0:
                limits.append((COORDINATE_LIMIT - coordinate) // direction)
            elif direction < 0:
                limits.append((-COORDINATE_LIMIT - coordinate) // direction)
        multiplier = rng.randint(1, min(limits))
        point = (first[0] + multiplier * normal[0], first[1] + multiplier * normal[1])
        # The edge is a supporting line, so its endpoint is a nearest point.
        value = multiplier * math.hypot(dx, dy)
        if safe_distance(value, radii):
            queries.append(point)
    return polygon, queries


def maximum_queries(rng):
    side = rng.randint(1, SMALL_BOUND)
    polygon = [(0, 0), (side, 0), (side, side), (0, side)]
    return polygon, random_queries(polygon, rng, MAX_COUNT, COORDINATE_LIMIT)


def threshold_case(rng):
    unit_polygon = [(0, 0), (1, 0), (1, 1), (0, 1)]
    first_radius = boundary_radii(unit_polygon)[0]
    # A lattice settlement can be close to a positive-day boundary after scaling.
    candidates = []
    for side in range(1, THRESHOLD_SEARCH + 1):
        gap = abs(side * first_radius - round(side * first_radius))
        if SAFE_MARGIN <= gap:
            candidates.append((gap, side))
    candidates.sort()
    side = rng.choice(candidates[:SMALL_BOUND])[1]
    polygon = [(0, 0), (side, 0), (side, side), (0, side)]
    radii = boundary_radii(polygon)
    queries = polygon + [(side // 2, side // 2)]
    for radius in radii[:THRESHOLD_DAYS]:
        for offset in THRESHOLD_OFFSETS:
            displacement = round(radius) + offset
            edge_point = (side // 2, -displacement)
            diagonal = round(radius / math.sqrt(2)) + offset
            corner_point = (-diagonal, -diagonal)
            for point in (edge_point, corner_point):
                if max(map(abs, point)) <= COORDINATE_LIMIT:
                    if safe_distance(distance(polygon, point), radii):
                        queries.append(point)
    rng.shuffle(queries)
    return polygon, queries


def maximum_collinear(rng):
    step = rng.randint(1, COORDINATE_LIMIT // (MAX_COUNT - 2))
    width = (MAX_COUNT - 2) * step
    height = rng.randint(COORDINATE_LIMIT // 10, COORDINATE_LIMIT)
    left, bottom = -width // 2, -height // 2
    apex = (left + width // MIN_VERTICES, bottom + height)
    polygon = [(left + i * step, bottom) for i in range(MAX_COUNT - 1)]
    polygon.append(apex)
    triangle = [polygon[0], polygon[-2], apex]
    candidates = [
        (left + width // 2, bottom - 1),
        (left - 1, bottom),
        apex,
        polygon[0],
    ]
    candidates += [(x, y) for x in (-COORDINATE_LIMIT, COORDINATE_LIMIT)
                   for y in (-COORDINATE_LIMIT, COORDINATE_LIMIT)]
    return polygon, safe_queries(triangle, candidates, boundary_radii(triangle))


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    builders = {
        MODE_SMALL: small_case,
        MODE_COLLINEAR: collinear_case,
        MODE_SKINNY: skinny_case,
        MODE_MAX_POLYGON: maximum_polygon,
        MODE_MAX_QUERIES: maximum_queries,
        MODE_THRESHOLDS: threshold_case,
        MODE_MAX_NORMALS: maximum_normals,
        MODE_MAX_COLLINEAR: maximum_collinear,
    }
    polygon, queries = builders[mode](rng)
    if mode == MODE_MAX_COLLINEAR:
        rotation = rng.randrange(1, len(polygon) - 2)
    else:
        rotation = rng.randrange(len(polygon))
    polygon = polygon[rotation:] + polygon[:rotation]
    lines = [str(len(polygon))]
    lines.extend(f"{x} {y}" for x, y in polygon)
    lines.append(str(len(queries)))
    lines.extend(f"{x} {y}" for x, y in queries)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
