"""Pumpkins: a seed, N and a mode. Mode 1 scatters N points over the
whole field, mode 2 uses a square of the lattice around the first
pumpkin (many pumpkins on each ray), mode 3 puts the first pumpkin in a
corner of the field, mode 4 puts it in a corner of a lattice square."""

import random
import sys

TOP = 1000
MAX_N = 30000


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    if not 3 <= n <= MAX_N or mode not in (1, 2, 3, 4):
        raise ValueError("expected 3 <= N <= MAX_N and a mode from 1 to 4")
    rng = random.Random(seed)
    if mode in (1, 3):
        first = (-TOP, -TOP) if mode == 3 else (rng.randint(-TOP, TOP), rng.randint(-TOP, TOP))
        seen = {first}
        pts = [first]
        while len(pts) < n:
            p = (rng.randint(-TOP, TOP), rng.randint(-TOP, TOP))
            if p not in seen:
                seen.add(p)
                pts.append(p)
    else:
        side = max(2, int(n**0.5))
        lo = -(side // 2) if mode == 2 else -TOP
        grid = [(lo + i, lo + j) for i in range(side) for j in range(side)]
        first = (0, 0) if mode == 2 else (lo, lo)
        grid.remove(first)
        rng.shuffle(grid)
        pts = [first] + grid[: n - 1]
    a, b = pts[:2]
    if all((b[0] - a[0]) * (p[1] - a[1]) == (b[1] - a[1]) * (p[0] - a[0]) for p in pts[2:]):
        while True:
            p = (rng.randint(-TOP, TOP), rng.randint(-TOP, TOP))
            if p not in pts and (b[0] - a[0]) * (p[1] - a[1]) != (b[1] - a[1]) * (p[0] - a[0]):
                pts[-1] = p
                break
    print(len(pts))
    print("\n".join("%d %d" % p for p in pts))


main()
