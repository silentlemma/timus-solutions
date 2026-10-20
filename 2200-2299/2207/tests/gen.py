"""Print a deterministic valid board: python gen.py MODE SEED."""

import random
import sys

MAX_COUNT = 10_000
MAX_VALUE = 10**9
SMALL_COUNT = 20
MEDIUM_COUNT = 300
SMALL_SIDE = 10
SMALL_AMOUNT = 10
GRID_WIDTH = 200
CLUSTER_SIDE = 1000
CLUSTERS = 10
HIERARCHY_BASE = 3


def generate(mode, seed):
    rng = random.Random(seed)
    width = height = MAX_VALUE
    if mode in ("small", "balanced", "people", "jobs"):
        n, m = (rng.randint(1, SMALL_COUNT) for _ in range(2))
        width = height = SMALL_SIDE
    elif mode == "medium":
        n, m = (rng.randint(1, MEDIUM_COUNT) for _ in range(2))
    elif mode in ("max_random", "line", "grid", "clusters", "separated", "hierarchy"):
        n = m = MAX_COUNT
    elif mode == "one_house":
        n, m = 1, MAX_COUNT
    elif mode == "one_farm":
        n, m = MAX_COUNT, 1
    else:
        raise SystemExit("unknown mode")

    count = n + m
    if mode == "hierarchy":
        positions = [1]
        for i in range(1, count):
            level = (i & -i).bit_length() - 1
            positions.append(positions[-1] + HIERARCHY_BASE**level)
        points = [(v, v) for v in positions]
        points = points[::2] + points[1::2]
    elif mode == "line":
        width = 1
        points = [(1, 1 + i * ((MAX_VALUE - 1) // count)) for i in range(count)]
    elif mode == "grid":
        width, height = GRID_WIDTH, count // GRID_WIDTH
        points = [(i % width + 1, i // width + 1) for i in range(count)]
    elif mode == "separated":
        points = [(i + 1, 1) for i in range(n)]
        points += [(MAX_VALUE - i, MAX_VALUE) for i in range(m)]
    else:
        points = []
        used = set()
        while len(points) < count:
            if mode == "clusters":
                cluster = rng.randrange(CLUSTERS)
                base = cluster * (MAX_VALUE // CLUSTERS)
                point = (base + rng.randint(1, CLUSTER_SIDE), rng.randint(1, CLUSTER_SIDE))
            else:
                point = (rng.randint(1, width), rng.randint(1, height))
            if point not in used:
                used.add(point)
                points.append(point)
    if mode not in ("separated", "hierarchy"):
        rng.shuffle(points)
    limit = SMALL_AMOUNT if mode in ("small", "balanced", "people", "jobs") else MAX_VALUE
    amounts = [rng.randint(1, limit) for _ in range(count)]
    if mode == "balanced":
        amounts = [m] * n + [n] * m
    elif mode == "people":
        amounts = [MAX_VALUE] * n + [1] * m
    elif mode == "jobs":
        amounts = [1] * n + [MAX_VALUE] * m
    elif mode in ("grid", "line", "separated", "hierarchy"):
        amounts = [MAX_VALUE] * count
    return width, height, n, m, [(*p, a) for p, a in zip(points, amounts)]


def main():
    width, height, n, m, buildings = generate(sys.argv[1], int(sys.argv[2]))
    print(width, height)
    print(n, m)
    for building in buildings:
        print(*building)


if __name__ == "__main__":
    main()
