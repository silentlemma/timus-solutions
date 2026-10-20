import random
import sys


MAX_SIZE = 100_000
MAX_LABEL = 1_000_000_000
ARGUMENT_COUNT = 3
TINY_SIZE = 32
TINY_LABEL = 8
SPARSE_MIN_SIZE = 50
SPARSE_MAX_SIZE = 600
BLOCK_MIN_SIZE = 100
BLOCK_MAX_SIZE = 3_000
BLOCK_VERTICES = 30
BLOCK_EDGES = 20
LONG_VERTICES = 20_000
DENSE_VERTICES = 317
THRESHOLD_VERTICES = 500


def unique_edges(vertices, count, rng):
    edges = []
    seen = set()
    while len(edges) < count:
        first = rng.randint(1, vertices)
        second = rng.randint(1, vertices)
        edge = (min(first, second), max(first, second))
        if first != second and edge not in seen:
            seen.add(edge)
            edges.append((first, second))
    return edges


def flatten_edges(edges):
    return [vertex for edge in edges for vertex in edge]


def make_tiny(rng):
    size = rng.randint(1, TINY_SIZE)
    return [rng.randint(0, TINY_LABEL) for _ in range(size)]


def make_sparse(rng):
    size = rng.randint(SPARSE_MIN_SIZE, SPARSE_MAX_SIZE)
    pool = [0, 1, 2, TINY_LABEL, MAX_LABEL, MAX_LABEL - 1]
    return [rng.choice(pool) if rng.randrange(2) else rng.randint(0, size) for _ in range(size)]


def make_blocks(rng):
    size = rng.randint(BLOCK_MIN_SIZE, BLOCK_MAX_SIZE)
    values = []
    while len(values) < size:
        vertices = rng.randint(2, BLOCK_VERTICES)
        capacity = vertices * (vertices - 1) // 2
        count = rng.randint(0, min(BLOCK_EDGES, capacity))
        edges = unique_edges(vertices, count, rng)
        values.extend([vertices, count])
        values.extend(flatten_edges(edges))
        if edges and rng.randrange(2):
            first, second = edges[-1]
            values.extend([vertices, 1, second, first])
        if rng.randrange(2):
            values.append(rng.randint(0, BLOCK_VERTICES))
    return values[:size]


def make_zeros(rng):
    pool = [0, 0, 1, 1, 2, 2, TINY_LABEL]
    return [rng.choice(pool) for _ in range(MAX_SIZE)]


def make_duplicates(rng):
    values = []
    while len(values) < MAX_SIZE:
        first = rng.randint(1, BLOCK_VERTICES)
        second = first % BLOCK_VERTICES + 1
        vertices = max(first, second)
        values.extend([vertices, 2, first, second, second, first])
        values.extend([vertices, 1, first, second])
        if rng.randrange(2):
            values.append(first)
    return values[:MAX_SIZE]


def make_long(rng):
    count = (MAX_SIZE - 2) // 2
    edges = unique_edges(LONG_VERTICES, count, rng)
    return [MAX_LABEL, count] + flatten_edges(edges)


def make_maxlabels(rng):
    pool = [0, 1, 2, MAX_LABEL, MAX_LABEL - 1, MAX_LABEL - 2]
    values = []
    while len(values) < MAX_SIZE:
        values.extend([MAX_LABEL, 1, MAX_LABEL, MAX_LABEL - 1])
        values.extend([MAX_LABEL - 1, 1, MAX_LABEL - 2, MAX_LABEL - 1])
        values.extend([rng.choice(pool), rng.choice(pool)])
        if rng.randrange(2):
            values.append(rng.choice(pool))
    return values[:MAX_SIZE]


def make_empty(rng):
    values = []
    for _ in range(MAX_SIZE // 2):
        values.extend([rng.randint(1, MAX_LABEL), 0])
    return values


def make_thresholds(rng):
    values = []
    while len(values) < MAX_SIZE:
        vertices = rng.randint(2, THRESHOLD_VERTICES)
        values.extend([vertices, 1, 1, vertices])
        values.extend([vertices, 1, vertices + 1, 1])
        values.extend([vertices, 1, 0, vertices])
        values.extend([vertices, 2, 1, vertices, vertices, 1])
        if rng.randrange(2):
            values.append(vertices)
    return values[:MAX_SIZE]


def make_dense(rng):
    count = (MAX_SIZE - 2) // 2
    edges = [
        (first, second)
        for first in range(1, DENSE_VERTICES + 1)
        for second in range(first + 1, DENSE_VERTICES + 1)
    ]
    rng.shuffle(edges)
    edges = edges[:count]
    edges = [(second, first) if rng.randrange(2) else (first, second) for first, second in edges]
    return [DENSE_VERTICES, count] + flatten_edges(edges)


GENERATORS = {
    "tiny": make_tiny,
    "sparse": make_sparse,
    "blocks": make_blocks,
    "zeros": make_zeros,
    "duplicates": make_duplicates,
    "long": make_long,
    "maxlabels": make_maxlabels,
    "empty": make_empty,
    "thresholds": make_thresholds,
    "dense": make_dense,
}


def main():
    if len(sys.argv) != ARGUMENT_COUNT or sys.argv[1] not in GENERATORS:
        raise SystemExit("usage: python gen.py MODE SEED")
    rng = random.Random(int(sys.argv[2]))
    values = GENERATORS[sys.argv[1]](rng)
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
