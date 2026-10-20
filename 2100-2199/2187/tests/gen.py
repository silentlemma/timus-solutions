"""Generate simple undirected graphs with deterministic rewards and journey costs.

Modes 1 and 2 make small and medium random graphs. Modes 3 through 6 make
maximum sparse, star, cycle, and disconnected graphs. Modes 7 and 9 use a
long increasing-degree path; mode 8 adds a dense suffix, and mode 10 varies
the costs on a smaller increasing-degree path. Mode 11 combines a threshold
graph and a chain, then repairs degrees to make the chain strictly increasing.
"""

import random
import sys

MODE_TINY = 1
MODE_MEDIUM = 2
MODE_MAX_RANDOM = 3
MODE_STAR = 4
MODE_CYCLE = 5
MODE_DISCONNECTED = 6
MODE_LONG_PATH = 7
MODE_DENSE_SUFFIX = 8
MODE_LARGE_REWARDS = 9
MODE_COSTS = 10
MODE_THRESHOLD = 11
MAX_VERTICES = 100_000
MAX_EDGES = 100_000
MAX_COINS = 1_000_000_000
TINY_VERTICES = 9
TINY_EDGES = 18
TINY_COINS = 40
MEDIUM_MIN = 40
MEDIUM_MAX = 180
MEDIUM_DENSITY = 4
LONG_PATH_VERTICES = 446
PREFIX_VERTICES = 150
SUFFIX_VERTICES = 280
SHORT_PATH_MIN = 12
SHORT_PATH_MAX = 35
CHEAP_COST = 20
THRESHOLD_VERTICES = 628


def random_edges(rng, first, last, count, edges):
    used = set(edges)
    while len(edges) < count:
        left = rng.randint(first, last)
        right = rng.randint(first, last)
        if left > right:
            left, right = right, left
        if left != right and (left, right) not in used:
            used.add((left, right))
            edges.append((left, right))


def increasing_path(length):
    edges = [(vertex, vertex + 1) for vertex in range(1, length)]
    next_leaf = length + 1
    for vertex in range(2, length + 1):
        degree = 1 if vertex == length else 2
        for _ in range(vertex - degree):
            edges.append((vertex, next_leaf))
            next_leaf += 1
    return edges, next_leaf


def dense_suffix():
    core_size = PREFIX_VERTICES + SUFFIX_VERTICES
    edges = [(vertex, vertex + 1) for vertex in range(1, PREFIX_VERTICES)]
    edges.append((PREFIX_VERTICES, PREFIX_VERTICES + 1))
    for left in range(PREFIX_VERTICES + 1, core_size + 1):
        for right in range(left + 1, core_size + 1):
            edges.append((left, right))
    next_leaf = core_size + 1
    for vertex in range(2, core_size + 1):
        if vertex <= PREFIX_VERTICES:
            target = vertex
            degree = 2
        else:
            offset = vertex - PREFIX_VERTICES - 1
            target = SUFFIX_VERTICES + 1 + offset
            degree = SUFFIX_VERTICES - 1
            if offset == 0:
                degree += 1
        for _ in range(target - degree):
            edges.append((vertex, next_leaf))
            next_leaf += 1
    return edges, next_leaf


def threshold_path():
    edges = []
    for left in range(1, THRESHOLD_VERTICES + 1):
        for right in range(left + 1, THRESHOLD_VERTICES + 1):
            if left + right >= THRESHOLD_VERTICES + 1:
                edges.append((left, right))
    used = set(edges)
    for vertex in range(1, THRESHOLD_VERTICES):
        edge = (vertex, vertex + 1)
        if edge not in used:
            edges.append(edge)
    degree = [0] * (THRESHOLD_VERTICES + 1)
    for left, right in edges:
        degree[left] += 1
        degree[right] += 1
    next_leaf = THRESHOLD_VERTICES + 1
    previous = 0
    for vertex in range(1, THRESHOLD_VERTICES + 1):
        target = max(degree[vertex], previous + 1)
        for _ in range(target - degree[vertex]):
            edges.append((vertex, next_leaf))
            next_leaf += 1
        previous = target
    return edges, next_leaf


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == MODE_TINY:
        n = rng.randint(2, TINY_VERTICES)
        m = rng.randint(1, min(TINY_EDGES, n * (n - 1) // 2))
        a = [rng.randint(1, TINY_COINS) for _ in range(n)]
        b = [rng.randint(1, TINY_COINS) for _ in range(n - 1)]
        edges = []
        random_edges(rng, 1, n, m, edges)
    elif mode == MODE_MEDIUM:
        n = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        m = rng.randint(n // 2, MEDIUM_DENSITY * n)
        a = [rng.randint(1, MAX_COINS) for _ in range(n)]
        b = [rng.randint(1, MAX_COINS) for _ in range(n - 1)]
        edges = []
        random_edges(rng, 1, n, m, edges)
    elif mode in (MODE_MAX_RANDOM, MODE_DISCONNECTED):
        n = MAX_VERTICES
        a = [rng.randint(1, MAX_COINS) for _ in range(n)]
        b = [rng.randint(1, MAX_COINS) for _ in range(n - 1)]
        edges = []
        first = 2 if mode == MODE_DISCONNECTED else 1
        random_edges(rng, first, n, MAX_EDGES, edges)
    elif mode == MODE_STAR:
        n = MAX_VERTICES
        a = [MAX_COINS] * n
        b = [rng.randint(1, MAX_COINS) for _ in range(n - 1)]
        b[0] = 1
        edges = [(1, 2)]
        edges.extend((2, vertex) for vertex in range(2 + 1, n + 1))
    elif mode == MODE_CYCLE:
        n = MAX_VERTICES
        a = [MAX_COINS] * n
        b = [1] * (n - 1)
        edges = [(vertex, vertex + 1) for vertex in range(1, n)]
        edges.append((1, n))
    elif mode in (MODE_LONG_PATH, MODE_DENSE_SUFFIX, MODE_LARGE_REWARDS):
        n = MAX_VERTICES
        if mode == MODE_DENSE_SUFFIX:
            edges, next_leaf = dense_suffix()
        else:
            edges, next_leaf = increasing_path(LONG_PATH_VERTICES)
        random_edges(rng, next_leaf, n, MAX_EDGES, edges)
        a = [rng.randint(1, MAX_COINS) for _ in range(n)]
        b = [rng.randint(1, MAX_COINS) for _ in range(n - 1)]
        if mode == MODE_LARGE_REWARDS:
            a[:LONG_PATH_VERTICES] = [MAX_COINS] * LONG_PATH_VERTICES
            b[0] = 1
    elif mode == MODE_COSTS:
        length = rng.randint(SHORT_PATH_MIN, SHORT_PATH_MAX)
        edges, next_leaf = increasing_path(length)
        n = next_leaf - 1
        a = [rng.randint(1, TINY_COINS) for _ in range(n)]
        b = [rng.randint(1, CHEAP_COST) for _ in range(n - 1)]
        b[0] = MAX_COINS
        b[length - 2] = 1
    elif mode == MODE_THRESHOLD:
        n = MAX_VERTICES
        edges, next_leaf = threshold_path()
        random_edges(rng, next_leaf, n, MAX_EDGES, edges)
        a = [rng.randint(1, MAX_COINS) for _ in range(n)]
        b = [rng.randint(1, MAX_COINS) for _ in range(n - 1)]
    else:
        raise ValueError("unknown generator mode")
    rng.shuffle(edges)
    print(n, len(edges))
    print(*a)
    print(*b)
    sys.stdout.write("".join(f"{left} {right}\n" for left, right in edges))


if __name__ == "__main__":
    main()
