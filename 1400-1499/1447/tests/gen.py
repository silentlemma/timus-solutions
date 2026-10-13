"""Branch networks: a seed, N, M and a mode. A random spanning tree comes
first, so a network always exists, then random extra links up to M.
Mode 1 draws lengths and costs independently, mode 2 makes the cost
almost proportional to the length (many trees with close ratios), mode 3
takes small values with many ties."""

import random
import sys

TOP = 10**6
RATIO = 1000
SMALL = 3


def main():
    seed, n, m, mode = (int(a) for a in sys.argv[1:5])
    rng = random.Random(seed)
    pairs = set()
    order = list(range(1, n + 1))
    rng.shuffle(order)
    for k in range(1, n):
        a, b = order[k], order[rng.randrange(k)]
        pairs.add((min(a, b), max(a, b)))
    if m > n * (n - 1) // 2 // 2:
        rest = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1) if (a, b) not in pairs]
        rng.shuffle(rest)
        pairs.update(rest[: m - len(pairs)])
    while len(pairs) < m:
        a, b = rng.sample(range(1, n + 1), 2)
        pairs.add((min(a, b), max(a, b)))
    lines = [str(n), str(m)]
    links = list(pairs)
    rng.shuffle(links)
    for a, b in links:
        if mode == 1:
            d, c = rng.randint(1, TOP), rng.randint(1, TOP)
        elif mode == 2:
            d = rng.randint(1, TOP // RATIO)
            c = d * RATIO // 2 + rng.randint(0, RATIO)
        else:
            d, c = rng.randint(1, SMALL), rng.randint(1, SMALL)
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d %d %d" % (a, b, d, c))
    print("\n".join(lines))


main()
