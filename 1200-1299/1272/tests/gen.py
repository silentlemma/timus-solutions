"""A city: a seed and a mode. Mode 1 draws random tunnels and bridges on
up to 10000 islands, mode 2 few tunnels and many islands (many bridges
needed), mode 3 the largest numbers with repeated and looping tunnels,
mode 4 maximum islands, tunnels and bridges with one tunnel-free island,
mode 5 maximum islands and bridges with no tunnels (maximum answer).
Bridges and tunnels together always connect every island."""

import random
import sys

ISLANDS = 10000
EDGES = 12000


def maximum_city(seed, mode):
    rng = random.Random(seed)
    n = ISLANDS
    tunnels = []
    if mode == 4:
        # A long tunnel chain leaves only island n disconnected by tunnels.
        tunnels = [(i, i + 1) for i in range(1, n - 1)]
        while len(tunnels) < EDGES:
            tunnels.append(tuple(rng.sample(range(1, n), 2)))
    order = list(range(1, n + 1))
    rng.shuffle(order)
    bridges = [(order[i], order[rng.randrange(i)]) for i in range(1, n)]
    while len(bridges) < EDGES:
        bridges.append(tuple(rng.sample(range(1, n + 1), 2)))
    rng.shuffle(bridges)
    out = ["%d %d %d" % (n, len(tunnels), len(bridges))]
    out += ["%d %d" % e for e in tunnels] + ["%d %d" % e for e in bridges]
    sys.stdout.write("\n".join(out) + "\n")


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (4, 5):
        maximum_city(seed, mode)
        return
    rng = random.Random(seed)
    n = ISLANDS if mode == 3 else rng.randint(1, ISLANDS)
    k = {1: rng.randint(0, EDGES), 2: rng.randint(0, n // 10), 3: EDGES}[mode]
    tunnels = []
    for _ in range(k):
        a = rng.randint(1, n)
        b = a if mode == 3 and rng.random() < 0.05 else rng.randint(1, n)
        tunnels.append((a, b))
    # a random spanning tree of bridges guarantees connectivity
    order = list(range(1, n + 1))
    rng.shuffle(order)
    bridges = [(order[i], order[rng.randrange(i)]) for i in range(1, n)]
    bridges = bridges[:EDGES]
    rng.shuffle(bridges)
    out = ["%d %d %d" % (n, k, len(bridges))]
    out += ["%d %d" % e for e in tunnels] + ["%d %d" % e for e in bridges]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
