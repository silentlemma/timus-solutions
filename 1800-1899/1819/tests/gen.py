"""One test from a seed and a mode: mode 1 a random graph, mode 2 a
wheel, mode 3 a ring of K4 blocks joined by single roads, mode 4 a
long path, mode 5 a random tree with extra roads, mode 6 many small
pieces. Half of the queries ask about nearby crossroads."""

import random
import sys

LIMIT = 50000
BLOCK = 4
WALK = 4
PIECE = 8


def random_graph(rng, n, k):
    roads = set()
    while len(roads) < k:
        a, b = rng.sample(range(1, n + 1), 2)
        roads.add((min(a, b), max(a, b)))
    return list(roads)


def blocks(count):
    roads = []
    for i in range(count):
        base = BLOCK * i
        for a in range(1, BLOCK + 1):
            for b in range(a + 1, BLOCK + 1):
                roads.append((base + a, base + b))
        nxt = BLOCK * ((i + 1) % count)
        roads.append((base + BLOCK, nxt + 1))
    return BLOCK * count, roads


def pieces(rng):
    roads, n = [], 0
    while True:
        size = rng.randint(2, PIECE)
        inner = random_graph(rng, size, rng.randint(1, size * (size - 1) // 2))
        if n + size > LIMIT or len(roads) + len(inner) > LIMIT:
            return n, roads
        roads += [(a + n, b + n) for a, b in inner]
        n += size


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, LIMIT)
        roads = random_graph(rng, n, rng.randint(1, min(LIMIT, n * (n - 1) // 2)))
    elif mode == 2:
        n = LIMIT // 2 + 1
        roads = [(1, v) for v in range(2, n + 1)]
        roads += [(v, v % (n - 1) + 2) for v in range(2, n + 1)]
    elif mode == 3:
        n, roads = blocks(LIMIT // (BLOCK * (BLOCK - 1) // 2 + 1))
    elif mode == 4:
        n = LIMIT
        roads = [(v, v + 1) for v in range(1, n)]
    elif mode == 5:
        n = LIMIT * 3 // 5
        roads = {(rng.randint(1, v - 1), v) for v in range(2, n + 1)}
        while len(roads) < LIMIT:
            a, b = rng.sample(range(1, n + 1), 2)
            roads.add((min(a, b), max(a, b)))
        roads = list(roads)
    else:
        n, roads = pieces(rng)
    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    roads = [(labels[a - 1], labels[b - 1]) for a, b in roads]
    rng.shuffle(roads)
    near = [[] for _ in range(n + 1)]
    for a, b in roads:
        near[a].append(b)
        near[b].append(a)
    queries = []
    while len(queries) < LIMIT:
        a = rng.randint(1, n)
        b = a
        if rng.random() < 0.5:
            for _ in range(rng.randint(1, WALK)):
                if near[b]:
                    b = rng.choice(near[b])
        if b == a:
            b = rng.randint(1, n)
        if b != a:
            queries.append((a, b))
    out = [f"{n} {len(roads)}"]
    out += [f"{a} {b}" for a, b in roads]
    out.append(str(len(queries)))
    out += [f"{a} {b}" for a, b in queries]
    print("\n".join(out))


main()
