"""A random connected map: a seed, N, the number of borders and whether to
add one border inside a colour class (then no colouring exists)."""

import random
import sys


def main():
    seed, n, m, odd = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    side = [0] + [rng.randrange(2) for _ in range(n - 1)]
    reds = [v for v in range(n) if side[v] == 0]
    blues = [v for v in range(n) if side[v] == 1]
    if not blues:
        side[n - 1] = 1
        blues = [n - 1]
        reds.remove(n - 1)
    borders = set()
    # a spanning tree with every edge between the two colours
    order = list(range(n))
    rng.shuffle(order)
    placed = [order[0]]
    for v in order[1:]:
        options = [u for u in placed if side[u] != side[v]]
        if not options:
            continue
        u = rng.choice(options)
        borders.add((min(u, v), max(u, v)))
        placed.append(v)
    for v in order[1:]:
        if v not in placed:
            u = rng.choice([w for w in placed if side[w] != side[v]])
            borders.add((min(u, v), max(u, v)))
            placed.append(v)
    tries = 0
    while len(borders) < m and tries < 100 * m:
        tries += 1
        u, v = rng.choice(reds), rng.choice(blues)
        borders.add((min(u, v), max(u, v)))
    if odd:
        group = reds if len(reds) >= 2 else blues
        u, v = rng.sample(group, 2)
        borders.add((min(u, v), max(u, v)))
    higher = [[] for _ in range(n)]
    for u, v in borders:
        higher[u].append(v + 1)
    lines = [str(n)]
    for u in range(n):
        rng.shuffle(higher[u])
        lines.append(" ".join(map(str, higher[u] + [0])))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
