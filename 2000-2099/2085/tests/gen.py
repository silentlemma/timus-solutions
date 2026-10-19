"""A tree of projects with technologies from a seed.

Mode 1: a few projects, random sets. Mode 2: a few projects with a planted
path that covers every technology once. Mode 3: 10^5 projects with a planted
path. Mode 4: 10^5 projects in a line with a planted path. Mode 5: 10^5
projects with random sets, so most likely no plan.
Mode 6: a maximum balanced tree with globally unique technologies and no path.
Mode 7: ten full projects, reaching the one-million membership limit.
Mode 8: a maximum line with two technology blocks, empty corridors and guards.
Mode 9: 120 random projects with 30 technologies and sets of size zero to five.
"""

import random
import sys

SMALL_N = 8
SMALL_M = 5
MAX = 10 ** 5
NOISE = 3  # technologies of a project off the planted path


def tree(rng, n, line):
    return [(v, v - 1 if line else rng.randrange(v)) for v in range(1, n)]


def extra(mode, rng):
    if mode == 6:
        n = m = MAX
        labels = list(range(n))
        rng.shuffle(labels)
        edges = [(labels[v], labels[(v - 1) // 2]) for v in range(1, n)]
        technologies = list(range(1, m + 1))
        rng.shuffle(technologies)
        sets = [[t] for t in technologies]
    elif mode == 7:
        n, m = 10, MAX
        edges = tree(rng, n, False)
        technologies = list(range(1, m + 1))
        rng.shuffle(technologies)
        sets = [technologies] * n
    elif mode == 8:
        n = m = MAX
        edges = tree(rng, n, True)
        sets = [[] for _ in range(n)]
        sets[n // 3] = list(range(1, m + 1, 2))
        sets[2 * n // 3] = list(range(2, m + 1, 2))
        rng.shuffle(sets[n // 3])
        rng.shuffle(sets[2 * n // 3])
        sets[0], sets[-1] = [1], [2]
    elif mode == 9:
        n, m = 120, 30
        edges = tree(rng, n, False)
        sets = [rng.sample(range(1, m + 1), rng.randrange(6)) for _ in range(n)]
    else:
        raise ValueError("unknown mode")
    rng.shuffle(edges)
    print(n, m)
    for u, v in edges:
        print(u + 1, v + 1)
    for s in sets:
        print(len(s), *s)


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode >= 6:
        extra(mode, rng)
        return
    small = mode <= 2
    n = rng.randint(1, SMALL_N) if small else MAX
    m = rng.randint(1, SMALL_M) if small else MAX
    edges = tree(rng, n, mode == 4)
    sets = [rng.sample(range(1, m + 1), rng.randint(0, min(m, NOISE))) for _ in range(n)]
    if mode in (2, 3, 4):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # walk a random simple path and share all technologies along it
        path, seen = [rng.randrange(n)], set()
        seen.add(path[0])
        while True:
            options = [u for u in adj[path[-1]] if u not in seen]
            if not options or rng.random() < 1 / max(2, len(path) // 2 + 1) and small:
                break
            path.append(rng.choice(options))
            seen.add(path[-1])
        for v in path:
            sets[v] = []
        for t in range(1, m + 1):
            sets[rng.choice(path)].append(t)
    rng.shuffle(edges)
    print(n, m)
    for u, v in edges:
        print(u + 1, v + 1)
    for s in sets:
        print(len(s), *s)


main()
