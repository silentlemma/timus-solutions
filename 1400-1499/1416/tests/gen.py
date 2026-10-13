"""Galaxies of 500 planets: a seed and a mode. Mode 1 is the complete
graph with random costs, mode 2 a random tree with no second set,
mode 3 the complete graph with every cost 1000, mode 4 a random tree
plus 2000 more random links with costs from 0 to 3."""

import random
import sys

N = 500
TOP = 1000
EXTRA = 2000


def tree(rng):
    order = list(range(1, N + 1))
    rng.shuffle(order)
    return [(order[i], order[rng.randrange(i)]) for i in range(1, N)]


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (1, 3):
        pairs = [(a, b) for a in range(1, N + 1) for b in range(a + 1, N + 1)]
        edges = [(a, b, rng.randint(0, TOP) if mode == 1 else TOP) for a, b in pairs]
    elif mode == 2:
        edges = [(a, b, rng.randint(0, TOP)) for a, b in tree(rng)]
    else:
        seen = {tuple(sorted(e)) for e in tree(rng)}
        while len(seen) < N - 1 + EXTRA:
            a, b = rng.sample(range(1, N + 1), 2)
            seen.add((min(a, b), max(a, b)))
        edges = [(a, b, rng.randint(0, 3)) for a, b in seen]
    rng.shuffle(edges)
    lines = ["%d %d" % (N, len(edges))] + ["%d %d %d" % e for e in edges]
    print("\n".join(lines))


main()
