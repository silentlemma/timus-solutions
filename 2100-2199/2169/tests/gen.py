"""Generate a simple graph: python gen.py MODE SEED. Modes 3-10 and 12 use maximum n.
1=random, 2=forest, 3=path, 4=cycle, 5=tree, 6=triangles, 7=crowns,
8=star, 9=bicyclic, 10=matching, 11=mixed, 12=empty."""

import random
import sys

LIMIT = 100_000
SMALL_SIZE = 18
SMALL_EDGES = 24
SMALL_TREE_SIZE = 80
BRANCHING = 3
MAX_DEGREE = 4
BLOCK_SIZE = 5
MIXED_SIZE = 12
MODE_COUNT = 12
(
    RANDOM,
    FOREST,
    PATH,
    CYCLE,
    TREE,
    TRIANGLES,
    CROWNS,
    STAR,
    MULTICYCLE,
    MATCHING,
    MIXED,
    EMPTY,
) = range(1, MODE_COUNT + 1)


def generate(mode, seed):
    rng = random.Random(seed)
    n, edges = LIMIT, []
    if mode == RANDOM:
        n = rng.randint(1, SMALL_SIZE)
        pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
        rng.shuffle(pairs)
        edges = pairs[: rng.randint(0, min(SMALL_EDGES, len(pairs)))]
    elif mode == FOREST:
        n = rng.randint(1, SMALL_TREE_SIZE)
        degree, available = [0] * n, [0]
        for vertex in range(1, n):
            if rng.randrange(BRANCHING):
                index = rng.randrange(len(available))
                parent = available[index]
                edges.append((parent, vertex))
                degree[parent] += 1
                degree[vertex] += 1
                if degree[parent] == MAX_DEGREE:
                    available.pop(index)
            available.append(vertex)
    elif mode == PATH:
        edges = [(vertex - 1, vertex) for vertex in range(1, n)]
    elif mode == CYCLE:
        edges = [(vertex, (vertex + 1) % n) for vertex in range(n)]
    elif mode == TREE:
        edges = [((vertex - 1) // BRANCHING, vertex) for vertex in range(1, n)]
    elif mode == TRIANGLES:
        for start in range(0, n - n % BRANCHING, BRANCHING):
            edges.extend([(start, start + 1), (start + 1, start + 2), (start + 2, start)])
    elif mode == CROWNS:
        for start in range(0, n, BLOCK_SIZE):
            edges.extend([(start, start + 1), (start + 1, start + 2), (start + 2, start)])
            edges.extend([(start, start + BRANCHING), (start, start + MAX_DEGREE)])
    elif mode == STAR:
        edges = [(0, vertex) for vertex in range(1, n)]
    elif mode == MULTICYCLE:
        core = n - 1
        edges = [(vertex, (vertex + 1) % core) for vertex in range(core)]
        edges.append((0, 2))
    elif mode == MATCHING:
        edges = [(vertex, vertex + 1) for vertex in range(0, n, 2)]
    elif mode == MIXED:
        n, start = rng.randint(1, SMALL_TREE_SIZE), 0
        while start < n:
            size = rng.randint(1, min(MIXED_SIZE, n - start))
            edges.extend((vertex - 1, vertex) for vertex in range(start + 1, start + size))
            if size >= BRANCHING and rng.randrange(2):
                edges.append((start, start + size - 1))
            start += size
    elif mode != EMPTY:
        raise ValueError("unknown mode")
    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    edges = [
        (labels[a], labels[b]) if rng.randrange(2) else (labels[b], labels[a]) for a, b in edges
    ]
    rng.shuffle(edges)
    return n, edges


def main():
    mode, seed = map(int, sys.argv[1:])
    n, edges = generate(mode, seed)
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{a} {b}" for a, b in edges)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
