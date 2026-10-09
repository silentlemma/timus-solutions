"""A random tree written as its code: a seed, N and the shape (0 any tree,
1 a path, 2 a few hubs with many leaves), with the vertices numbered at
random. The numbers go 20 to a line."""

import heapq
import random
import sys

PER_LINE = 20
ANY, PATH, HUBS = 0, 1, 2


def tree(rng, n, shape):
    order = list(range(1, n + 1))
    rng.shuffle(order)
    edges = []
    for i in range(1, n):
        if shape == PATH:
            parent = i - 1
        elif shape == HUBS:
            parent = rng.randrange(min(i, PER_LINE))
        else:
            parent = rng.randrange(i)
        edges.append((order[i], order[parent]))
    return edges


def encode(n, edges):
    adj = [set() for _ in range(n + 1)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    heap = [v for v in range(1, n + 1) if len(adj[v]) == 1]
    heapq.heapify(heap)
    code = []
    for _ in range(n - 1):
        leaf = heapq.heappop(heap)
        (u,) = adj[leaf]
        code.append(u)
        adj[u].discard(leaf)
        if len(adj[u]) == 1:
            heapq.heappush(heap, u)
    return code


def main():
    seed, n, shape = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    code = encode(n, tree(rng, n, shape))
    lines = [" ".join(map(str, code[i : i + PER_LINE])) for i in range(0, len(code), PER_LINE)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
