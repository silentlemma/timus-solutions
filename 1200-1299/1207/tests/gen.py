"""Points with no three on a line: a seed, N and a mode. Mode 1 takes the
points (i, i^2 mod p) for a prime p, which has no three collinear points,
stretched and shuffled; mode 2 does the same with the axes swapped and
mirrored; mode 3 is a few random points checked by brute force; mode 4 is
a sheared modular parabola in reverse angular order; mode 5 is random
points across the full coordinate range, checked by brute force."""

from fractions import Fraction
import random
import sys

PRIME = 10007
TOP = 10**6


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode in (1, 2):
        sx, sy = rng.randint(1, TOP // PRIME), rng.randint(1, TOP // PRIME)
        rows = rng.sample(range(PRIME), n)
        pts = [(i * sx - TOP // 2, (i * i % PRIME) * sy - TOP // 2) for i in rows]
        if mode == 2:
            pts = [(-y, x) for x, y in pts]
    elif mode == 4:
        shear = rng.randint(80, 98)
        pts = [(shear * i + i * i % PRIME, i) for i in range(1, n)]
        pts.sort(key=lambda p: Fraction(p[1], p[0]), reverse=True)
        pts = [(0, 0)] + pts
        pts = [(x - TOP // 2, y - TOP // 2) for x, y in pts]
    else:
        bound = TOP if mode == 5 else 5
        pts = []
        while len(pts) < n:
            p = (rng.randint(-bound, bound), rng.randint(-bound, bound))
            if p in pts or any(collinear(a, b, p) for a in pts for b in pts if a < b):
                continue
            pts.append(p)
    if mode != 4:
        rng.shuffle(pts)
    lines = [str(n)] + ["%d %d" % p for p in pts]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
