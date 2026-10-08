"""Deterministic graph inputs; modes and arguments:

SEED TESTS N M MAX_LENGTH: random multigraphs (the original mode).
bipartite SEED TESTS N: complete balanced bipartite graphs, padded with
    parallel roads to N*(N-1) roads, all of length 300 (4 <= N <= 100).
forest SEED TESTS N: random trees padded with parallel roads to N*(N-1)
    roads, with lengths 1 or 300 (3 <= N <= 100); no valid cycle exists.
TESTS is between 1 and 5 in every mode.
"""

import random
import sys

END_OF_INPUT = -1

mode = sys.argv[1]
if mode in ("bipartite", "forest"):
    seed, tests, n = map(int, sys.argv[2:5])
    assert 1 <= tests <= 5
    assert (4 if mode == "bipartite" else 3) <= n <= 100
    rng = random.Random(seed)
    lines = []
    for _ in range(tests):
        labels = list(range(1, n + 1))
        rng.shuffle(labels)
        if mode == "bipartite":
            middle = n // 2
            pairs = [(a, b) for a in labels[:middle] for b in labels[middle:]]
        else:
            pairs = [(labels[i], labels[rng.randrange(i)]) for i in range(1, n)]
        rng.shuffle(pairs)
        m = n * (n - 1)
        lines.append("%d %d" % (n, m))
        for i in range(m):
            a, b = pairs[i % len(pairs)]
            if rng.randrange(2):
                a, b = b, a
            length = 300 if mode == "bipartite" else rng.choice((1, 300))
            lines.append("%d %d %d" % (a, b, length))
    lines.append(str(END_OF_INPUT))
    print("\n".join(lines))
    sys.exit(0)

seed, tests, n, m, max_length = (int(x) for x in sys.argv[1:6])
rng = random.Random(seed)
lines = []
for _ in range(tests):
    lines.append("%d %d" % (n, m))
    for _ in range(m):
        a, b = rng.sample(range(1, n + 1), 2)
        lines.append("%d %d %d" % (a, b, rng.randint(1, max_length)))
lines.append(str(END_OF_INPUT))
print("\n".join(lines))
