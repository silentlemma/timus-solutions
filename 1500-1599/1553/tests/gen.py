"""One test from a seed and a mode: a tree of caves and queries. Mode 1
takes N = Q = 100000 on a random tree, mode 2 a path, mode 3 a star, mode
4 a small tree, mode 5 a random tree whose root sits in the middle of a
long path, mode 6 increments of 10000 piling up on few caves."""

import random
import sys

LARGEST = 100000
SMALL = 8
TOP = 10000
FEW = 5


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 4 else LARGEST
    q = rng.randint(1, SMALL * 2) if mode == 4 else LARGEST
    label = list(range(1, n + 1))
    rng.shuffle(label)
    edges = []
    for v in range(1, n):
        if mode == 2:
            p = v - 1
        elif mode == 3:
            p = 0
        elif mode == 5:
            p = v - 1 if v < n // 2 else rng.randrange(v)
        else:
            p = rng.randrange(max(0, v - FEW * 10), v) if rng.random() < 0.5 else rng.randrange(v)
        edges.append((label[p], label[v]))
    rng.shuffle(edges)
    lines = [str(n)] + ["%d %d" % e for e in edges] + [str(q)]
    hot = [rng.randint(1, n) for _ in range(FEW)]
    for _ in range(q):
        if rng.random() < 0.5:
            u = rng.choice(hot) if mode == 6 else rng.randint(1, n)
            lines.append("I %d %d" % (u, TOP if mode == 6 else rng.randint(0, TOP)))
        else:
            lines.append("G %d %d" % (rng.randint(1, n), rng.randint(1, n)))
    print("\n".join(lines))


main()
