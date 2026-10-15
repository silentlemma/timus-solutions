"""One test from a seed and a mode: lasers are placed at random heights and
the pairs whose projections cross on both rays are reported by which is
higher there. Mode 1 is small, mode 2 has 100 lasers and every crossing
pair, mode 3 has steep lasers and heights close together, mode 4 gives a
long chain of pairs so that heights pile up, mode 5 reports every crossing
of the full lines, repeated up to 10000 pairs."""

import random
import sys
from fractions import Fraction

COORD = 100
MOST_LASERS = 100
MOST_PAIRS = 10000


def crossing(a, b):
    """the parameters on a and b where their projections cross, or None"""
    xa, ya, ua, va, _ = a
    xb, yb, ub, vb, _ = b
    det = ua * vb - va * ub
    if det == 0:
        return None
    dx, dy = xb - xa, yb - ya
    return Fraction(dx * vb - dy * ub, det), Fraction(va * dx - ua * dy, det)


def same_plane(a, b):
    xa, ya, ua, va, _ = a
    xb, yb, ub, vb, _ = b
    return ua * vb == va * ub and (xb - xa) * va == (yb - ya) * ua


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = MOST_LASERS if mode in (2, 4, 5) else rng.randint(1, 10)
    spread = COORD // 10 if mode == 3 else COORD
    lasers = []
    while len(lasers) < n:
        u, v = rng.randint(-spread, spread), rng.randint(-spread, spread)
        if u == 0 and v == 0:
            continue
        w = rng.randint(-COORD, COORD)
        cand = (rng.randint(-COORD, COORD), rng.randint(-COORD, COORD), u, v, w)
        if not any(same_plane(cand, other) for other in lasers):
            lasers.append(cand)
    if mode in (4, 5):
        z = [Fraction(i * 1000) for i in range(n)]
    elif mode == 3:
        z = [Fraction(rng.randint(-10, 10)) for _ in range(n)]
    else:
        z = [Fraction(rng.randint(-10**4, 10**4), rng.randint(1, 7)) for _ in range(n)]
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            at = crossing(lasers[i], lasers[j])
            if at is None or (mode != 5 and (at[0] < 0 or at[1] < 0)):
                continue
            hi = z[i] + lasers[i][4] * at[0]
            hj = z[j] + lasers[j][4] * at[1]
            if hi != hj and (mode in (2, 4, 5) or rng.random() < 0.7):
                pairs.append((i, j) if hi > hj else (j, i))
    if mode == 5:
        pairs += [rng.choice(pairs) for _ in range(MOST_PAIRS - len(pairs))]
    rng.shuffle(pairs)
    print(n)
    for laser in lasers:
        print(*laser)
    print(len(pairs))
    for i, j in pairs:
        print(i + 1, j + 1)


main()
