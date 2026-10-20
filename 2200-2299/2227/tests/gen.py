"""Print one valid polygon and operation sequence: python gen.py MODE SEED."""

import heapq
import math
import random
import sys

MIN_VERTICES = 4
MAX_VERTICES = 100_000
MAX_QUERIES = 100_000
COORD_LIMIT = 10**9
SMALL_POINTS = 40
SMALL_QUERIES = 100
MEDIUM_QUARTER = 250
MEDIUM_QUERIES = 1000
MIXED_PERIOD = 10
SMALL_MODE = 1
MEASURE_MODE = 2
CUT_MODE = 3
MEDIUM_MODE = 4
MIXED_MODE = 5
PREFIX_MODE = 6


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def turn(a, b, c):
    return cross((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))


def hull(points):
    points = sorted(set(points))
    lower = []
    for point in points:
        while len(lower) >= 2 and turn(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and turn(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def lattice_polygon(n, rng):
    quarter = n // MIN_VERTICES
    bound = math.isqrt(2 * quarter) + 2
    while True:
        directions = [
            (x, y) for x in range(1, bound + 1) for y in range(1, bound + 1) if math.gcd(x, y) == 1
        ]
        if len(directions) >= quarter:
            break
        bound *= 2
    directions.sort(key=lambda p: p[1] / p[0])
    directions = [directions[i * len(directions) // quarter] for i in range(quarter)]
    points = []
    x = y = 0
    for _ in range(MIN_VERTICES):
        for dx, dy in directions:
            points.append((x, y))
            x += dx
            y += dy
        directions = [(-dy, dx) for dx, dy in directions]
    center_x = (min(x for x, _ in points) + max(x for x, _ in points)) // 2
    center_y = (min(y for _, y in points) + max(y for _, y in points)) // 2
    points = [(x - center_x, y - center_y) for x, y in points]
    radius = max(max(abs(x), abs(y)) for x, y in points)
    scale = COORD_LIMIT // radius
    points = [(x * scale, y * scale) for x, y in points]
    offset = rng.randrange(n)
    return points[offset:] + points[:offset]


def diagonal(active, rng):
    size = len(active)
    left = rng.randrange(size)
    right = (left + rng.randrange(2, size - 1)) % size
    return sorted((left, right))


def random_operations(points, count, rng):
    active = list(range(len(points)))
    operations = []
    for step in range(count):
        left, right = diagonal(active, rng)
        a, b = active[left], active[right]
        kind = "m"
        if len(active) > MIN_VERTICES and rng.randrange(2) == 0 or step == count - 1:
            inside = active[left : right + 1]
            outside = active[right:] + active[: left + 1]
            part = sum(cross(points[u], points[v]) for u, v in zip(inside, inside[1:]))
            part += cross(points[b], points[a])
            other = sum(cross(points[u], points[v]) for u, v in zip(outside, outside[1:]))
            other += cross(points[a], points[b])
            keep = inside if part >= other else outside
            if len(keep) >= MIN_VERTICES or step == count - 1:
                active = sorted(keep)
                kind = "c"
        if rng.randrange(2):
            a, b = b, a
        operations.append((kind, a + 1, b + 1))
    return operations


def ear_operations(points, count, rng, mixed):
    n = len(points)
    previous = [(i - 1) % n for i in range(n)]
    following = [(i + 1) % n for i in range(n)]
    versions = [0] * n
    heap = []

    def push(i):
        versions[i] += 1
        area = turn(points[previous[i]], points[i], points[following[i]])
        heapq.heappush(heap, (area, rng.random(), i, versions[i]))

    for i in range(n):
        push(i)
    operations = []
    remaining = n
    for step in range(count):
        while True:
            _, _, tip, version = heap[0]
            if versions[tip] == version and following[tip] != tip:
                break
            heapq.heappop(heap)
        a, b = previous[tip], following[tip]
        kind = "m"
        if remaining > MIN_VERTICES and (not mixed or step % MIXED_PERIOD == 0):
            heapq.heappop(heap)
            kind = "c"
            following[a], previous[b] = b, a
            following[tip] = tip
            remaining -= 1
            push(a)
            push(b)
        elif mixed:
            while True:
                a, b = rng.randrange(n), rng.randrange(n)
                if a == b or following[a] == a or following[b] == b:
                    continue
                if following[a] != b and following[b] != a:
                    break
        if rng.randrange(2):
            a, b = b, a
        operations.append((kind, a + 1, b + 1))
    return operations


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL_MODE:
        while True:
            points = hull(
                [
                    (
                        rng.randint(-SMALL_POINTS, SMALL_POINTS),
                        rng.randint(-SMALL_POINTS, SMALL_POINTS),
                    )
                    for _ in range(SMALL_POINTS)
                ]
            )
            if len(points) >= MIN_VERTICES:
                break
        operations = random_operations(points, rng.randint(1, SMALL_QUERIES), rng)
    elif mode == MEDIUM_MODE:
        n = MIN_VERTICES * rng.randint(1, MEDIUM_QUARTER)
        points = lattice_polygon(n, rng)
        operations = random_operations(points, rng.randint(1, MEDIUM_QUERIES), rng)
    elif mode in (MEASURE_MODE, CUT_MODE, MIXED_MODE, PREFIX_MODE):
        points = lattice_polygon(MAX_VERTICES, rng)
        if mode in (CUT_MODE, MIXED_MODE):
            operations = ear_operations(points, MAX_QUERIES, rng, mode == MIXED_MODE)
        elif mode == MEASURE_MODE:
            active = list(range(MAX_VERTICES))
            operations = []
            for _ in range(MAX_QUERIES):
                a, b = diagonal(active, rng)
                if rng.randrange(2):
                    a, b = b, a
                operations.append(("m", a + 1, b + 1))
        else:
            # Dense low bits exercise long Fenwick prefix traversals.
            middle = 1 << (MAX_VERTICES.bit_length() - 1)
            a, b = middle - 1, middle + middle // 2 - 1
            operations = [("c", 1, 1 + 2)]
            operations += [("m", a + 1, b + 1)] * (MAX_QUERIES - 1)
    else:
        raise ValueError("mode must be between 1 and 6")
    lines = [f"{len(points)} {len(operations)}"]
    lines.extend(f"{x} {y}" for x, y in points)
    lines.extend(f"{kind} {a} {b}" for kind, a, b in operations)
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.stdout.write(generate(int(sys.argv[1]), int(sys.argv[2])))
