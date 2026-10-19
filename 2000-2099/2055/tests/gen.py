"""Deterministic seed/family: tree, cycle, sparse_random, dense_random,
parallel_then_bridge, star_then_leaf_chain; maximal m and up to 50000 vertices.
"""

import random
import sys

MAX_VERTICES = 50000
MAX_WEIGHT = 10**9
SPARSE_VERTICES = MAX_VERTICES // 2
DENSE_VERTICES = 1000
BRIDGE_VERTICES = 3


def generate(seed, family):
    randomizer = random.Random(seed)
    limit = MAX_VERTICES
    tree = [(v, v - 1, randomizer.randrange(1, MAX_WEIGHT + 1)) for v in range(1, limit)]
    cases = {"tree": (limit, tree), "cycle": (limit, tree + [(0, limit - 1, MAX_WEIGHT)])}
    for n, name in ((SPARSE_VERTICES, "sparse_random"), (DENSE_VERTICES, "dense_random")):
        rows = [
            (v, randomizer.randrange(v), randomizer.randrange(1, MAX_WEIGHT + 1))
            for v in range(1, n)
        ]
        while len(rows) < limit:
            first, second = randomizer.sample(range(n), 2)
            rows.append((first, second, randomizer.randrange(1, MAX_WEIGHT + 1)))
        cases[name] = n, rows
    rows = [(0, 1, i + 1) for i in range(limit - 1)] + [(1, 2, MAX_WEIGHT)]
    cases["parallel_then_bridge"] = BRIDGE_VERTICES, rows
    rows = [(0, v, v) for v in range(1, SPARSE_VERTICES + 1)]
    rows += [(v, v + 1, SPARSE_VERTICES + v) for v in range(1, SPARSE_VERTICES)]
    rows.append((1, SPARSE_VERTICES, MAX_WEIGHT))
    cases["star_then_leaf_chain"] = SPARSE_VERTICES + 1, rows
    n, rows = cases[family]
    return f"{n} {len(rows)}\n" + "".join(f"{u + 1} {v + 1} {w}\n" for u, v, w in rows)


if __name__ == "__main__":
    sys.stdout.write(generate(int(sys.argv[1]), sys.argv[2]))
