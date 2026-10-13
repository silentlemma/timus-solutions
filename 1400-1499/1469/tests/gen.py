"""Cigarettes: a seed, N and a mode. Mode 1 lays long disjoint horizontal
cigarettes, three to a row, and lets the last one touch the end of
another, mode 2 lays the disjoint cigarettes only (NO), mode 3
scatters long random cigarettes (crossings everywhere), mode 4 lays a
fan of cigarettes that all meet at one point."""

import random
import sys

TOP = 10000
PIECES = 3
SPANS = [(-TOP, -3334), (-3332, 3332), (3334, TOP)]


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    segs = []
    if mode in (1, 2):
        # three long pieces on each of some rows never meet, and the sweep
        # holds all of them at once
        rows = rng.sample(range(-TOP, TOP + 1), (n + PIECES - 1) // PIECES)
        for y in rows:
            for lo, hi in SPANS:
                segs.append((lo, y, hi, y))
        segs = segs[:n]
        rng.shuffle(segs)
        if mode == 1:
            x1, y1, x2, y2 = segs[0]
            segs[-1] = (x1, y1, x1, y1 + 1)  # a short upright piece from an end of the first one
    elif mode == 3:
        while len(segs) < n:
            s = tuple(rng.randint(-TOP, TOP) for _ in range(4))
            if s[:2] != s[2:]:
                segs.append(s)
    else:
        for i in range(n):
            x, y = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
            segs.append((0, 0, x, y) if (x, y) != (0, 0) else (0, 0, 1, 1))
    print(n)
    print("\n".join("%d %d %d %d" % s for s in segs))


main()
