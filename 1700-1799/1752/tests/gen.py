"""One test from a seed and a mode: mode 1 a random tree of up to 10
vertices with every query on it, mode 2 a random tree of 20000 vertices,
mode 3 a path of 20000 vertices, mode 4 a broom: a long handle with many
short bristles, mode 5 a star. Modes 2 to 5 ask 50000 random queries."""

import random
import sys

FEW = 10
MOST = 20000
QUERIES = 50000
SHORT = 0.9


def farthest(adj, start):
    depth = {start: 0}
    order = [start]
    for v in order:
        for u in adj[v]:
            if u not in depth:
                depth[u] = depth[v] + 1
                order.append(u)
    return order[-1], depth[order[-1]]


def diameter(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    end, _ = farthest(adj, 1)
    return farthest(adj, end)[1]


def tree(rng, n, mode):
    if mode == 3:
        parent = [0, 0] + [v - 1 for v in range(2, n + 1)]
    elif mode == 4:
        handle = n // 2
        parent = [0, 0] + [v - 1 if v <= handle else rng.randint(1, handle)
                           for v in range(2, n + 1)]
    elif mode == 5:
        parent = [0, 0] + [1] * (n - 1)
    else:
        parent = [0, 0] + [rng.randint(1, v - 1) for v in range(2, n + 1)]
    label = list(range(1, n + 1))
    rng.shuffle(label)
    label = [0] + label
    edges = [(label[v], label[parent[v]]) for v in range(2, n + 1)]
    rng.shuffle(edges)
    return edges


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 1 else MOST
    edges = tree(rng, n, mode)
    if mode == 1:
        queries = [(v, d) for v in range(1, n + 1) for d in range(n + 1)]
    else:
        # most distances are up to one past the diameter, the rest up to n
        top = diameter(n, edges) + 1
        queries = [(rng.randint(1, n), rng.randint(0, top if rng.random() < SHORT else n))
                   for _ in range(QUERIES)]
    lines = ["%d %d" % (n, len(queries))]
    lines += ["%d %d" % e for e in edges]
    lines += ["%d %d" % e for e in queries]
    sys.stdout.write("\n".join(lines) + "\n")


main()
