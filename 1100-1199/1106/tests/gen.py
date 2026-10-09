"""Random friendships where everyone has a friend: a seed, the number of
members and a mode. Mode 0 adds random pairs, mode 1 splits everyone into
pairs (a triple when the count is odd), mode 2 joins stars, mode 3 lays
one long path."""

import random
import sys

NEW_CENTRE = 0.1


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    edges = set()

    def link(a, b):
        if a != b:
            edges.add((min(a, b), max(a, b)))

    order = list(range(1, n + 1))
    rng.shuffle(order)
    if mode == 0:
        for _ in range(rng.randint(n // 2, n * 2)):
            link(rng.randint(1, n), rng.randint(1, n))
    elif mode == 1:
        for k in range(0, n - 1, 2):
            link(order[k], order[k + 1])
        if n % 2:
            link(order[-1], order[0])
    elif mode == 2:
        centre = order[0]
        for v in order[1:]:
            if rng.random() < NEW_CENTRE:
                centre = v
            else:
                link(centre, v)
    else:
        for a, b in zip(order, order[1:]):
            link(a, b)
    # anyone left alone gets a random friend
    touched = {v for e in edges for v in e}
    for v in range(1, n + 1):
        if v not in touched:
            link(v, rng.choice([u for u in range(1, n + 1) if u != v]))
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    lines = [str(n)]
    for v in range(1, n + 1):
        rng.shuffle(adj[v])
        lines.append(" ".join(map(str, adj[v] + [0])))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
