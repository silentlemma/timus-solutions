"""Forest from "MODE SEED": mode 1 a small acyclic graph with a few days,
mode 2 10^5 random edges with a planted route, mode 3 a long chain with
shortcuts and days near the best ratio, mode 4 glades numbered beyond N
and extreme counts, mode 5 maximum-width two-edge routes and 10^5 days,
mode 6 a dense random DAG with source and target inside its topological order."""

import random
import sys

MAX_N = 10 ** 5
MAX_V = 10 ** 9
SMALL_N = 7
SMALL_V = 6
CHAIN_V = 1000
PATH = 30
SPREAD = 4


def build(n, m, rng, top, labels=None):
    rank = list(range(1, n + 1))
    rng.shuffle(rank)
    rank.remove(1)
    rank.remove(n)
    rank = [1] + rank + [n]
    if labels:
        rank = [labels.get(v, v) for v in rank]
    pairs = set()
    if len(rank) > PATH:
        path = [0] + sorted(rng.sample(range(1, len(rank) - 1), PATH)) + [len(rank) - 1]
        pairs.update((rank[i], rank[j]) for i, j in zip(path, path[1:]))
    while len(pairs) < m:
        i, j = sorted(rng.sample(range(len(rank)), 2))
        pairs.add((rank[i], rank[j]))
    return [(u, v, rng.randint(1, top), rng.randint(1, top)) for u, v in pairs]


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, SMALL_N)
        m = rng.randint(1, n * (n - 1) // 2)
        edges = build(n, m, rng, SMALL_V)
        days = [(rng.randint(1, SMALL_V), rng.randint(1, SMALL_V)) for _ in range(SMALL_N)]
    elif mode == 2:
        n = MAX_N
        edges = build(n, MAX_N, rng, MAX_V)
        days = [(MAX_V, max(1, int(MAX_V * rng.random() ** SPREAD))) for _ in range(MAX_N)]
    elif mode == 3:
        n = MAX_N
        edges = [(v, v + 1, rng.randint(CHAIN_V, 2 * CHAIN_V), CHAIN_V) for v in range(1, n)]
        while len(edges) < MAX_N:
            u = rng.randint(1, n - 2)
            v = rng.randint(u + 2, min(n, u + CHAIN_V))
            edges.append((u, v, rng.randint(CHAIN_V, 2 * CHAIN_V), CHAIN_V))
        edges = list({(u, v): (u, v, s, w) for u, v, s, w in edges}.values())
        days = [(CHAIN_V, rng.randint(1, 2 * CHAIN_V)) for _ in range(MAX_N)]
    elif mode == 4:
        n = MAX_N // 2
        labels = {v: v + MAX_N // 2 for v in range(2, n) if v % 2 == 0}
        edges = build(n, MAX_N, rng, MAX_V, labels)
        edges = [(u, v, MAX_V, rng.choice([1, MAX_V])) for u, v, _, _ in edges]
        days = [(rng.choice([1, MAX_V]), rng.choice([1, MAX_V])) for _ in range(MAX_N)]
    elif mode == 5:
        n = MAX_N
        edges = []
        for v in range(2, MAX_N // 2 + 2):
            edges.append((1, v, rng.randint(1, MAX_V - 2), MAX_V))
            edges.append((v, n, rng.randint(1, MAX_V - 2), MAX_V))
        # One best branch; all other branches have a strictly smaller ratio.
        edges[-2] = (1, MAX_N // 2 + 1, MAX_V - 1, MAX_V)
        edges[-1] = (MAX_N // 2 + 1, n, MAX_V, MAX_V)
        prices = [(1, 1), (MAX_V, MAX_V - 1), (MAX_V - 1, MAX_V - 2),
                  (MAX_V, 1), (1, MAX_V), (MAX_V, MAX_V - 2)]
        days = [prices[i % len(prices)] for i in range(MAX_N)]
    elif mode == 6:
        n = 40
        rank = list(range(2, n))
        rng.shuffle(rank)
        rank.insert(8, 1)
        rank.insert(30, n)
        edges = [(u, v, rng.randint(1, 30), rng.randint(1, 30))
                 for i, u in enumerate(rank) for v in rank[i + 1:]
                 if rng.random() < 0.6]
        days = [(rng.randint(1, 30), rng.randint(1, 30)) for _ in range(80)]
        days += [(w, s) for _, _, s, w in rng.sample(edges, 20)]
    else:
        raise ValueError('mode must be between 1 and 6')
    rng.shuffle(edges)
    print(n, len(edges), len(days))
    for e in edges:
        print(*e)
    for a, b in days:
        print(a, b)


main()
