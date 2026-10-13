"""One test from a seed and a mode. Mode 1 is a small random tree, mode 2 a
random tree of 50000 vertices, mode 3 a path of 50000 vertices with the
heaviest edges, asked first for its two ends, mode 4 a star, mode 5 a long
path with short branches, mode 6 a maximum-size all-zero binary tree,
and mode 7 a 64-vertex random Prufer tree with every ordered query pair.
Vertex names are shuffled. Modes 2 through 6 ask 75000 questions; mode 1
asks 200, and mode 7 asks 4096."""

import heapq
import random
import sys

LARGEST = 50000
QUESTIONS = 75000
SMALL = 30
SMALL_QUESTIONS = 200
HEAVIEST = 1000
BRANCH = 3  # in mode 5 every vertex hangs within this many steps back


def extra_case(rng, mode):
    n = LARGEST if mode == 6 else 64
    if mode == 6:
        edges = [((v - 1) // 2, v, 0) for v in range(1, n)]
        queries = [(rng.randrange(n), rng.randrange(n)) for _ in range(QUESTIONS)]
    else:
        code = [rng.randrange(n) for _ in range(n - 2)]
        degree = [1] * n
        for v in code:
            degree[v] += 1
        leaves = [v for v in range(n) if degree[v] == 1]
        heapq.heapify(leaves)
        edges = []
        for v in code:
            leaf = heapq.heappop(leaves)
            edges.append((leaf, v, rng.choice((0, 1, HEAVIEST - 1, HEAVIEST))))
            degree[v] -= 1
            if degree[v] == 1:
                heapq.heappush(leaves, v)
        a, b = leaves
        edges.append((a, b, rng.choice((0, 1, HEAVIEST - 1, HEAVIEST))))
        queries = [(a, b) for a in range(n) for b in range(n)]
        rng.shuffle(queries)
    names = list(range(n))
    rng.shuffle(names)
    rng.shuffle(edges)
    lines = [str(n)]
    for a, b, w in edges:
        a, b = names[a], names[b]
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d %d" % (a, b, w))
    lines.append(str(len(queries)))
    lines.extend("%d %d" % (names[a], names[b]) for a, b in queries)
    print("\n".join(lines))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7):
        extra_case(rng, mode)
        return
    n = rng.randint(1, SMALL) if mode == 1 else LARGEST
    m = SMALL_QUESTIONS if mode == 1 else QUESTIONS
    parents = []
    for v in range(1, n):
        if mode == 3:
            parents.append(v - 1)
        elif mode == 4:
            parents.append(0)
        elif mode == 5:
            parents.append(max(0, v - rng.randint(1, BRANCH)))
        else:
            parents.append(rng.randrange(v))
    names = list(range(n))
    rng.shuffle(names)
    lines = [str(n)]
    for v, p in zip(range(1, n), parents):
        w = HEAVIEST if mode == 3 else rng.randint(0, HEAVIEST)
        a, b = names[v], names[p]
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d %d" % (a, b, w))
    lines.append(str(m))
    for i in range(m):
        if mode == 3 and i == 0:
            lines.append("%d %d" % (names[0], names[n - 1]))  # the two ends
        else:
            lines.append("%d %d" % (rng.randrange(n), rng.randrange(n)))
    print("\n".join(lines))


main()
