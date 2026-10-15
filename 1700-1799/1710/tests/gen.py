"""One test from a seed and a mode: mode 1 small coordinates, mode 2 the
full range, mode 3 near the tangent case, where |BC| is close to the
distance from B to the line AC."""

import random
import sys

LIMIT = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = 5 if mode == 1 else LIMIT
    while True:
        pts = [(rng.randint(-top, top), rng.randint(-top, top)) for _ in range(3)]
        (ax, ay), (bx, by), (cx, cy) = pts
        cross = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        if cross == 0:
            continue
        dot = (bx - ax) * (cx - ax) + (by - ay) * (cy - ay)
        side = (cx - ax) ** 2 + (cy - ay) ** 2
        if mode == 3 and abs(dot - side) > side // 20:
            continue
        break
    for x, y in pts:
        print(x, y)


main()
