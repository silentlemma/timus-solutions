"""Pumpkins: a seed, N and a mode. Mode 1 scatters N points over the
whole field, mode 2 fills a square of the lattice around the first
pumpkin (many pumpkins on each ray), mode 3 puts the first pumpkin in a
corner of the field, mode 4 puts it in a corner of a lattice square."""

import random
import sys

TOP = 1000


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
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
        side = int(n**0.5)
        lo = -(side // 2) if mode == 2 else -TOP
        grid = [(lo + i, lo + j) for i in range(side) for j in range(side)]
        first = (0, 0) if mode == 2 else (lo, lo)
        grid.remove(first)
        rng.shuffle(grid)
        pts = [first] + grid
    print(len(pts))
    print("\n".join("%d %d" % p for p in pts))


main()
