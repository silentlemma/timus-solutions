"""One test from a seed and a mode: mode 1 small coordinates, mode 2 the
largest coordinates and intensities, mode 3 a flat tetrahedron, mode 4
stars along the axes."""

import math
import random
import sys

LIMIT = 100
BRIGHTEST = 2500
MOST_STARS = 10


def star(rng, used):
    while True:
        v = tuple(rng.randint(-BRIGHTEST, BRIGHTEST) for _ in range(3))
        length = math.sqrt(sum(x * x for x in v))
        if 0 < length <= BRIGHTEST:
            g = math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2]))
            direction = tuple(x // g for x in v)
            if direction not in used:
                used.add(direction)
                return v


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = 3 if mode == 1 else LIMIT
    while True:
        pts = [[rng.randint(-top, top) for _ in range(3)] for _ in range(4)]
        if mode == 3:
            pts[3] = [(pts[0][t] + pts[1][t] + pts[2][t]) // 3 for t in range(3)]
            pts[3][rng.randrange(3)] += rng.choice((-1, 1))
        u, v, w = ([p[t] - pts[0][t] for t in range(3)] for p in pts[1:])
        volume = (u[0] * (v[1] * w[2] - v[2] * w[1]) - u[1] * (v[0] * w[2] - v[2] * w[0])
                  + u[2] * (v[0] * w[1] - v[1] * w[0]))
        if volume:
            break
    used = set()
    if mode == 4:
        axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        stars = [tuple(x * rng.randint(1, BRIGHTEST) for x in a) for a in axes]
    else:
        stars = [star(rng, used) for _ in range(rng.randint(1, MOST_STARS))]
    for p in pts:
        print(*p)
    print(len(stars))
    for s in stars:
        print(*s)


main()
