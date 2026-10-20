"""Generate valid dense friendship graphs with python gen.py MODE SEED.

Modes: 1 small random, 2 medium random, 3 maximum random, 4 maximum bipartite,
5 maximum odd near-bipartite, 6 maximum complete, 7 even greedy trap,
8 odd greedy trap, 9 maximum degree-tight circulant. Seeds control all choices.
"""

import random
import sys

MAX_N = 1000
SMALL_MAX = 18
MEDIUM_MIN = 20
MEDIUM_MAX = 100
DENSITY_SCALE = 10
MAX_RANDOM = 3
BIPARTITE = 4
ODD_BIPARTITE = 5
COMPLETE = 6
EVEN_TRAP = 7
ODD_TRAP = 8
CIRCULANT = 9
ARGUMENT_COUNT = 3


def join(graph, first, second):
    graph[first][second] = 1
    graph[second][first] = 1


def repaired_random(n, rng):
    graph = [bytearray(n) for _ in range(n)]
    density = rng.randrange(1, DENSITY_SCALE)
    for first in range(n):
        for second in range(first):
            if rng.randrange(DENSITY_SCALE) < density:
                join(graph, first, second)
    minimum = (n + 1) // 2
    for first in range(n):
        missing = [second for second in range(n) if second != first and not graph[first][second]]
        rng.shuffle(missing)
        for second in missing[: max(0, minimum - sum(graph[first]))]:
            join(graph, first, second)
    return graph


def bipartite(n):
    graph = [bytearray(n) for _ in range(n)]
    middle = n // 2
    for first in range(middle):
        for second in range(middle, n):
            join(graph, first, second)
    if n % 2:
        # The larger part needs one extra friend per vertex.
        for vertex in range(middle, n, 2):
            join(graph, vertex, vertex + 1)
    return graph


def split_graph(n):
    graph = [bytearray(n) for _ in range(n)]
    middle = (n + 1) // 2
    for first in range(n):
        for second in range(first):
            if second < middle:
                join(graph, first, second)
    return graph


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == 1:
        graph = repaired_random(rng.randint(2, SMALL_MAX), rng)
    elif mode == 2:
        graph = repaired_random(rng.randint(MEDIUM_MIN, MEDIUM_MAX), rng)
    elif mode == MAX_RANDOM:
        graph = repaired_random(MAX_N, rng)
    elif mode == BIPARTITE:
        graph = bipartite(MAX_N)
    elif mode == ODD_BIPARTITE:
        graph = bipartite(MAX_N - 1)
    elif mode == COMPLETE:
        graph = [bytearray([1]) * MAX_N for _ in range(MAX_N)]
        for vertex in range(MAX_N):
            graph[vertex][vertex] = 0
    elif mode == EVEN_TRAP:
        return split_graph(MAX_N)
    elif mode == ODD_TRAP:
        return split_graph(MAX_N - 1)
    elif mode == CIRCULANT:
        n = MAX_N - seed % 2
        graph = [bytearray(n) for _ in range(n)]
        radius = ((n + 1) // 2 + 1) // 2
        for first in range(n):
            for distance in range(1, radius + 1):
                join(graph, first, (first + distance) % n)
    else:
        raise ValueError("unknown mode")
    order = list(range(len(graph)))
    rng.shuffle(order)
    return [bytearray(graph[first][second] for second in order) for first in order]


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    graph = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(len(graph))
    for row in graph:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
