"""One test from a seed and a mode:
1: small coordinates; 2: full coordinate range; 3: near the tangent case;
4: right angle at B with AB > BC; 5: nearly collinear, doubled area one.
"""

import random
import sys

LIMIT = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (4, 5):
        if mode == 4:
            long_leg = rng.randint(2, 2 * LIMIT)
            short_leg = rng.randint(1, long_leg - 1)
            pts = [(0, 0), (long_leg, 0), (long_leg, short_leg)]
        else:
            n = rng.randint(40, 2 * LIMIT - 1)
            pts = [(0, 0), (n, n - 1), (n + 1, n)]
        sx, sy = rng.choice((-1, 1)), rng.choice((-1, 1))
        pts = [(sx * x, sy * y) for x, y in pts]
        if rng.randrange(2):
            pts = [(y, x) for x, y in pts]
        dx = rng.randint(-LIMIT - min(x for x, y in pts), LIMIT - max(x for x, y in pts))
        dy = rng.randint(-LIMIT - min(y for x, y in pts), LIMIT - max(y for x, y in pts))
        for x, y in pts:
            print(x + dx, y + dy)
        return
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
