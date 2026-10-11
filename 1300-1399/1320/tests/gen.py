"""A graph without loops and repeated edges: a seed and a mode. Mode 1
gives 1050 random edges over all 1000 vertices, mode 2 several
components with an even number of edges each, mode 3 one component with
1050 edges, mode 4 the same as mode 2 with two components made odd."""

import random
import sys

VERTICES = 1000
MOST = 1050


def component(rng, names, size):
    """Edges of a connected graph on the given vertices: a random tree and
    then random extra edges, size edges in all."""
    edges = {tuple(sorted((names[i], rng.choice(names[:i])))) for i in range(1, len(names))}
    while len(edges) < size:
        a, b = rng.sample(names, 2)
        edges.add((min(a, b), max(a, b)))
    return list(edges)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    names = list(range(1, VERTICES + 1))
    rng.shuffle(names)
    edges = []
    if mode == 1:
        edges = component(rng, names[:2], 1)
        while len(edges) < MOST:
            a, b = rng.sample(names, 2)
            if (min(a, b), max(a, b)) not in edges:
                edges.append((min(a, b), max(a, b)))
    elif mode == 3:
        edges = component(rng, names[:200], MOST)
    else:
        sizes = [2 * rng.randint(1, 20) for _ in range(20)]
        if mode == 4:
            sizes[0] -= 1
            sizes[1] += 1
        start = 0
        for size in sizes:
            fewest = 2  # enough vertices to hold size edges
            while fewest * (fewest - 1) // 2 < size:
                fewest += 1
            count = rng.randint(fewest, max(fewest, min(size + 1, 12)))
            edges += component(rng, names[start : start + count], size)
            start += count
    rng.shuffle(edges)
    for a, b in edges:
        if rng.random() < 0.5:
            a, b = b, a
        print(a, b)


main()
