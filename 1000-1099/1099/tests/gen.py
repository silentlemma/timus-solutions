"""Random guards: a seed, N, the shape (0 random pairs, 1 an independent
set joined to a clique, 2 a chain of triangles) and the share of possible
pairs in percent for shape 0. Guards are numbered at random."""

import random
import sys

RANDOM, DEFICIENT, TRIANGLES = 0, 1, 2
PERCENT = 100
TRIANGLE = 3


def main():
    seed, n, shape, share = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    edges = []
    if shape == RANDOM:
        edges = [
            (a, b) for a in range(n) for b in range(a + 1, n) if rng.randrange(PERCENT) < share
        ]
    elif shape == DEFICIENT:
        clique = n // 3
        edges = [(a, b) for a in range(clique) for b in range(a + 1, n)]
    else:
        for i in range(0, n - TRIANGLE + 1, TRIANGLE):
            edges += [(i, i + 1), (i + 1, i + 2), (i, i + 2)]
            if i + TRIANGLE < n:
                edges.append((i + 2, i + TRIANGLE))
    label = list(range(1, n + 1))
    rng.shuffle(label)
    rng.shuffle(edges)
    lines = [str(n)] + [
        "%d %d" % (label[a], label[b]) if rng.random() < 0.5 else "%d %d" % (label[b], label[a])
        for a, b in edges
    ]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
