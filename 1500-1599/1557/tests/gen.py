"""One test from a seed and a mode: a connected network of servers with
shuffled channels. Mode 1 is a dense random network, mode 2 one long ring
with a few doubled channels, mode 3 a tree buried in self-loops, mode 4 a
chain of rings joined by single channels, mode 5 a small network."""

import random
import sys

SERVERS = 2000
CHANNELS = 100000
SMALL = 8
RING = 50


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 5 else SERVERS
    edges = []
    if mode == 2:
        edges = [(i, (i + 1) % n) for i in range(n)]
        edges += [edges[rng.randrange(n)] for _ in range(rng.randint(1, SMALL))]
    elif mode == 4:
        for start in range(0, n, RING):
            size = min(RING, n - start)
            edges += [(start + i, start + (i + 1) % size) for i in range(size)]
            if start:
                edges.append((rng.randrange(start), start + rng.randrange(size)))
            if rng.random() < 0.5:
                edges.append(edges[-1 - rng.randrange(size)])
    else:
        edges = [(rng.randrange(i), i) for i in range(1, n)]
        extra = CHANNELS - len(edges) if mode in (1, 3) else rng.randint(0, SMALL)
        for _ in range(extra):
            u = rng.randrange(n)
            edges.append((u, u if mode == 3 else rng.randrange(n)))
    perm = list(range(n))
    rng.shuffle(perm)
    rng.shuffle(edges)
    print(n, len(edges))
    for u, v in edges:
        if rng.random() < 0.5:
            u, v = v, u
        print(perm[u] + 1, perm[v] + 1)


main()
