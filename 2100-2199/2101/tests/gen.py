"""Print one deterministic triangle and a strictly interior integer point."""

import random
import sys

MAX_COORDINATE = 10000
SMALL_COORDINATE = 20
VERTICES = 3
POINTS = VERTICES + 1
MIN_SIDE = 3
THIN_HEIGHT = 3
QUARTER_TURNS = 4
RANDOM_SMALL = 1
RANDOM_LARGE = 2
RIGHT = 3
SYMMETRIC = 4
OBTUSE = 5
THIN = 6
MAXIMUM = 7
NEAR_RIGHT = 8


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def inside(points):
    triangle = points[:VERTICES]
    signs = [
        cross(triangle[i], triangle[(i + 1) % VERTICES], points[VERTICES]) for i in range(VERTICES)
    ]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def random_points(rng, bound):
    while True:
        points = [(rng.randint(-bound, bound), rng.randint(-bound, bound)) for _ in range(POINTS)]
        if inside(points):
            return points


def right_triangle(rng, maximum):
    limit = MAX_COORDINATE
    width = 2 * limit if maximum else rng.randint(MIN_SIDE, 2 * limit)
    height = 2 * limit if maximum else rng.randint(MIN_SIDE, 2 * limit)
    while True:
        x = rng.randint(1, width - 1)
        upper = (height * (width - x) - 1) // width
        if upper > 0:
            y = rng.randint(1, upper)
            break
    return [
        (-limit, -limit),
        (width - limit, -limit),
        (-limit, height - limit),
        (x - limit, y - limit),
    ]


def generate(mode, rng):
    limit = MAX_COORDINATE
    if mode == RANDOM_SMALL:
        return random_points(rng, SMALL_COORDINATE)
    if mode == RANDOM_LARGE:
        return random_points(rng, limit)
    if mode in (RIGHT, MAXIMUM):
        return right_triangle(rng, mode == MAXIMUM)
    if mode == SYMMETRIC:
        half_width = rng.randint(2, limit)
        height = rng.randint(half_width + 1, 2 * limit)
        y = rng.randint(1, height - 1)
        return [(-half_width, -limit), (half_width, -limit), (0, height - limit), (0, y - limit)]
    if mode == OBTUSE:
        width = rng.randint(limit // 2, limit)
        offset = rng.randint(1, limit)
        upper = (limit * width - 1) // (width + offset)
        return [(0, 0), (width, 0), (-offset, limit), (0, rng.randint(1, upper))]
    if mode == THIN:
        x = rng.randint(0, limit - 1)
        return [(-limit, -limit), (limit, limit - THIN_HEIGHT), (limit, limit), (x, x - 1)]
    if mode == NEAR_RIGHT:
        return [(0, 0), (limit, 0), (-1, limit), (0, rng.randint(1, limit - 1))]
    raise ValueError("mode must be between 1 and 8")


def main():
    if len(sys.argv) != VERTICES:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    points = generate(mode, rng)
    if rng.randrange(2):
        points = [(-x, y) for x, y in points]
    for _ in range(rng.randrange(QUARTER_TURNS)):
        points = [(-y, x) for x, y in points]
    triangle = points[:VERTICES]
    rng.shuffle(triangle)
    points = triangle + points[VERTICES:]
    assert inside(points)
    assert all(abs(value) <= MAX_COORDINATE for point in points for value in point)
    sys.stdout.write("".join(f"{x} {y}\n" for x, y in points))


if __name__ == "__main__":
    main()
