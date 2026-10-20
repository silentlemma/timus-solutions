import random
import sys

MAX_COUNT = 100_000
COORD_LIMIT = 10**9
MAX_DISTANCE = 2 * 2 * COORD_LIMIT
SMALL_COORD = 12
SMALL_COUNT = 40
GRID_RADIUS = 30
DIAGONAL_HALF = 300
MEDIUM_COUNT = 1_500
WIDE_COUNT = 1_200
QUERY_PERIOD = 5


def random_points(rng, count, bound):
    points = []
    seen = set()
    while len(points) < count:
        point = (rng.randint(-bound, bound), rng.randint(-bound, bound))
        if point not in seen:
            seen.add(point)
            points.append(point)
    return points


def random_queries(rng, points, count, bound, all_hits=False):
    queries = []
    for index in range(count):
        x = rng.randint(-bound, bound)
        y = rng.randint(-bound, bound)
        branch = index % QUERY_PERIOD
        if branch == 0:
            x, y = rng.choice(points)
            distance = 0
        elif all_hits or branch == 1:
            px, py = rng.choice(points)
            distance = abs(x - px) + abs(y - py)
        elif branch == 2:
            distance = MAX_DISTANCE
        else:
            distance = rng.randint(0, min(MAX_DISTANCE, 2 * 2 * bound))
        queries.append((x, y, distance))
    return queries


def generate(mode, rng):
    if mode == "small":
        count = rng.randint(1, SMALL_COUNT)
        points = random_points(rng, count, SMALL_COORD)
        queries = random_queries(rng, points, rng.randint(1, SMALL_COUNT), SMALL_COORD)
    elif mode == "grid":
        points = [
            (x, y)
            for x in range(-GRID_RADIUS, GRID_RADIUS + 1)
            for y in range(-GRID_RADIUS, GRID_RADIUS + 1)
        ]
        rng.shuffle(points)
        queries = random_queries(rng, points, MEDIUM_COUNT, 2 * GRID_RADIUS)
    elif mode == "diagonals":
        points = []
        seen = set()
        for x in range(-DIAGONAL_HALF, DIAGONAL_HALF + 1):
            for point in ((x, x), (x, -x), (x, x + 1)):
                if point not in seen:
                    seen.add(point)
                    points.append(point)
        rng.shuffle(points)
        queries = random_queries(rng, points, MEDIUM_COUNT, 2 * DIAGONAL_HALF)
    elif mode == "planted":
        points = random_points(rng, MEDIUM_COUNT, MAX_COUNT)
        queries = random_queries(rng, points, MEDIUM_COUNT, MAX_COUNT, all_hits=True)
    elif mode == "wide":
        points = random_points(rng, WIDE_COUNT, COORD_LIMIT)
        queries = random_queries(rng, points, WIDE_COUNT, COORD_LIMIT)
    elif mode == "max_diag":
        points = [(x, -x) for x in range(-MAX_COUNT // 2, MAX_COUNT // 2)]
        rng.shuffle(points)
        queries = []
        for _ in range(MAX_COUNT):
            radius = rng.randint(1, MAX_COUNT)
            queries.append((radius, radius, 2 * radius))
    elif mode in ("max_hits", "max_edges"):
        radius = MAX_COUNT // (2 * 2)
        points = []
        for offset in range(radius):
            points.extend(
                (
                    (offset, radius - offset),
                    (radius - offset, -offset),
                    (-offset, -radius + offset),
                    (-radius + offset, offset),
                )
            )
        rng.shuffle(points)
        if mode == "max_edges":
            queries = [(0, 0, radius)] * MAX_COUNT
        else:
            queries = []
            for index in range(MAX_COUNT):
                if index % 2 == 0:
                    queries.append((0, 0, radius))
                else:
                    x, y = rng.choice(points)
                    queries.append((x, y, 0))
    elif mode == "max_random":
        points = random_points(rng, MAX_COUNT, COORD_LIMIT)
        queries = random_queries(rng, points, MAX_COUNT, COORD_LIMIT, all_hits=True)
    else:
        raise SystemExit("unknown mode: " + mode)
    return points, queries


def main():
    mode, seed = sys.argv[1:]
    points, queries = generate(mode, random.Random(int(seed)))
    lines = [str(len(points))]
    lines.extend(f"{x} {y}" for x, y in points)
    lines.append(str(len(queries)))
    lines.extend(f"{x} {y} {distance}" for x, y, distance in queries)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
