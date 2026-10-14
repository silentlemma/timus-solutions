"""One cactus from a seed and a mode, written as edge-disjoint paths. The
cactus grows from vertex 1: each new piece hangs from an existing vertex
and is either a single edge or a cycle. Mode 1 has 50000 vertices of
mixed pieces, mode 2 one huge cycle, mode 3 a long path, mode 4 many
triangles and squares on one vertex, mode 5 a small cactus (at most 12
edges), mode 6 a deep chain of cycles."""

import random
import sys

MOST = 50000
SMALL_EDGES = 12


def grow(rng, n, cycle_chance, longest, chain=False):
    """Edges of a random cactus with n vertices: (edges, list of cycles)."""
    paths = []
    count = 1
    while count < n:
        at = count if chain else rng.randint(1, count)
        room = n - count
        if rng.random() < cycle_chance and room >= 2:
            size = rng.randint(2, min(longest, room))  # new vertices on the cycle
            new = list(range(count + 1, count + size + 1))
            paths.append([at] + new + [at])
            count += size
        else:
            paths.append([at, count + 1])
            count += 1
    return paths


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, paths = MOST, grow(rng, MOST, 0.3, 8)
    elif mode == 2:
        n = MOST
        paths = [list(range(1, n + 1)) + [1]]
    elif mode == 3:
        n = MOST
        paths = [list(range(1, n + 1))]
    elif mode == 4:
        n = MOST - 1
        paths = []
        v = 2
        while v + 2 <= n:
            size = rng.choice([2, 3])
            if v + size - 1 > n:
                break
            paths.append([1] + list(range(v, v + size)) + [1])
            v += size
        n = v - 1
    elif mode == 5:
        while True:
            n = rng.randint(2, 9)
            paths = grow(rng, n, 0.5, 4)
            if sum(len(p) - 1 for p in paths) <= SMALL_EDGES:
                break
    else:
        n, paths = MOST, grow(rng, MOST, 0.9, 5, chain=True)
    # relabel at random, choose a root and shuffle the paths
    label = list(range(1, n + 1))
    rng.shuffle(label)
    paths = [[label[v - 1] for v in p] for p in paths]
    rng.shuffle(paths)
    root = label[0] if mode != 5 else rng.randint(1, n)
    print(n, len(paths), root)
    for p in paths:
        if rng.random() < 0.5:
            p = p[::-1]
        print(len(p), *p)


main()
