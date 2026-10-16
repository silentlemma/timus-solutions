"""One kingdom from a seed and a mode: mode 1 a small random tree, mode
2 the largest random tree, mode 3 a broom (a long chain ending in a
wide fan), mode 4 a wide king with small households, mode 5 a deep
chain. Labels are shuffled so suzerains may have larger numbers."""

import random
import sys

LIMIT = 10000
DAYS = 100
SMALL = 12


def king_ready(n, parent, days, share):
    days = days[:]
    days[1] = 0
    kids = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        kids[parent[v]].append(v)
    ready = [0] * (n + 1)
    for v in range(n, 0, -1):
        times = sorted(ready[w] for w in kids[v])
        need = -(-share * len(times) // 100)
        ready[v] = days[v] + (times[need - 1] if need else 0)
    return ready[1]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else LIMIT
    parent = [0] * (n + 1)
    for v in range(2, n + 1):
        if mode == 3:
            parent[v] = v - 1 if v <= n // 2 else n // 2
        elif mode == 4:
            parent[v] = 1 if v <= n // 10 else rng.randint(2, n // 10)
        elif mode == 5:
            parent[v] = max(1, v - rng.randint(1, 2))
        else:
            parent[v] = rng.randint(1, v - 1)
    labels = [0, 1] + rng.sample(range(2, n + 1), n - 1)
    days = [rng.randint(0, DAYS) for _ in range(n + 1)]
    rows = sorted((labels[v], labels[parent[v]], days[v]) for v in range(2, n + 1))
    if mode == 1:
        limit = rng.randint(0, sum(days) + 1)
    else:
        # aim the limit at the days needed for a random share, so the
        # answer is seldom 0 or 100
        limit = max(0, king_ready(n, parent, days, rng.randint(1, 99)) - rng.randint(0, 1))
    print(n, limit)
    for _, p, d in rows:
        print(p, d)


main()
