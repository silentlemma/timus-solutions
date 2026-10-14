"""One test from a seed and a mode, with integer factories inside the
disk. Mode 1 takes 300 random factories with R = 1000, mode 2 puts them
near a circle of half the radius, mode 3 takes one factory, mode 4
crowds them on one side, mode 5 repeats a few points many times, mode 6
is small, mode 7 puts them on a lattice."""

import math
import random
import sys

LARGEST = 300
RADIUS = 1000
SMALL = 6
STEP = 150


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    r = rng.randint(1, 20) if mode == 6 else RADIUS
    n = {3: 1, 6: rng.randint(1, SMALL)}.get(mode, LARGEST)

    def anywhere(radius, cx=0, cy=0):
        while True:
            x, y = cx + rng.randint(-radius, radius), cy + rng.randint(-radius, radius)
            if (x - cx) ** 2 + (y - cy) ** 2 <= radius * radius and x * x + y * y <= r * r:
                return x, y

    if mode == 2:
        pts = []
        for _ in range(n):
            a = rng.uniform(0, 2 * math.pi)
            pts.append((round(r / 2 * math.cos(a)), round(r / 2 * math.sin(a))))
    elif mode == 4:
        pts = [anywhere(r // 4, r // 2, 0) for _ in range(n)]
    elif mode == 5:
        spots = [anywhere(r) for _ in range(SMALL)]
        pts = [rng.choice(spots) for _ in range(n)]
    elif mode == 7:
        lattice = [
            (x, y)
            for x in range(-r, r + 1, STEP)
            for y in range(-r, r + 1, STEP)
            if x * x + y * y <= r * r
        ]
        pts = lattice[:LARGEST]
    else:
        pts = [anywhere(r) for _ in range(n)]
    print(len(pts), r)
    print("\n".join("%d %d" % p for p in pts))


main()
