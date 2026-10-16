"""One test from a seed and a mode: mode 1 a regular polygon in order,
either way round, mode 2 the same with one vertex moved by 0.001 to
0.01 towards the centre, mode 3 the vertices of a regular polygon in a
star order, mode 4 a smaller regular polygon walked round twice or
more."""

import math
import random
import sys

MOST = 100
SMALLEST = 0.16
SHIFT_LOW, SHIFT_HIGH = 0.001, 0.01
DIGITS = "%.12f"


def polygon(rng, n, step=1):
    r = rng.uniform(SMALLEST, 0.5)
    cx, cy = rng.uniform(r, 1 - r), rng.uniform(r, 1 - r)
    start = rng.uniform(0, 2 * math.pi)
    way = rng.choice((1, -1))
    return [(cx + r * math.cos(start + way * 2 * math.pi * step * i / n),
             cy + r * math.sin(start + way * 2 * math.pi * step * i / n)) for i in range(n)]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(3, MOST)
    if mode == 3:
        steps = []
        while not steps:
            n = rng.randint(5, MOST)
            steps = [k for k in range(2, n - 1) if math.gcd(k, n) == 1]
        pts = polygon(rng, n, rng.choice(steps))
    elif mode == 4:
        m = rng.randint(3, MOST // 2)
        n = m * rng.randint(2, MOST // m)
        pts = polygon(rng, m) * (n // m)
    else:
        pts = polygon(rng, n)
    if mode == 2:
        # the vertex moves towards the centre, so it stays on the square
        i = rng.randrange(n)
        x, y = pts[i]
        cx, cy = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
        shift = rng.uniform(SHIFT_LOW, SHIFT_HIGH) / math.hypot(cx - x, cy - y)
        pts[i] = (x + shift * (cx - x), y + shift * (cy - y))
    print(n)
    for x, y in pts:
        print(DIGITS % x, DIGITS % y)


main()
