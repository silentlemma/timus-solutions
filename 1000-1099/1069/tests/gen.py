"""Usage: gen.py SEED N SHAPE. Modes: 0 random recursive tree, 1 path,
2 up to twenty hubs with many leaves, 3 star, 4 balanced binary tree
(all with randomly numbered vertices), 5 uniform random extended Pruefer
code ending in N. The numbers go 20 to a line.
"""

import heapq
import random
import sys

PER_LINE = 20
ANY, PATH, HUBS = 0, 1, 2
STAR, BINARY, UNIFORM_CODE = 3, 4, 5


def tree(rng, n, shape):
    order = list(range(1, n + 1))
    rng.shuffle(order)
    edges = []
    for i in range(1, n):
        if shape == PATH:
            parent = i - 1
        elif shape == HUBS:
            parent = rng.randrange(min(i, PER_LINE))
        elif shape == STAR:
            parent = 0
        elif shape == BINARY:
            parent = (i - 1) // 2
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
    if shape == UNIFORM_CODE:
        code = [rng.randint(1, n) for _ in range(n - 2)] + [n]
    else:
        code = encode(n, tree(rng, n, shape))
    lines = [" ".join(map(str, code[i : i + PER_LINE])) for i in range(0, len(code), PER_LINE)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
