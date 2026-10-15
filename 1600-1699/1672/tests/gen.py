"""One test from a seed and a mode: mode 1 up to 100 points anywhere, mode
2 a few points, mode 3 points on a plane, mode 4 points on a line, mode 5
points near a sphere, mode 6 a long thin cloud."""

import random
import sys

TOP = 100
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    pts = set()
    want = rng.randint(2, MOST) if mode in (1, 5, 6) else rng.randint(2, 6)
    if mode == 3:
        want = rng.randint(3, 40)
    if mode == 4:
        want = rng.randint(2, 20)
    while True:
        a = [rng.randint(-5, 5) for _ in range(3)]
        b = [rng.randint(-5, 5) for _ in range(3)]
        normal = (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
        if any(normal):
            break
    tries = 0
    while len(pts) < want and tries < 2000:
        tries += 1
        if mode in (1, 2):
            p = tuple(rng.randint(-TOP, TOP) for _ in range(3))
        elif mode == 3:
            s, t = rng.randint(-10, 10), rng.randint(-10, 10)
            p = tuple(s * a[k] + t * b[k] for k in range(3))
        elif mode == 4:
            s = rng.randint(-20, 20)
            p = tuple(s * a[k] for k in range(3))
        elif mode == 5:
            v = [rng.gauss(0, 1) for _ in range(3)]
            norm = sum(x * x for x in v) ** 0.5
            p = tuple(round(TOP * x / norm) for x in v)
        else:
            s = rng.uniform(-1, 1)
            p = tuple(round(TOP * s * c / 6 + rng.uniform(-3, 3)) for c in (6, 2, 1))
        if all(abs(c) <= TOP for c in p):
            pts.add(p)
    pts = list(pts)
    if len(pts) < 2:
        pts = [(1, 0, 0), (-1, 0, 0)]
    rng.shuffle(pts)
    print(len(pts))
    for p in pts:
        print(*p)


main()
