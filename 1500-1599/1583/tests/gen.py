"""One test from a seed and a mode: holes that touch neither each other nor
the sides of the bar. Mode 1 tries for 100 small holes, mode 2 a few
large ones, mode 3 holes packed along the bar, mode 4 a few random ones."""

import math
import random
import sys

MOST = 100
SIDE = 10.0
LENGTH = 100.0
GAP = 0.01


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    want = {1: MOST, 2: rng.randint(1, 6), 3: MOST, 4: rng.randint(1, 8)}[mode]
    holes = []
    tries = 0
    while len(holes) < want and tries < 100000:
        tries += 1
        if mode == 2:
            r = round(rng.uniform(2.0, SIDE / 2 - GAP), 2)
        elif mode == 3:
            r = round(rng.uniform(0.3, 1.5), 2)
        else:
            r = round(rng.uniform(0.1, 2.0), 2)
        x = round(rng.uniform(r + GAP, SIDE - r - GAP), 2)
        z = round(rng.uniform(r + GAP, SIDE - r - GAP), 2)
        y = round(rng.uniform(r + GAP, LENGTH - r - GAP), 2)
        if min(x, SIDE - x, z, SIDE - z) <= r or min(y, LENGTH - y) <= r:
            continue
        if all(math.dist((x, y, z), (a, b, c)) > r + s + GAP for a, b, c, s in holes):
            holes.append((x, y, z, r))
    print(len(holes))
    for h in holes:
        print("%.2f %.2f %.2f %.2f" % h)


main()
