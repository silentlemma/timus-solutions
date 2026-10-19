"""Usage: seed mode. Relabeled simple connected maximum graph families.
Modes: path_forced, path_remote, cycle_avoid, cycle_forced, branch_outside,
star, dense, diamonds. Distinct terminals; at most 100000 vertices and edges.
"""

import random
import sys
from itertools import combinations

LIMIT = 100000
LAYERS = 25000
DENSE_VERTICES = 448


def make(mode):
    n = LIMIT
    if mode.startswith("path") or mode.startswith("cycle"):
        edges = [[v - 1, v] for v in range(1, n)]
        if mode.startswith("cycle"):
            edges.append([n - 1, 0])
        if mode == "path_remote":
            return n, edges, n - 3, n - 2, 0, n - 3
        if mode == "cycle_avoid":
            return n, edges, 0, n // 2, n // 4, n // 4
        if mode == "cycle_forced":
            return n, edges, 0, n // 2 - 1, n // 4, 0
        return n, edges, 0, n - 1, n // 2, 0
    if mode == "branch_outside":
        edges = [[v - 1, v] for v in range(1, n - 1)] + [[n // 2 - 1, n - 1]]
        return n, edges, 0, n - 2, n - 1, 1
    if mode == "star":
        return n, [[0, v] for v in range(1, n)], 1, 2, 3, 1
    if mode == "dense":
        n = DENSE_VERTICES
        edges = [list(edge) for edge in combinations(range(n), 2)][:LIMIT]
        return n, edges, 0, 1, 2, 1
    if mode == "diamonds":
        n = 2 * LAYERS + 2
        edges = [[0, 1], [0, 2]]
        for layer in range(1, LAYERS):
            for a in (2 * layer - 1, 2 * layer):
                for b in (2 * layer + 1, 2 * layer + 2):
                    edges.append([a, b])
        edges.extend([[n - 3, n - 1], [n - 2, n - 1]])
        return n, edges, 0, n - 1, 1 + 2 * (LAYERS // 2), 1
    raise ValueError(mode)


def main():
    rng = random.Random(int(sys.argv[1]))
    size, edges, start, finish, origin, _ = make(sys.argv[2])
    labels = list(range(size))
    rng.shuffle(labels)
    rng.shuffle(edges)
    write = sys.stdout.write
    write(f"{size} {len(edges)}\n")
    for a, b in edges:
        if rng.randrange(2):
            a, b = b, a
        write(f"{labels[a] + 1} {labels[b] + 1}\n")
    write(f"{labels[start] + 1} {labels[finish] + 1} {labels[origin] + 1}\n")


if __name__ == "__main__":
    main()
