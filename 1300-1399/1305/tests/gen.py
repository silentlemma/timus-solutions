"""Points: a seed and a mode. Mode 1 gives a few points on a small grid,
mode 2 100000 random points on the full grid, mode 3 points on one line
in a random direction, mode 4 100000 copies of a few points, mode 5
points inside a random diamond, so the hull has slanted sides."""

import random
import sys

TOP = 1000
COUNT = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        points = [(rng.randint(0, 6), rng.randint(0, 6)) for _ in range(rng.randint(1, 8))]
    elif mode == 2:
        points = [(rng.randint(0, TOP), rng.randint(0, TOP)) for _ in range(COUNT)]
    elif mode == 3:
        dx, dy = rng.choice([(1, 0), (0, 1), (1, 1), (1, -1), (1, 2), (3, 1)])
        x0, y0 = rng.randint(0, TOP // 2), rng.randint(TOP // 4, 3 * TOP // 4)
        points = []
        for _ in range(rng.randint(1, 50)):
            k = rng.randint(0, 100)
            x, y = x0 + k * dx, y0 + k * dy
            if 0 <= x <= TOP and 0 <= y <= TOP:
                points.append((x, y))
        points = points or [(x0, y0)]
    elif mode == 4:
        few = [(rng.randint(0, TOP), rng.randint(0, TOP)) for _ in range(3)]
        points = [rng.choice(few) for _ in range(COUNT)]
    else:
        cx, cy, r = TOP // 2, TOP // 2, rng.randint(1, TOP // 2)
        points = []
        while len(points) < COUNT // 10:
            x, y = rng.randint(cx - r, cx + r), rng.randint(cy - r, cy + r)
            if abs(x - cx) + abs(y - cy) <= r:
                points.append((x, y))
    print(len(points))
    print("\n".join("%d %d" % p for p in points))


main()
