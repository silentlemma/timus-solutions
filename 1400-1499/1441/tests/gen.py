"""A random connected simple graph: a seed, N, M and a mode. Mode 1 is a
random tree plus random extra edges, mode 2 a long cycle with chords
between rooms of the cycle, mode 3 a star plus extra edges. Rooms are
shuffled and so are the tunnels."""

import random
import sys


def main():
    seed, n, m, mode = (int(a) for a in sys.argv[1:5])
    rng = random.Random(seed)
    edges = set()

    def add(a, b):
        if a != b and (b, a) not in edges:
            edges.add((a, b))

    if mode == 1:
        for v in range(2, n + 1):
            add(v, rng.randint(1, v - 1))
    elif mode == 2:
        for v in range(1, n + 1):
            add(v, v % n + 1)
    else:
        for v in range(2, n + 1):
            add(1, v)
    while len(edges) < m:
        add(rng.randint(1, n), rng.randint(1, n))
    names = list(range(1, n + 1))
    rng.shuffle(names)
    lines = ["%d %d" % (n, m)]
    order = list(edges)
    rng.shuffle(order)
    for a, b in order:
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d" % (names[a - 1], names[b - 1]))
    print("\n".join(lines))


main()
