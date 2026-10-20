import math
import random
import sys


MAX_SIZE = 100000
MAX_COORD = 100000
SMALL_SIZE = 16
SMALL_COORD = 100
MEDIUM_MIN = 100
MEDIUM_SIZE = 2000
HIGH_MIN = 50000
CLUSTER_CENTER = 50000
CLUSTER_RADIUS = 25
AXIS_SIZE = 32
GRID_SIDE = 317


def random_points(rng, count, low, high, primitive=False, narrow=False):
    points = []
    seen = set()
    while len(points) < count:
        x = rng.randint(low, high)
        if narrow:
            y = rng.randint(CLUSTER_CENTER - CLUSTER_RADIUS, CLUSTER_CENTER + CLUSTER_RADIUS)
        else:
            y = rng.randint(low, high)
        point = (x, y)
        if point in seen or (primitive and math.gcd(x, y) != 1):
            continue
        seen.add(point)
        points.append(point)
    return points


def make_points(mode, rng):
    if mode == "small":
        count = rng.randint(2, SMALL_SIZE)
        return random_points(rng, count, -SMALL_COORD, SMALL_COORD)
    if mode == "medium":
        count = rng.randint(MEDIUM_MIN, MEDIUM_SIZE)
        return random_points(rng, count, -MAX_COORD, MAX_COORD)
    if mode == "max":
        return random_points(rng, MAX_SIZE, -MAX_COORD, MAX_COORD)
    if mode in ("positive", "ordered"):
        points = random_points(rng, MAX_SIZE, HIGH_MIN, MAX_COORD, primitive=True)
        if mode == "ordered":
            points.sort(key=lambda point: point[1] / point[0], reverse=True)
            shift = rng.randrange(MAX_SIZE)
            points = points[shift:] + points[:shift]
        return points
    if mode == "cluster":
        return random_points(rng, MAX_SIZE, HIGH_MIN, MAX_COORD, primitive=True, narrow=True)
    if mode == "line":
        height = rng.randint(1, MAX_COORD)
        points = [(x, height) for x in range(-HIGH_MIN, HIGH_MIN)]
    elif mode == "origin":
        points = random_points(rng, MEDIUM_SIZE, -MAX_COORD, MAX_COORD)
        if (0, 0) not in points:
            points[0] = (0, 0)
    elif mode == "rays":
        points = [(value, value) for value in range(-HIGH_MIN, HIGH_MIN + 1) if value]
    elif mode == "determinant":
        value = rng.randint(HIGH_MIN, MAX_COORD)
        points = [(value, value - 1), (1 - value, 2 - value)]
    elif mode == "axes":
        values = rng.sample(range(1, MAX_COORD + 1), AXIS_SIZE)
        points = [(value, 0) if value % 2 else (0, -value) for value in values]
    elif mode == "grid":
        points = [(index % GRID_SIDE + 1, index // GRID_SIDE + 1) for index in range(MAX_SIZE)]
    elif mode == "near_opposite":
        points = random_points(rng, MEDIUM_SIZE, HIGH_MIN, MAX_COORD, primitive=True)
        points.extend((-x, 1 - y) for x, y in points[:MEDIUM_MIN])
    else:
        raise SystemExit("unknown mode")
    rng.shuffle(points)
    return points


def main():
    mode = sys.argv[1]
    rng = random.Random(int(sys.argv[2]))
    points = make_points(mode, rng)
    lines = [str(len(points))]
    lines.extend(f"{x} {y}" for x, y in points)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
