"""One test from a seed and a mode: Vasya and N cows that touch neither
Vasya nor each other. Mode 1 scatters 50000 cows over the whole square,
mode 2 packs cows in a lattice around Vasya, mode 3 puts a few cows near
Vasya, mode 4 puts rows of cows along rays from Vasya, mode 5 uses
P = 0 or 100, mode 6 is the lattice with 16 arrows and the largest cows."""

import math
import random
import sys

LARGEST = 50000
TOP = 25000
SMALL = 8
SPREAD = 40
GAP = 0.05
MOST_ARROWS = 16
LARGEST_R = 2.0
FAR = 3000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    k, p = rng.randint(2, 16), rng.randint(0, 100)
    if mode == 5:
        p = rng.choice((0, 100))
    r = round(rng.uniform(0.4, 2.0), 3)
    vx, vy = round(rng.uniform(-100, 100), 3), round(rng.uniform(-100, 100), 3)
    if mode == 6:
        k, r = MOST_ARROWS, LARGEST_R
    cows = []
    taken = set()
    cell = 2 * r + GAP  # cows in different cells of this size never meet

    def place(x, y):
        key = (math.floor(x / cell), math.floor(y / cell))
        near = [(key[0] + a, key[1] + b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        if any(c in taken for c in near) or math.hypot(x - vx, y - vy) <= r + GAP:
            return
        if abs(x) <= TOP and abs(y) <= TOP:
            taken.add(key)
            cows.append((x, y))

    if mode in (2, 6):
        side = int(math.isqrt(LARGEST)) + 1
        for a in range(side):
            for b in range(side):
                place(vx + (a - side / 2) * cell * 2, vy + (b - side / 2) * cell * 2)
    elif mode == 4:
        while len(cows) < LARGEST // 10:
            angle, start = rng.uniform(0, 2 * math.pi), rng.uniform(0, FAR)
            for step in range(1, rng.randint(2, 9)):
                d = start + step * 3 * cell
                place(vx + d * math.cos(angle), vy + d * math.sin(angle))
    else:
        want = rng.randint(1, SMALL) if mode == 3 else LARGEST
        while len(cows) < want:
            if mode == 3:
                place(vx + rng.uniform(-SPREAD, SPREAD), vy + rng.uniform(-SPREAD, SPREAD))
            else:
                place(rng.uniform(-TOP, TOP), rng.uniform(-TOP, TOP))
    cows = cows[:LARGEST]
    print(len(cows), k, p, r)
    print(vx, vy)
    for x, y in cows:
        print("%.4f %.4f" % (x, y))


main()
