"""A random tree: a seed, n, the shape (random, path, caterpillar, deep) and
the start: a number, or "end" / "middle" for paths. Every airport has at
most 20 flights. Airports are renumbered at random."""

import random
import sys

MAX_DEGREE = 20


def main():
    seed, n = int(sys.argv[1]), int(sys.argv[2])
    shape, start = sys.argv[3], sys.argv[4]
    rng = random.Random(seed)
    degree = [0] * n
    edges = []
    for v in range(1, n):
        if shape == "path":
            u = v - 1
        elif shape == "caterpillar":
            u = v - 2 if v % 2 == 0 and v >= 2 else v - 1
        elif shape == "deep":
            u = rng.randrange(max(0, v - 3), v)
        else:
            u = rng.randrange(v)
        while degree[u] >= MAX_DEGREE:
            u = rng.randrange(v)
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))
    label = list(range(1, n + 1))
    rng.shuffle(label)
    if start == "end":
        k = label[0]
    elif start == "middle":
        k = label[n // 2]
    else:
        k = int(start)
    pairs = [(label[u], label[v]) if rng.randrange(2) else (label[v], label[u]) for u, v in edges]
    rng.shuffle(pairs)
    lines = ["%d %d" % (n, k)] + ["%d %d" % p for p in pairs]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
