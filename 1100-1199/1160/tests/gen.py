"""A connected network: a seed, N, M and a mode. Modes 0-3 start with a
random spanning tree, then random extra pairs without repeats. Mode 0 draws lengths
up to 10^6, mode 1 makes all lengths equal, mode 2 draws them from 1 to 5,
mode 3 puts one bridge of the largest length that every plan needs,
mode 4 plants a length-1 spanning cycle among longer random chords."""

import random
import sys

TOP = 10**6
FEW = 5


def cycle_network(seed, n, m):
    rng = random.Random(seed)
    order = rng.sample(range(1, n + 1), n)
    pairs = set()
    edges = []

    def add(a, b, length):
        pair = tuple(sorted((a, b)))
        if a != b and pair not in pairs:
            pairs.add(pair)
            edges.append((a, b, length))

    for k in range(n):
        add(order[k], order[(k + 1) % n], 1)
    m = min(m, n * (n - 1) // 2)
    while len(edges) < m:
        add(rng.randint(1, n), rng.randint(1, n), rng.randint(2, TOP))
    rng.shuffle(edges)
    lines = ["%d %d" % (n, len(edges))] + ["%d %d %d" % e for e in edges]
    sys.stdout.write("\n".join(lines) + "\n")


def main():
    seed, n, m, mode = (int(x) for x in sys.argv[1:5])
    if mode == 4:
        cycle_network(seed, n, m)
        return
    rng = random.Random(seed)
    order = rng.sample(range(1, n + 1), n)
    pairs = set()
    edges = []

    def add(a, b):
        if a != b and (a, b) not in pairs:
            pairs.add((a, b))
            pairs.add((b, a))
            if mode == 1:
                length = TOP
            elif mode == 2:
                length = rng.randint(1, FEW)
            else:
                length = rng.randint(1, TOP - 1)
            edges.append([a, b, length])

    for k in range(1, n):
        add(order[k], order[rng.randrange(k)])
    if mode == 3:
        # the tree edge to the last hub is its only connection
        edges[-1][2] = TOP
    # every pair at most once; the last hub of mode 3 keeps its one cable
    free = n - 1 if mode == 3 else n
    m = min(m, free * (free - 1) // 2 + (n - free))
    while len(edges) < m:
        a, b = rng.randint(1, n), rng.randint(1, n)
        if mode == 3 and order[-1] in (a, b):
            continue
        add(a, b)
    rng.shuffle(edges)
    lines = ["%d %d" % (n, len(edges))] + ["%d %d %d" % tuple(e) for e in edges]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
