"""Usage: seed mode. At most 100000 vertices and exactly 100000 requests.
Modes: path_queries, path_updates, path_mixed, star_root, star_leafroot,
star_mixed, binary_mixed, random_sparse, random_mixed, singleton_empty,
singleton_queries. Includes empty output, maximum depth and high-degree copying.
"""

import random
import sys

LIMIT = 100_000
MAX_VALUE = 1_000_000_000
PREFIX = 50_000
FIBONACCI_STEPS = 70_000
ACTIVE_COUNT = 12


def make(seed, mode):
    rng = random.Random(seed)
    size = 1 if mode.startswith("singleton_") else LIMIT
    initial = [MAX_VALUE] * size
    if mode.startswith("path_"):
        edges = [(v - 1, v) for v in range(1, size)]
    elif mode.startswith("star_"):
        center = 0 if mode == "star_root" else size - 1 if mode == "star_leafroot" else size // 2
        edges = [(center, v) for v in range(size) if v != center]
    elif mode == "binary_mixed":
        edges = [((v - 1) // 2, v) for v in range(1, size)]
    elif mode.startswith("random_"):
        labels = list(range(size))
        rng.shuffle(labels)
        edges = [(labels[rng.randrange(v)], labels[v]) for v in range(1, size)]
    elif mode.startswith("singleton_"):
        edges = []
    else:
        raise ValueError("unknown mode")
    if mode == "path_queries":
        queries = [(2, v) for v in range(size)]
    elif mode == "path_updates":
        queries = [(1, v) for v in range(size)]
    elif mode == "star_root":
        queries = [(1, 0)] * PREFIX + [(2, v) for v in range(LIMIT - PREFIX)]
    elif mode == "star_leafroot":
        initial = [1] * size
        queries = [(1, size - 1 if i % 2 == 0 else 0) for i in range(FIBONACCI_STEPS)]
        queries += [(2, v) for v in range(LIMIT - FIBONACCI_STEPS - 1)] + [(2, size - 1)]
    elif mode == "singleton_empty":
        queries = [(1, 0)] * LIMIT
    elif mode == "singleton_queries":
        queries = [(1 if i % 2 == 0 else 2, 0) for i in range(LIMIT)]
    else:
        initial = [rng.choice((0, MAX_VALUE, rng.randrange(MAX_VALUE + 1))) for _ in range(size)]
        if mode in ("random_sparse", "star_mixed"):
            active = rng.sample(range(size), ACTIVE_COUNT)
            if mode == "star_mixed":
                active[0] = size // 2
            queries = [
                (1, rng.choice(active)) if rng.randrange(2) else (2, rng.randrange(size))
                for _ in range(LIMIT)
            ]
        else:
            queries = [(rng.randrange(1, 3), rng.randrange(size)) for _ in range(LIMIT)]
    rng.shuffle(edges)
    edges = [edge if rng.randrange(2) else edge[::-1] for edge in edges]
    return initial, edges, queries


def main():
    initial, edges, queries = make(int(sys.argv[1]), sys.argv[2])
    write = sys.stdout.write
    write(str(len(initial)) + "\n" + " ".join(map(str, initial)) + "\n")
    for a, b in edges:
        write(f"{a + 1} {b + 1}\n")
    write(str(len(queries)) + "\n")
    for kind, vertex in queries:
        write(f"{kind} {vertex + 1}\n")


if __name__ == "__main__":
    main()
