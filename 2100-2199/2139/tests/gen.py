"""Generate a strictly convex polygon and a sequence of continuous rotations."""

import math
import random
import sys
from functools import cmp_to_key

SCALE = 1000
DECIMAL_PLACES = 3
QUADRANTS = 4
MIN_VERTICES = 3
VERTEX_LIMIT = 100000
QUERY_LIMIT = 100000
COORDINATE_LIMIT = 100000 * SCALE
FULL_TURN = 360 * SCALE
SMALL_VERTEX_LIMIT = 40
SMALL_QUERY_LIMIT = 80
MEDIUM_VERTEX_MIN = 100
MEDIUM_VERTEX_LIMIT = 1000
MEDIUM_QUERY_LIMIT = 500
SHORT_VERTEX_LIMIT = 12
TINY_VERTEX_LIMIT = 20
LARGE_VERTEX_LIMIT = 50
LONG_VERTICES = 4096
LONG_QUERIES = 20000
SMALL_ANGLE = 60 * SCALE
MEDIUM_ANGLE = 2 * SCALE
LARGE_QUERY_COUNT = 100
OUTPUT_CHUNK = 4096
MIN_RANDOM_BUDGET = SCALE
MAX_RANDOM_BUDGET = COORDINATE_LIMIT // 10
MODE_MAXIMAL = 3
MODE_MANY_TURNS = 4
MODE_TINY = 5
MODE_TRANSLATED = 6
MODE_MONOTONE = 7
MODE_INITIAL = 8


def direction_order(first, second):
    cross = first[0] * second[1] - first[1] * second[0]
    return (cross < 0) - (cross > 0)


def polygon(count, rng, tiny=False):
    quarter = (count + QUADRANTS - 1) // QUADRANTS
    bound = math.isqrt(2 * quarter) + 1
    while True:
        directions = [
            (x, y) for x in range(1, bound + 1) for y in range(bound + 1) if math.gcd(x, y) == 1
        ]
        if len(directions) >= quarter:
            break
        bound *= 2
    rng.shuffle(directions)
    directions = sorted(directions[:quarter], key=cmp_to_key(direction_order))
    # Four rotations close the chain while keeping every edge direction distinct.
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
    if len(points) != count:
        indices = sorted(rng.sample(range(len(points)), count))
        points = [points[index] for index in indices]

    center_x = (min(x for x, _ in points) + max(x for x, _ in points)) // 2
    center_y = (min(y for _, y in points) + max(y for _, y in points)) // 2
    # Even vertex coordinates make every side midpoint exactly representable.
    points = [(2 * (x - center_x), 2 * (y - center_y)) for x, y in points]
    extent = max(max(abs(x), abs(y)) for x, y in points)
    budget = rng.randint(MIN_RANDOM_BUDGET, MAX_RANDOM_BUDGET)
    if count == VERTEX_LIMIT:
        budget = COORDINATE_LIMIT // 2
    factor = 1 if tiny else max(1, budget // extent)
    return [(x * factor, y * factor) for x, y in points]


def fixed(value):
    sign = "-" if value < 0 else ""
    integer, fraction = divmod(abs(value), SCALE)
    return f"{sign}{integer}.{fraction:0{DECIMAL_PLACES}d}"


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        count = rng.randint(MIN_VERTICES, SMALL_VERTEX_LIMIT)
        queries = rng.randint(0, SMALL_QUERY_LIMIT)
    elif mode == 2:
        count = rng.randint(MEDIUM_VERTEX_MIN, MEDIUM_VERTEX_LIMIT)
        queries = rng.randint(MEDIUM_VERTEX_MIN, MEDIUM_QUERY_LIMIT)
    elif mode == MODE_MAXIMAL:
        count = VERTEX_LIMIT
        queries = QUERY_LIMIT
    elif mode == MODE_MANY_TURNS:
        count = rng.randint(MIN_VERTICES, SHORT_VERTEX_LIMIT)
        queries = QUERY_LIMIT
    elif mode == MODE_TINY:
        count = rng.randint(MIN_VERTICES, TINY_VERTEX_LIMIT)
        queries = rng.randint(0, SMALL_QUERY_LIMIT)
    elif mode == MODE_TRANSLATED:
        count = rng.randint(MIN_VERTICES, LARGE_VERTEX_LIMIT)
        queries = LARGE_QUERY_COUNT
    elif mode == MODE_MONOTONE:
        count = LONG_VERTICES
        queries = LONG_QUERIES
    elif mode == MODE_INITIAL:
        count = rng.randint(MIN_VERTICES, MEDIUM_VERTEX_LIMIT)
        queries = 0
    else:
        raise SystemExit("mode must be between 1 and 8")

    points = polygon(count, rng, tiny=mode == MODE_TINY)
    if mode == MODE_TRANSLATED:
        shift_x = COORDINATE_LIMIT - max(x for x, _ in points)
        shift_y = -COORDINATE_LIMIT - min(y for _, y in points)
    else:
        left = -COORDINATE_LIMIT - min(x for x, _ in points)
        right = COORDINATE_LIMIT - max(x for x, _ in points)
        bottom = -COORDINATE_LIMIT - min(y for _, y in points)
        top = COORDINATE_LIMIT - max(y for _, y in points)
        shift_x = rng.randint(left, right)
        shift_y = rng.randint(bottom, top)
    points = [(x + shift_x, y + shift_y) for x, y in points]

    if mode in (MODE_MAXIMAL, MODE_MANY_TURNS, MODE_MONOTONE):
        side = max(range(count), key=lambda i: points[i][1] + points[(i + 1) % count][1])
    else:
        side = rng.randrange(count)
    first, second = points[side], points[(side + 1) % count]
    hole = ((first[0] + second[0]) // 2, (first[1] + second[1]) // 2)

    lines = [str(count)]
    lines.extend(f"{fixed(x)} {fixed(y)}" for x, y in points)
    lines.append(f"{fixed(hole[0])} {fixed(hole[1])}")
    lines.append(str(queries))
    for index in range(queries):
        if mode == MODE_MAXIMAL:
            angle = -1 if index % QUADRANTS == QUADRANTS - 1 else 1
            if index == queries - 1:
                angle = FULL_TURN
        elif mode == MODE_MANY_TURNS:
            angle = 1 if index % 2 == 0 else -1
            if index == queries - 1:
                angle = -FULL_TURN
        elif mode == MODE_MONOTONE:
            angle = rng.randint(1, 10)
            if seed % 2:
                angle = -angle
        elif mode == 2:
            angle = rng.randint(-MEDIUM_ANGLE, MEDIUM_ANGLE)
        else:
            angle = rng.randint(-SMALL_ANGLE, SMALL_ANGLE)
            if index % SHORT_VERTEX_LIMIT == 0:
                angle = rng.choice((0, FULL_TURN, -FULL_TURN, angle))
        lines.append(fixed(angle))
    for start in range(0, len(lines), OUTPUT_CHUNK):
        sys.stdout.write("\n".join(lines[start : start + OUTPUT_CHUNK]) + "\n")


if __name__ == "__main__":
    main()
