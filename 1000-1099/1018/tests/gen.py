"""A random tree where every vertex has zero or two children (N odd), with
random apple counts; a seed, N, Q and the largest number of apples. The
vertices are numbered randomly with the root 1, the edges are shuffled."""

import random
import sys


def tree(rng, n):
    """Edges (parent, child) of a random full binary tree with n vertices."""
    edges, leaves, count = [], [0], 1
    while count < n:
        v = leaves.pop(rng.randrange(len(leaves)))
        for child in (count, count + 1):
            edges.append((v, child))
            leaves.append(child)
        count += 2
    return edges


def main():
    seed, n, q, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    label = [1] + rng.sample(range(2, n + 1), n - 1)
    lines = ["%d %d" % (n, q)]
    edges = tree(rng, n)
    rng.shuffle(edges)
    for a, b in edges:
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d %d" % (label[a], label[b], rng.randint(0, top)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
