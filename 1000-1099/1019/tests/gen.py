"""Deterministic repaintings, with these modes:

SEED N SPAN COVER: random repaintings (the original positional mode); COVER
makes the first repainting black from 1 to SPAN when nonzero.
nested N: alternating black and white intervals with distinct nested ends.
comb SEED N: a black cover followed by shuffled, disjoint random white islands.
"""

import random
import sys

END = 10**9

if sys.argv[1] == "nested":
    n = int(sys.argv[2])
    assert 1 <= n <= 5000
    print(n)
    for i in range(n):
        print(i + 1, END - i - 1, "b" if i % 2 == 0 else "w")
    sys.exit()

if sys.argv[1] == "comb":
    seed, n = map(int, sys.argv[2:4])
    assert 2 <= n <= 5000
    rng = random.Random(seed)
    islands = []
    for i in range(1, n):
        a = 1 + i * ((END - 2) // n)
        islands.append((a, a + rng.randint(1, 31)))
    rng.shuffle(islands)
    print(n)
    print(1, END - 1, "b")
    for a, b in islands:
        print(a, b, "w")
    sys.exit()

seed, n, span, cover = (int(x) for x in sys.argv[1:5])
rng = random.Random(seed)
lines = [str(n)]
if cover:
    lines.append("1 %d b" % span)
    n -= 1
for _ in range(n):
    a, b = sorted(rng.sample(range(1, span + 1), 2))
    lines.append("%d %d %s" % (a, b, rng.choice("bw")))
print("\n".join(lines))
