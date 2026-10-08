"""Random multigraphs; a test count, vertices, roads and the maximal length."""

import random
import sys

END_OF_INPUT = -1

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
