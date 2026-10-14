"""One test from a seed and a mode, n = 50 unless small. Mode 1 is a
sparse random matrix, mode 2 hides a random cycle through all rows among
random entries, so the graph is strongly connected, mode 3 does the same
and then clears one column, mode 4 is a small random matrix, mode 5 splits
the rows into groups and lets each group lead only to the next one, a
periodic strongly connected graph."""

import random
import sys

LARGEST = 50
TOP = 100
SMALL = 5
SPARSE = 0.06


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 4 else LARGEST
    m = [[0] * n for _ in range(n)]

    def put(i, j):
        m[i][j] = rng.randint(1, TOP)

    if mode == 5:
        groups = rng.randint(2, SMALL)
        group = [i % groups for i in range(n)]
        rng.shuffle(group)
        for i in range(n):
            for j in range(n):
                if group[j] == (group[i] + 1) % groups and rng.random() < SPARSE * 2:
                    put(i, j)
        order = sorted(range(n), key=lambda i: (group[i], rng.random()))
        for k in range(n):
            # a cycle through the groups in turn keeps the graph connected
            i, j = order[k], order[(k + n // groups) % n]
            put(i, j)
    else:
        density = rng.random() / 2 if mode == 4 else SPARSE
        for i in range(n):
            for j in range(n):
                if rng.random() < density:
                    put(i, j)
        if mode in (2, 3):
            perm = list(range(n))
            rng.shuffle(perm)
            for k in range(n):
                put(perm[k], perm[(k + 1) % n])
        if mode == 3:
            gone = rng.randrange(n)
            for i in range(n):
                m[i][gone] = 0
    print(n)
    for row in m:
        print(" ".join(map(str, row)))


main()
