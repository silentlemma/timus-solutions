"""One test from a seed and a mode: holes that touch neither each other nor
the sides of the bar. Mode 1 tries for 100 small holes, mode 2 a few
large ones, mode 3 holes packed along the bar, mode 4 a few random ones.
Mode 5 makes 100 dense holes in twenty layers, mode 6 makes 100 tiny
holes close to side faces, mode 7 makes a transverse sheet of 100 holes."""

import math
import random
import sys

MOST = 100
SIDE = 10.0
LENGTH = 100.0
GAP = 0.01


def structured(rng, mode):
    holes = []
    if mode == 5:
        for layer in range(20):
            y = 2.5 + 5 * layer
            for x in (2.5, 7.5):
                for z in (2.5, 7.5):
                    r = rng.randint(235, 245) / 100
                    holes.append((x, y, z, r))
            holes.append((5, y, 5, rng.randint(80, 95) / 100))
    elif mode == 6:
        for i in range(MOST):
            r = rng.randint(100, 600) / 10000
            x = r + 0.0001 if i % 2 else SIDE - r - 0.0001
            z = r + 0.0001 if i % 4 < 2 else SIDE - r - 0.0001
            holes.append((x, 0.5 + i, z, r))
    else:
        for i in range(10):
            for j in range(10):
                y = rng.randint(497000, 503000) / 10000
                r = rng.randint(20, 40) / 100
                holes.append((0.5 + i, y, 0.5 + j, r))
    rng.shuffle(holes)
    print(len(holes))
    for h in holes:
        print("%.4f %.4f %.4f %.4f" % h)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        structured(rng, mode)
        return
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
