import math
import random
import sys

MIN_VERTICES = 3
MAX_VERTICES = 200
COORD_LIMIT = 100_000_000
ARG_COUNT = 3
MODE_SMALL = 1
MODE_MEDIUM = 2
MODE_MAXIMUM = 3
MODE_THIN = 4
MODE_ASYMMETRIC = 5
SMALL_POINT_MIN = 3
SMALL_POINT_MAX = 30
SMALL_COORD_LIMIT = 20
MEDIUM_VERTEX_MIN = 20
MEDIUM_VERTEX_MAX = 80
CIRCLE_RADIUS = 1_000_000
CIRCLE_JITTER = 0.2
CIRCLE_SCALE_MAX = 50
PARABOLA_LIMIT = 1_000
THIN_SCALE_MIN = 10_000
THIN_SCALE_MAX = 50_000
ASYMMETRIC_POINT_COUNT = 100
ASYMMETRIC_COORD_LIMIT = 10_000
ASYMMETRIC_TIP = 80_000
ASYMMETRIC_X_SCALE_MAX = 1_000
ASYMMETRIC_Y_SCALE_MAX = 5_000
QUARTER_TURNS = 4


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


def circle(count, rng):
    step = 2 * math.pi / count
    points = []
    for index in range(count):
        angle = step * (index + rng.uniform(-CIRCLE_JITTER, CIRCLE_JITTER))
        points.append(
            (round(CIRCLE_RADIUS * math.cos(angle)), round(CIRCLE_RADIUS * math.sin(angle)))
        )
    return points


def transform(points, x_scale, y_scale, rng):
    points = [(x * x_scale, y * y_scale) for x, y in points]
    for _ in range(rng.randrange(QUARTER_TURNS)):
        points = [(-y, x) for x, y in points]
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)
    shift_x = rng.randint(-COORD_LIMIT - min_x, COORD_LIMIT - max_x)
    shift_y = rng.randint(-COORD_LIMIT - min_y, COORD_LIMIT - max_y)
    points = [(x + shift_x, y + shift_y) for x, y in points]
    start = rng.randrange(len(points))
    return points[start:] + points[:start]


def generate(mode, rng):
    if mode == MODE_SMALL:
        while True:
            points = hull(
                [
                    (
                        rng.randint(-SMALL_COORD_LIMIT, SMALL_COORD_LIMIT),
                        rng.randint(-SMALL_COORD_LIMIT, SMALL_COORD_LIMIT),
                    )
                    for _ in range(rng.randint(SMALL_POINT_MIN, SMALL_POINT_MAX))
                ]
            )
            if len(points) >= MIN_VERTICES:
                return transform(points, 1, 1, rng)
    if mode in (MODE_MEDIUM, MODE_MAXIMUM):
        count = MAX_VERTICES
        if mode == MODE_MEDIUM:
            count = rng.randint(MEDIUM_VERTEX_MIN, MEDIUM_VERTEX_MAX)
        return transform(
            circle(count, rng),
            rng.randint(1, CIRCLE_SCALE_MAX),
            rng.randint(1, CIRCLE_SCALE_MAX),
            rng,
        )
    if mode == MODE_THIN:
        positions = sorted(rng.sample(range(-PARABOLA_LIMIT, PARABOLA_LIMIT + 1), MAX_VERTICES))
        points = [(x, x * x) for x in positions]
        return transform(points, rng.randint(THIN_SCALE_MIN, THIN_SCALE_MAX), 1, rng)
    if mode == MODE_ASYMMETRIC:
        points = [
            (
                rng.randint(-ASYMMETRIC_COORD_LIMIT, ASYMMETRIC_COORD_LIMIT),
                rng.randint(-ASYMMETRIC_COORD_LIMIT, ASYMMETRIC_COORD_LIMIT),
            )
            for _ in range(ASYMMETRIC_POINT_COUNT)
        ]
        points.extend(
            [
                (-ASYMMETRIC_COORD_LIMIT, -ASYMMETRIC_COORD_LIMIT),
                (-ASYMMETRIC_COORD_LIMIT, ASYMMETRIC_COORD_LIMIT),
                (ASYMMETRIC_TIP, 0),
            ]
        )
        return transform(
            hull(points),
            rng.randint(1, ASYMMETRIC_X_SCALE_MAX),
            rng.randint(1, ASYMMETRIC_Y_SCALE_MAX),
            rng,
        )
    raise ValueError("unknown generator mode")


def validate(points):
    assert MIN_VERTICES <= len(points) <= MAX_VERTICES
    assert len(set(points)) == len(points)
    assert all(abs(x) <= COORD_LIMIT and abs(y) <= COORD_LIMIT for x, y in points)
    for index in range(len(points)):
        a = points[index]
        b = points[(index + 1) % len(points)]
        for offset in range(2, len(points)):
            assert cross(a, b, points[(index + offset) % len(points)]) > 0


def main():
    if len(sys.argv) != ARG_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    points = generate(int(sys.argv[1]), random.Random(int(sys.argv[2])))
    validate(points)
    print(len(points))
    for x, y in points:
        print(x, y)


if __name__ == "__main__":
    main()
