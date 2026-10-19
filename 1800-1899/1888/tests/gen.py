"""Flights from a seed and a mode: mode 1 a few pilots at random, 2 the
most pilots and flights on a random bipartite graph, 3 a long path with
extra flights between its two sides, 4 two or more separate groups,
5 a bipartite graph with one odd cycle added. Every pilot flies at least
once."""

import random
import sys

MOST_FLIGHTS = 1000
MOST_PILOTS = 50
FEW = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    p = rng.randint(2, FEW) if mode == 1 else rng.randint(MOST_PILOTS // 2, MOST_PILOTS)
    side = [rng.randint(0, 1) for _ in range(p + 1)]
    order = list(range(1, p + 1))
    rng.shuffle(order)
    edges = set()
    if mode == 1:
        for _ in range(rng.randint(1, FEW * 2)):
            a, b = rng.sample(range(1, p + 1), 2)
            edges.add((a, b))
    else:
        groups = [order]
        if mode == 4:
            cut = rng.randint(2, p - 2)
            groups = [order[:cut], order[cut:]]
        for group in groups:
            # a spanning path keeps the group connected
            for a, b in zip(group, group[1:]):
                edges.add((a, b))
                side[b] = 1 - side[a]
            if mode == 3:
                continue
            extra = MOST_FLIGHTS // len(groups) - len(group)
            for _ in range(extra):
                a, b = rng.sample(group, 2) if len(group) > 1 else (group[0], group[0])
                if a != b and side[a] != side[b]:
                    edges.add((a, b))
        if mode == 3:
            path = order
            for _ in range(rng.randint(0, FEW)):
                i, j = sorted(rng.sample(range(p), 2))
                if (j - i) % 2:
                    edges.add((path[i], path[j]))
        if mode == 5:
            a, b = rng.sample(order, 2)
            while side[a] != side[b]:
                a, b = rng.sample(order, 2)
            edges.add((a, b))
    seen = {x for e in edges for x in e}
    for x in range(1, p + 1):
        if x not in seen:
            y = rng.choice([z for z in range(1, p + 1) if side[z] != side[x]] or [x % p + 1])
            edges.add((x, y))
    flights = list(edges)
    while len(flights) < MOST_FLIGHTS and mode != 1 and rng.random() < 0.5:
        flights.append(rng.choice(list(edges)))
    flights = flights[:MOST_FLIGHTS]
    rng.shuffle(flights)
    print(len(flights), p)
    print("\n".join("%d %d" % (a, b) if rng.random() < 0.5 else "%d %d" % (b, a) for a, b in flights))


main()
