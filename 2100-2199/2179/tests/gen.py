import random
import sys

MIN_POINTS = 2
MAX_POINTS = 100_000
COORD_LIMIT = 1_000_000_000
SMALL_RANDOM = 1
SMALL_LINE = 2
SMALL_GRID = 3
SMALL_RECTANGLE = 4
SMALL_PRECISION = 5
LARGE_RANDOM = 6
LARGE_LINE = 7
LARGE_GRID = 8
LARGE_PERIMETER = 9
LARGE_CONVEX = 10
LARGE_THIN = 11
LARGE_COLUMNS = 12
SMALL_WIDE = 13
TINY_LIMIT = 12
TINY_SIZE = 35
SMALL_SIZE = 200
GRID_SIZE = 300
GRID_SIDE = 20
RECTANGLE_SIDE = 14
LINE_SPAN = 50_000
LINE_ORIGIN = 100_000_000
PRECISION_RADIUS = 9
PRECISION_SIZE = 100
PRECISION_SCALE = 50_000_000
LARGE_GRID_WIDTH = 400
LARGE_GRID_HEIGHT = 250
LENS_RADIUS = 25_000
COLUMN_COUNT = 3
ARGUMENT_COUNT = 3


def random_points(rng, count, limit):
    points = []
    seen = set()
    while len(points) < count:
        point = (rng.randint(-limit, limit), rng.randint(-limit, limit))
        if point not in seen:
            points.append(point)
            seen.add(point)
    return points


def make_points(mode, rng):
    if mode == SMALL_RANDOM:
        count = rng.randint(MIN_POINTS, TINY_SIZE)
        return random_points(rng, count, TINY_LIMIT)

    if mode == SMALL_LINE:
        count = rng.randint(MIN_POINTS, SMALL_SIZE)
        dx = dy = 0
        while dx == 0 and dy == 0:
            dx = rng.randint(-10, 10)
            dy = rng.randint(-10, 10)
        origin_x = rng.randint(-LINE_ORIGIN, LINE_ORIGIN)
        origin_y = rng.randint(-LINE_ORIGIN, LINE_ORIGIN)
        offsets = rng.sample(range(-LINE_SPAN, LINE_SPAN + 1), count)
        return [(origin_x + dx * step, origin_y + dy * step) for step in offsets]

    if mode == SMALL_GRID:
        width = rng.randint(2, GRID_SIDE)
        height = rng.randint(2, GRID_SIDE)
        grid = [(x, y) for x in range(width) for y in range(height)]
        count = rng.randint(MIN_POINTS, min(GRID_SIZE, len(grid)))
        return rng.sample(grid, count)

    if mode == SMALL_RECTANGLE:
        width = rng.randint(2, RECTANGLE_SIDE)
        height = rng.randint(2, RECTANGLE_SIDE)
        boundary = []
        interior = []
        for x in range(width + 1):
            for y in range(height + 1):
                target = boundary if x in (0, width) or y in (0, height) else interior
                target.append((x, y))
        count = rng.randint(0, len(interior))
        return boundary + rng.sample(interior, count)

    if mode == SMALL_PRECISION:
        grid = [
            (x, y)
            for x in range(-PRECISION_RADIUS, PRECISION_RADIUS + 1)
            for y in range(-PRECISION_RADIUS, PRECISION_RADIUS + 1)
        ]
        count = rng.randint(MIN_POINTS, PRECISION_SIZE)
        scale = PRECISION_SCALE
        # This integer map has determinant one, despite its large coefficients.
        return [
            (scale * x + (scale - 1) * y, (scale + 1) * x + scale * y)
            for x, y in rng.sample(grid, count)
        ]

    if mode == LARGE_RANDOM:
        return random_points(rng, MAX_POINTS, COORD_LIMIT)

    if mode == LARGE_LINE:
        step = COORD_LIMIT // MAX_POINTS
        offset = COORD_LIMIT // 2
        return [(index * step - offset, offset - index * step) for index in range(MAX_POINTS)]

    if mode == LARGE_GRID:
        return [(x, y) for x in range(LARGE_GRID_WIDTH) for y in range(LARGE_GRID_HEIGHT)]

    if mode == LARGE_PERIMETER:
        side = MAX_POINTS // (2 * 2)
        scale = COORD_LIMIT // side
        points = []
        for index in range(side):
            points.extend(
                [
                    (index * scale, 0),
                    (COORD_LIMIT, index * scale),
                    (COORD_LIMIT - index * scale, COORD_LIMIT),
                    (0, COORD_LIMIT - index * scale),
                ]
            )
        return points

    if mode == LARGE_CONVEX:
        height = LENS_RADIUS * LENS_RADIUS
        lower = [(x, x * x - height) for x in range(-LENS_RADIUS, LENS_RADIUS)]
        upper = [(x, height - x * x) for x in range(-LENS_RADIUS + 1, LENS_RADIUS + 1)]
        return lower + upper

    if mode == LARGE_THIN:
        step = COORD_LIMIT // MAX_POINTS
        offset = COORD_LIMIT // 2
        points = []
        for index in range(MAX_POINTS):
            x = index * step - offset
            points.append((x, x + rng.choice((-1, 0, 1))))
        return points

    if mode == LARGE_COLUMNS:
        rows = (MAX_POINTS + COLUMN_COUNT - 1) // COLUMN_COUNT
        step = 2 * COORD_LIMIT // (rows - 1)
        return [
            ((index % COLUMN_COUNT - 1) * COORD_LIMIT, index // COLUMN_COUNT * step - COORD_LIMIT)
            for index in range(MAX_POINTS)
        ]

    if mode == SMALL_WIDE:
        count = rng.randint(MIN_POINTS, SMALL_SIZE)
        return random_points(rng, count, COORD_LIMIT)

    raise SystemExit("unknown generator mode")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = int(sys.argv[1])
    seed = int(sys.argv[2])
    rng = random.Random(seed)
    points = make_points(mode, rng)
    rng.shuffle(points)
    lines = [str(len(points))]
    lines.extend(f"{x} {y}" for x, y in points)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
