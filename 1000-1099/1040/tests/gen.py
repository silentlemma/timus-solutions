"""A random connected graph: a seed, N, M and the shape (random, path,
star, complete). A random spanning tree of the shape gets M - (N - 1)
more random edges; flights and their ends are listed in random order."""

import random
import sys


def main():
    seed, n, m = (int(x) for x in sys.argv[1:4])
    shape = sys.argv[4]
    rng = random.Random(seed)
    label = list(range(1, n + 1))
    rng.shuffle(label)
    edges = set()
    for v in range(1, n):
        if shape == "path":
            u = v - 1
        elif shape == "star":
            u = 0
        else:
            u = rng.randrange(v)
        edges.add((u, v))
    if shape == "complete":
        m = n * (n - 1) // 2
    m = min(m, n * (n - 1) // 2)
    while len(edges) < m:
        u, v = sorted(rng.sample(range(n), 2))
        edges.add((u, v))
    flights = []
    for u, v in edges:
        a, b = label[u], label[v]
        flights.append((a, b) if rng.randrange(2) else (b, a))
    rng.shuffle(flights)
    lines = ["%d %d" % (n, len(flights))] + ["%d %d" % f for f in flights]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
