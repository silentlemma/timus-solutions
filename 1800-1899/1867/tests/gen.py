"""Squared distances from a seed and a mode, all of them between points
of a hidden integer placement: mode 1 a few atoms near each other,
2 the most atoms spread far, 3 the most atoms with one distance changed
by one, 4 the most atoms on one slanted line, some of them in one spot,
5 the most atoms where the first distance is a sum of two squares in
many ways, 6 a few atoms with one distance changed by one, 7 the most
atoms on a line through the first two, at a distance that is a sum of
two squares in many ways, and one atom off it. Distances stay within
10^9."""

import random
import sys
from math import isqrt

MOST = 100
FEW = 5
NEAR = 6
FAR = 11000
# 5^2 * 13 * 17 * 29, a sum of two squares in many ways
RICH = 5 * 5 * 13 * 17 * 29


def points(rng, mode, n):
    if mode in (1, 6):
        return [(rng.randint(-NEAR, NEAR), rng.randint(-NEAR, NEAR)) for _ in range(n)]
    if mode == 4:
        dx, dy = rng.randint(1, NEAR), rng.randint(1, NEAR)
        steps = [rng.randint(-FAR // NEAR, FAR // NEAR) for _ in range(n // 2)]
        return [(dx * t, dy * t) for t in steps + rng.sample(steps, n - n // 2)]
    out = [(rng.randint(-FAR, FAR), rng.randint(-FAR, FAR)) for _ in range(n)]
    root = isqrt(RICH)
    ways = [(a, s * isqrt(RICH - a * a)) for a in range(-root, root + 1) for s in (1, -1)
            if isqrt(RICH - a * a) ** 2 == RICH - a * a]
    dx, dy = rng.choice(ways)
    if mode == 5:
        out[1] = (out[0][0] + dx, out[0][1] + dy)
    if mode == 7:
        reach = FAR // root
        out = [(0, 0), (dx, dy)] + [(dx * t, dy * t) for t in
                                    (rng.randint(-reach, reach) for _ in range(n - 3))]
        out.append((rng.randint(-FAR, FAR), rng.randint(-FAR, FAR)))
    return out


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode in (1, 6) else MOST
    pts = points(rng, mode, n)
    d = [[(p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 for q in pts] for p in pts]
    if mode in (3, 6):
        i, j = rng.sample(range(n), 2)
        d[i][j] += 1 if d[i][j] == 0 or rng.random() < 0.5 else -1
        d[j][i] = d[i][j]
    print(n)
    print("\n".join(" ".join(map(str, row)) for row in d))


main()
