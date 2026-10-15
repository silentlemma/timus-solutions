"""One test from a seed and a mode: mode 1 a union of small paths and
cliques with an occasional defect, mode 2 a small random graph, mode 3 the
largest sizes (a long path, cliques, or a dense random graph)."""

import random
import sys

MOST_BALLS = 100
MOST_RODS = 10000


def pieces(rng, n):
    """paths and cliques of up to five vertices covering 0..n-1"""
    order = list(range(n))
    rng.shuffle(order)
    edges = set()
    pos = 0
    while pos < n:
        kind = rng.choice(["path", "clique", "cycle", "star"])
        k = min(n - pos, rng.randint(1, 5) if kind != "path" else rng.randint(1, n))
        part = order[pos : pos + k]
        pos += k
        if kind == "path":
            edges |= {(part[i], part[i + 1]) for i in range(k - 1)}
        elif kind == "clique":
            edges |= {(part[i], part[j]) for i in range(k) for j in range(i + 1, k)}
        elif kind == "cycle" and k >= 3:
            edges |= {(part[i], part[(i + 1) % k]) for i in range(k)}
        else:
            edges |= {(part[0], part[i]) for i in range(1, k)}
    return edges


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, 15)
        edges = pieces(rng, n)
        if rng.random() < 0.3 and n >= 2:
            u, v = rng.sample(range(n), 2)
            edges.add((u, v))
    elif mode == 2:
        n = rng.randint(1, 7)
        pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
        edges = {p for p in pairs if rng.random() < rng.random()}
    else:
        n = MOST_BALLS
        style = seed % 3
        if style == 0:
            edges = {(i, i + 1) for i in range(n - 1)}
        elif style == 1:
            edges = set()
            for base in range(0, n, 4):
                part = range(base, min(base + 4, n))
                edges |= {(a, b) for a in part for b in part if a < b}
        else:
            pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
            edges = set(rng.sample(pairs, min(MOST_RODS, len(pairs))))
    edges = {(min(e), max(e)) for e in edges}
    edges = {tuple(rng.sample(e, 2)) for e in edges}
    lines = ["%d %d" % (n, len(edges))]
    lines += ["%d %d" % (u + 1, v + 1) for u, v in sorted(edges, key=lambda e: rng.random())]
    print("\n".join(lines))


main()
