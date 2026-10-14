"""One test from a seed and a mode. Every station but N gets a pipe towards
N along a random tree, more random pipes are added, and the flow is the sum
of random walks from random stations that end in N, so it is valid. Mode 1
is large with half the pipes full, mode 2 has no flow at all, so no well
and no answer, mode 3 is large with every pipe full and costly except a
few free ones, mode 4 is small, mode 5 is a chain of 10000 full pipes with
the largest cost each. Mode 6 has exactly 100000 pipes at 10000 stations:
full circulations share ten costly exits to N. Mode 7 is a medium
random network with overlapping circulation cycles and well-to-N paths."""

import random
import sys

STATIONS = 10000
PIPES = 100000
WALKS = 3000
STEPS = 60
MOST = 10000
PRICE = 1000000
SMALL = 6


def circulation(rng, mode):
    n = STATIONS if mode == 6 else rng.randint(30, 60)
    pipes = {}
    if mode == 6:
        # Each offset gives equal inflow and outflow at every non-sink
        # station; the ten exits create exactly ten wells.
        for u in range(1, n):
            for offset in range(1, 11):
                v = (u - 1 + offset) % (n - 1) + 1
                pipes[u, v] = MOST
        for u in rng.sample(range(1, n), 10):
            pipes[u, n] = MOST
    else:
        def walk(vertices):
            for u, v in zip(vertices, vertices[1:]):
                pipes[u, v] = pipes.get((u, v), 0) + 1

        for _ in range(100):
            cycle = rng.sample(range(1, n), rng.randint(2, 8))
            walk(cycle + cycle[:1])
        for _ in range(10):
            walk(rng.sample(range(1, n), rng.randint(2, 12)) + [n])
        for _ in range(100):
            u, v = rng.randint(1, n - 1), rng.randint(1, n)
            if u != v:
                pipes.setdefault((u, v), 0)
    rows = [[] for _ in range(n)]
    for (u, v), flow in pipes.items():
        if mode == 6:
            cap = flow
            price = rng.randint(1, PRICE) if v == n else PRICE
        else:
            cap = flow + (rng.randint(1, 3) if rng.random() < 0.15 else 0)
            price = rng.randint(0, PRICE)
        rows[u - 1].append(f"{v} {cap} {flow} {price}")
    print(n)
    for row in rows:
        print(", ".join(row) + ".")


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7):
        circulation(rng, mode)
        return
    n = rng.randint(2, SMALL) if mode == 4 else STATIONS
    pipes = {}  # (from, to) -> flow
    if mode == 5:
        for i in range(1, n):
            pipes[(i, i + 1)] = 1
    else:
        order = list(range(1, n))
        rng.shuffle(order)
        order.append(n)
        parent = {}
        for k in range(n - 1):
            parent[order[k]] = order[rng.randint(k + 1, n - 1)]
            pipes[(order[k], parent[order[k]])] = 0
        extra = rng.randint(0, n) if mode == 4 else PIPES - len(pipes)
        for _ in range(extra):
            a, b = rng.randint(1, n - 1), rng.randint(1, n)
            if a != b:
                pipes.setdefault((a, b), 0)
        leaving = {}
        for a, b in pipes:
            leaving.setdefault(a, []).append(b)
        walks = 0 if mode == 2 else (rng.randint(0, SMALL) if mode == 4 else WALKS)
        for _ in range(walks):
            v = rng.randint(1, n - 1)
            used = []
            for _ in range(STEPS):
                if v == n:
                    break
                w = parent[v] if rng.random() < 0.5 else rng.choice(leaving[v])
                used.append((v, w))
                v = w
            if v == n and all(pipes[p] < MOST for p in used):
                for p in used:
                    pipes[p] += 1
    lines = [[] for _ in range(n + 1)]
    for (a, b), c in pipes.items():
        if mode == 5:
            cap, price = c, PRICE
        elif mode == 3:
            free = rng.random() < 0.01
            cap, price = c, (0 if free else rng.randint(PRICE // 2, PRICE))
        else:
            cap = c if rng.random() < 0.5 else min(MOST, c + rng.randint(0, SMALL))
            price = rng.randint(0, PRICE if mode != 4 else SMALL)
        lines[a].append("%d %d %d %d" % (b, cap, c, price))
    print(n)
    for a in range(1, n + 1):
        print(", ".join(lines[a]) + ".")


main()
