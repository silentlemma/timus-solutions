"""Modes:
SEED N TOP: legacy random pencils; degeneracies are left to chance.
grid SEED N TOP: random pencils in [-TOP, TOP], rejecting every collinear
triple and concyclic quadruple (intended for small N).
parabola SEED N: shuffled points (t-10^8, t^2-10^8), t=10001-N..10000.
Positive distinct t guarantees no collinear triple or concyclic quadruple.
"""

from itertools import combinations
import random
import sys


def general_position(pts, p):
    for a, b in combinations(pts, 2):
        if (a[0] - p[0]) * (b[1] - p[1]) == (a[1] - p[1]) * (b[0] - p[0]):
            return False
    for a, b, c in combinations(pts, 3):
        rows = [(q[0] - p[0], q[1] - p[1]) for q in (a, b, c)]
        (ax, ay), (bx, by), (cx, cy) = rows
        aa, bb, cc = ax * ax + ay * ay, bx * bx + by * by, cx * cx + cy * cy
        if ax * (by * cc - bb * cy) - ay * (bx * cc - bb * cx) + aa * (bx * cy - by * cx) == 0:
            return False
    return True


def main():
    if sys.argv[1] in ("grid", "parabola"):
        sys.stdout.reconfigure(newline="\n")
        mode, seed, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
        rng = random.Random(seed)
        assert 3 <= n <= 4999 and n % 2 == 1
        if mode == "parabola":
            pts = [(t - 10**8, t * t - 10**8) for t in range(10001 - n, 10001)]
            rng.shuffle(pts)
        else:
            top = int(sys.argv[4])
            assert 1 <= top <= 10**8
            pts = []
            while len(pts) < n:
                p = (rng.randint(-top, top), rng.randint(-top, top))
                if p not in pts and general_position(pts, p):
                    pts.append(p)
        sys.stdout.write("\n".join([str(n)] + ["%d %d" % p for p in pts]) + "\n")
        return
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    pts = set()
    while len(pts) < n:
        pts.add((rng.randint(-top, top), rng.randint(-top, top)))
    pts = list(pts)
    rng.shuffle(pts)
    sys.stdout.write("\n".join([str(n)] + ["%d %d" % p for p in pts]) + "\n")


if __name__ == "__main__":
    main()
