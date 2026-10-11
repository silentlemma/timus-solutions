"""A game tree: a seed and a mode. Nodes are numbered at random, so a
parent may come after its children. Mode 1 draws a small tree, mode 2 up
to 1000 nodes with up to five children each, mode 3 a long thin tree."""

import random
import sys

NODES = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 12) if mode == 1 else rng.randint(NODES // 2, NODES)
    # build the shape on labels 0..n-1 with 0 as the root
    parent = [None]
    kids = [0]
    for v in range(1, n):
        if mode == 3:
            p = max(0, v - rng.randint(1, 3))
        else:
            open_nodes = [u for u in range(v) if kids[u] < 5]
            p = rng.choice(open_nodes[-30:])
        parent.append(p)
        kids[p] += 1
        kids.append(0)
    names = [1] + rng.sample(range(2, n + 1), n - 1)
    lines = [None] * (n + 1)
    for v in range(1, n):
        name = names[v]
        if kids[v]:
            lines[name] = "N %d" % names[parent[v]]
        else:
            lines[name] = "L %d %s" % (names[parent[v]], rng.choice(["+1", "0", "-1"]))
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(lines[2:])))


if __name__ == "__main__":
    main()
