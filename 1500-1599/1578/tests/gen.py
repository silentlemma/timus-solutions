"""One test from a seed and a mode: N + 2 different points. Mode 1 is 2002
random points, mode 2 points on one line, mode 3 a grid, mode 4 points
on a circle, mode 5 a few points."""

import math
import random
import sys

TURNS = 2000
TOP = 2000
FEW = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    total = rng.randint(3, FEW) if mode == 5 else TURNS + 2
    pts = set()
    if mode == 2:
        pts = {(x, 2 * x // 3) for x in rng.sample(range(-TOP, TOP + 1), total)}
    elif mode == 3:
        side = int(math.isqrt(total)) + 1
        grid = [(x, y) for x in range(side) for y in range(side)]
        pts = set(rng.sample(grid, total))
    elif mode == 4:
        while len(pts) < total:
            a = rng.uniform(0, 2 * math.pi)
            pts.add((round(TOP * math.cos(a)), round(TOP * math.sin(a))))
    else:
        while len(pts) < total:
            pts.add((rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)))
    pts = list(pts)
    rng.shuffle(pts)
    print(total - 2)
    for x, y in pts:
        print(x, y)


main()
