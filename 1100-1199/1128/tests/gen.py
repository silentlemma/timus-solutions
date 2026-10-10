"""Random quarrels, each child with at most three enemies and enmity
mutual: a seed, N and a mode. Mode 0 adds random pairs while degrees allow,
mode 1 makes groups of four children who all quarrel, mode 2 builds long
chains and rings."""

import random
import sys

MOST = 3
CLIQUE = 4


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    adj = [set() for _ in range(n)]

    def link(a, b):
        if a != b and b not in adj[a] and len(adj[a]) < MOST and len(adj[b]) < MOST:
            adj[a].add(b)
            adj[b].add(a)

    order = list(range(n))
    rng.shuffle(order)
    if mode == 1:
        for k in range(0, n - CLIQUE + 1, CLIQUE):
            group = order[k : k + CLIQUE]
            for a in group:
                for b in group:
                    link(a, b)
    elif mode == 2:
        for a, b in zip(order, order[1:]):
            link(a, b)
        for _ in range(n // CLIQUE):
            link(rng.randrange(n), rng.randrange(n))
    else:
        for _ in range(MOST * n):
            link(rng.randrange(n), rng.randrange(n))
    lines = [str(n)]
    for a in range(n):
        lst = sorted(adj[a])
        rng.shuffle(lst)
        lines.append(" ".join(str(x) for x in [len(lst)] + [b + 1 for b in lst]))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
