"""10 000 paintings: a seed and a mode. Mode 1 has random points on the
whole canvas, mode 2 random points on a 7 by 7 grid, where ties and
collinear points are common, mode 3 corners of random tilted rectangles
and points on their sides, rounded to whole numbers, mode 4 points at
the very corners of the canvas's inner square."""

import random
import sys

N = 10000
LIMIT = 5000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    for _ in range(N):
        if mode == 1:
            pts = [(rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)) for _ in range(4)]
        elif mode == 2:
            pts = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(4)]
        elif mode == 3:
            # a corner, two side vectors (a, b) and (-b * k, a * k), and points on the sides
            a, b, k = rng.randint(-60, 60), rng.randint(-60, 60), rng.randint(1, 40)
            ox, oy = rng.randint(-2000, 2000), rng.randint(-2000, 2000)
            side = [(a, b), (-b * k, a * k)]
            pts = []
            for _ in range(4):
                s, t = rng.randint(0, 1), rng.choice([0, 1])
                f = rng.randint(0, 4) / 4 if (a * k) % 4 == 0 else rng.randint(0, 1)
                u = side[s]
                w = side[1 - s]
                pts.append((round(ox + u[0] * f + w[0] * t), round(oy + u[1] * f + w[1] * t)))
        else:
            pts = [
                rng.choice([(-LIMIT, -LIMIT), (LIMIT, LIMIT), (-LIMIT, LIMIT), (LIMIT, -LIMIT)])
                for _ in range(4)
            ]
        lines.append(" ".join("%d %d" % p for p in pts))
    print(N)
    print("\n".join(lines))


main()
