import random
import sys


MAX_VERTICES = 100000
MAX_REQUESTS = 100000
MAX_COST = 1000000000
SMALL_VERTICES = 30
MEDIUM_VERTICES = 1000
DENSE_VERTICES = 317
BLOCK_SIZE = 4
THRESHOLD_SCALE = 100
ARGUMENT_COUNT = 3


def costs(rng, seed):
    regimes = (
        (1, MAX_COST),
        (MAX_COST, 1),
        (MAX_COST, MAX_COST),
        (MAX_COST - 1, MAX_COST),
        (THRESHOLD_SCALE, THRESHOLD_SCALE * 2),
        (THRESHOLD_SCALE, THRESHOLD_SCALE * 2 - 1),
        (THRESHOLD_SCALE, THRESHOLD_SCALE * 2 + 1),
        (rng.randint(1, MAX_COST), rng.randint(1, MAX_COST)),
    )
    return regimes[seed % len(regimes)]


def random_requests(rng, vertex_count, request_count):
    width = vertex_count - 1
    codes = rng.sample(range(vertex_count * width), request_count)
    edges = []
    for code in codes:
        source, target = divmod(code, width)
        target += target >= source
        edges.append((source, target))
    return edges


def dag_requests(rng, vertex_count, request_count):
    edges = set()
    while len(edges) < request_count:
        source, target = rng.sample(range(vertex_count), 2)
        edges.add((min(source, target), max(source, target)))
    return sorted(edges)


def block_requests(rng, vertex_count):
    edges = []
    previous = None
    first = 0
    while first < vertex_count:
        size = rng.randint(1, min(BLOCK_SIZE, vertex_count - first))
        if size > 1:
            for offset in range(size):
                edges.append((first + offset, first + (offset + 1) % size))
        if previous is not None and rng.randrange(2):
            edges.append((previous, first))
        previous = first
        first += size
    return edges or [(0, 1)]


def generate(mode, seed):
    rng = random.Random(seed)
    one_way, two_way = costs(rng, seed)
    if mode in ("tiny", "random", "maxrandom", "dense"):
        if mode == "tiny":
            vertex_count = rng.randint(2, SMALL_VERTICES)
        elif mode == "random":
            vertex_count = rng.randint(2, MEDIUM_VERTICES)
        elif mode == "dense":
            vertex_count = DENSE_VERTICES
        else:
            vertex_count = MAX_VERTICES
        capacity = min(MAX_REQUESTS, vertex_count * (vertex_count - 1))
        request_count = rng.randint(1, capacity)
        if mode in ("maxrandom", "dense"):
            request_count = MAX_REQUESTS
        edges = random_requests(rng, vertex_count, request_count)
    elif mode == "dag":
        vertex_count = rng.randint(2, SMALL_VERTICES)
        capacity = vertex_count * (vertex_count - 1) // 2
        edges = dag_requests(rng, vertex_count, rng.randint(1, capacity))
    elif mode in ("blocks", "sccmix"):
        limit = SMALL_VERTICES if mode == "blocks" else MEDIUM_VERTICES
        vertex_count = rng.randint(2, limit)
        edges = block_requests(rng, vertex_count)
    elif mode == "sccchain":
        vertex_count = MAX_VERTICES
        active = vertex_count // 2
        edges = set()
        for first in range(0, active, 2):
            edges.add((first, first + 1))
            edges.add((first + 1, first))
            if first:
                edges.add((first - 1, first))
        while len(edges) < MAX_REQUESTS:
            left, right = sorted(rng.sample(range(active // 2), 2))
            edges.add((left * 2 + rng.randrange(2), right * 2 + rng.randrange(2)))
        edges = sorted(edges)
    elif mode == "pairs":
        vertex_count = MAX_VERTICES
        edges = []
        for first in range(0, vertex_count, 2):
            edges.extend(((first, first + 1), (first + 1, first)))
    elif mode in ("chain", "cycle", "maxdag"):
        vertex_count = MAX_VERTICES
        edges = [(vertex, vertex + 1) for vertex in range(vertex_count - 1)]
        if mode == "cycle":
            edges.append((vertex_count - 1, 0))
        elif mode == "maxdag":
            edges.append((0, vertex_count - 1))
    elif mode in ("outstar", "instar"):
        vertex_count = MAX_VERTICES
        edges = [(0, vertex) for vertex in range(1, vertex_count)]
        edges.append((1, 2))
        if mode == "instar":
            edges = [(target, source) for source, target in edges]
    elif mode == "sparse":
        vertex_count = MAX_VERTICES
        edges = [(0, vertex_count - 1)]
    elif mode == "threshold":
        vertex_count = BLOCK_SIZE + 1
        edges = [(0, 1), (1, 2), (2, 0), (2, BLOCK_SIZE - 1)]
        edges.append((BLOCK_SIZE - 1, BLOCK_SIZE))
        one_way = THRESHOLD_SCALE * 2
        two_way = one_way * (vertex_count - 2) // 2 + seed % (BLOCK_SIZE - 1) - 1
    elif mode == "twolevels":
        vertex_count = SMALL_VERTICES
        middle = vertex_count // 2
        edges = [(left, right) for left in range(middle) for right in range(middle, vertex_count)]
    else:
        raise SystemExit("unknown mode")

    labels = list(range(1, vertex_count + 1))
    rng.shuffle(labels)
    rng.shuffle(edges)
    lines = [f"{vertex_count} {len(edges)} {one_way} {two_way}"]
    lines.extend(f"{labels[source]} {labels[target]}" for source, target in edges)
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    sys.stdout.write(generate(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
