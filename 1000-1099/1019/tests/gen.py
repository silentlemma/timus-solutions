"""Random repaintings; a seed, N, the largest coordinate used and whether
the first repainting makes the whole range from 1 to that coordinate black
(so that the white intervals come from later repaintings)."""

import random
import sys

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
