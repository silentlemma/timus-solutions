"""A random acyclic network: a seed, N, M and a mode. The stations get a
random hidden order and every pipeline goes forward in it. Modes 1 and 3
pick S early and F late in that order, mode 2 picks them at random (often
no route); mode 3 adds every possible pipeline."""

import random
import sys

TOP = 10000


def main():
    seed, n, m, mode = (int(a) for a in sys.argv[1:5])
    rng = random.Random(seed)
    rank = list(range(1, n + 1))
    rng.shuffle(rank)
    if mode == 3:
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    else:
        chosen = set()
        while len(chosen) < m:
            i, j = sorted(rng.sample(range(n), 2))
            chosen.add((i, j))
        pairs = list(chosen)
    rng.shuffle(pairs)
    if mode != 2:
        s, f = rank[rng.randrange(n // 10 + 1)], rank[n - 1 - rng.randrange(n // 10 + 1)]
    else:
        s, f = (rank[k] for k in rng.sample(range(n), 2))
    lines = ["%d %d" % (n, len(pairs))]
    lines += ["%d %d %d" % (rank[i], rank[j], rng.randint(1, TOP)) for i, j in pairs]
    lines.append("%d %d" % (s, f))
    print("\n".join(lines))


main()
