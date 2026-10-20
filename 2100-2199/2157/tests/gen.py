import random
import sys

MAX_CLOUDS = 50000
MAX_COORDINATE = 10000
MAX_HEIGHT = 10000
MAX_DENSITY = 10000
FALL_FACTOR = 5
SMALL_LIMIT = 30
SMALL_HEIGHT = 160
SMALL_SPAN = 12
LAYER_COUNT = 10
DENSE_RADIUS = 44
COLUMN_COUNT = 6
STAIR_RADIUS = 22
EXTREME_COLUMNS = 12
LOW_LAYERS = 3
PEAK_RADIUS = 3
PEAK_SPACING = 15
BOUNDARY_ATTEMPTS = 10000
ARGUMENT_COUNT = 3

MODE_SMALL = 1
MODE_BOUNDARY = 2
MODE_LAYERS = 3
MODE_CHAIN = 4
MODE_UNIFORM = 5
MODE_DENSE = 6
MODE_COLUMNS = 7
MODE_EQUAL = 8
MODE_STAIR = 9
MODE_EXTREME = 10
MODE_LOW = 11
MODE_PEAKS = 12
MODE_VERTICAL = 13


def random_clouds(rng, count, start_y, left, right):
    coordinates = set()
    while len(coordinates) < count:
        coordinates.add((rng.randint(left, right), rng.randrange(1, start_y)))
    return [(x, y, rng.randint(1, MAX_DENSITY)) for x, y in sorted(coordinates)]


def generate(mode, rng):
    start_x = rng.randint(-SMALL_LIMIT, SMALL_LIMIT)
    start_y = MAX_HEIGHT

    if mode == MODE_SMALL:
        start_y = rng.randint(1, SMALL_HEIGHT)
        capacity = (2 * SMALL_SPAN + 1) * (start_y - 1)
        count = rng.randint(0, min(SMALL_LIMIT, capacity))
        clouds = random_clouds(rng, count, start_y, start_x - SMALL_SPAN, start_x + SMALL_SPAN)
    elif mode == MODE_BOUNDARY:
        start_y = rng.randint(SMALL_LIMIT, SMALL_HEIGHT)
        count = rng.randint(1, SMALL_LIMIT)
        clouds = []
        coordinates = set()
        anchors = [(start_x, start_y)]
        for _ in range(BOUNDARY_ATTEMPTS):
            source_x, source_y = rng.choice(anchors)
            dx = rng.randint(-SMALL_SPAN, SMALL_SPAN)
            cloud_x = source_x + dx
            cloud_y = source_y - FALL_FACTOR * dx * dx + rng.randint(-1, 1)
            point = (cloud_x, cloud_y)
            if not 0 < cloud_y < start_y or point in coordinates:
                continue
            coordinates.add(point)
            anchors.append(point)
            clouds.append((cloud_x, cloud_y, rng.randint(1, MAX_DENSITY)))
            if len(clouds) == count:
                break
    elif mode == MODE_LAYERS:
        start_y = rng.randint(2, SMALL_HEIGHT)
        heights = rng.sample(range(1, start_y), min(LAYER_COUNT, start_y - 1))
        points = [
            (start_x + dx, cloud_y)
            for dx in range(-SMALL_SPAN, SMALL_SPAN + 1)
            for cloud_y in heights
        ]
        chosen = rng.sample(points, rng.randint(0, min(SMALL_LIMIT, len(points))))
        clouds = [(x, y, rng.randint(1, MAX_DENSITY)) for x, y in chosen]
    elif mode == MODE_CHAIN:
        start_y = rng.randint(2, MAX_HEIGHT)
        count = rng.randint(0, min(SMALL_LIMIT, start_y - 1))
        heights = sorted(rng.sample(range(1, start_y), count), reverse=True)
        clouds = []
        cloud_x, previous_y = start_x, start_y
        for cloud_y in heights:
            if previous_y - cloud_y >= FALL_FACTOR:
                cloud_x += rng.randint(-1, 1)
            clouds.append((cloud_x, cloud_y, rng.randint(1, MAX_DENSITY)))
            previous_y = cloud_y
    elif mode == MODE_UNIFORM:
        start_x = rng.randint(-MAX_COORDINATE, MAX_COORDINATE)
        clouds = random_clouds(rng, MAX_CLOUDS, start_y, -MAX_COORDINATE, MAX_COORDINATE)
    elif mode == MODE_DENSE:
        start_x = 0
        clouds = random_clouds(rng, MAX_CLOUDS, start_y, -DENSE_RADIUS, DENSE_RADIUS)
    elif mode == MODE_COLUMNS:
        start_x = 0
        positions = rng.sample(range(COLUMN_COUNT * (start_y - 1)), MAX_CLOUDS)
        clouds = [
            (position // (start_y - 1), position % (start_y - 1) + 1, MAX_DENSITY)
            for position in positions
        ]
    elif mode == MODE_EQUAL:
        start_x = rng.randint(-MAX_COORDINATE, MAX_COORDINATE)
        width = 2 * MAX_COORDINATE + 1
        positions = rng.sample(range(LOW_LAYERS * width), MAX_CLOUDS)
        clouds = [
            (
                position % width - MAX_COORDINATE,
                start_y - 1 - position // width,
                rng.randint(1, MAX_DENSITY),
            )
            for position in positions
        ]
    elif mode == MODE_STAIR:
        start_x = 0
        rows = (start_y - 2) // FALL_FACTOR + 1
        width = 2 * STAIR_RADIUS + 1
        positions = rng.sample(range(rows * width), MAX_CLOUDS)
        clouds = [
            (
                position % width - STAIR_RADIUS,
                start_y - 1 - FALL_FACTOR * (position // width),
                rng.choice((1, MAX_DENSITY)),
            )
            for position in positions
        ]
    elif mode == MODE_EXTREME:
        start_x = rng.choice((-MAX_COORDINATE, MAX_COORDINATE))
        positions = rng.sample(range(EXTREME_COLUMNS * (start_y - 1)), MAX_CLOUDS)
        clouds = []
        for position in positions:
            column = position // (start_y - 1)
            cloud_y = position % (start_y - 1) + 1
            if column < COLUMN_COUNT:
                cloud_x = -MAX_COORDINATE + column
            else:
                cloud_x = MAX_COORDINATE - (column - COLUMN_COUNT)
            density = MAX_DENSITY if cloud_x * start_x < 0 else 1
            clouds.append((cloud_x, cloud_y, density))
    elif mode == MODE_LOW:
        start_x = 0
        width = 2 * MAX_COORDINATE + 1
        positions = rng.sample(range(LOW_LAYERS * width), MAX_CLOUDS)
        clouds = [
            (
                position % width - MAX_COORDINATE,
                position // width + 1,
                rng.randint(1, MAX_DENSITY),
            )
            for position in positions
        ]
    elif mode == MODE_PEAKS:
        start_x = 0
        columns = 2 * PEAK_RADIUS + 1
        positions = rng.sample(range(columns * (start_y - 1)), MAX_CLOUDS)
        clouds = [
            (
                (position // (start_y - 1) - PEAK_RADIUS) * PEAK_SPACING,
                position % (start_y - 1) + 1,
                rng.randint(1, MAX_DENSITY),
            )
            for position in positions
        ]
    elif mode == MODE_VERTICAL:
        start_x = 0
        clouds = [(0, height, MAX_DENSITY) for height in range(1, start_y)]
    else:
        raise ValueError("unknown generator mode")

    rng.shuffle(clouds)
    return start_x, start_y, clouds


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = map(int, sys.argv[1:])
    start_x, start_y, clouds = generate(mode, random.Random(seed))
    lines = [str(len(clouds)), f"{start_x} {start_y}"]
    lines.extend(f"{x} {y} {density}" for x, y, density in clouds)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
