"""One test from a seed and a mode:
1 small coordinates; 2 largest coordinates and intensities; 3 flat tetrahedron;
4 stars along the axes; 5 ten nearly parallel stars; 6 ten faint stars;
7 a large oblique tetrahedron with determinant one and ten random stars.
"""

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


def targeted(rng, mode):
    if mode == 7:
        a, b = (rng.randint(150, 200) for _ in range(2))
        pts = [(-100, -100, -1), (a - 100, -99, -1),
               (-100, b - 100, 0), (-99, -100, -1)]
        axes = rng.sample(range(3), 3)
        signs = [rng.choice((-1, 1)) for _ in range(3)]
        pts = [tuple(p[axes[i]] * signs[i] for i in range(3)) for p in pts]
    else:
        while True:
            pts = [tuple(rng.randint(-LIMIT, LIMIT) for _ in range(3)) for _ in range(4)]
            u, v, w = ([p[t] - pts[0][t] for t in range(3)] for p in pts[1:])
            if (u[0] * (v[1] * w[2] - v[2] * w[1])
                    - u[1] * (v[0] * w[2] - v[2] * w[0])
                    + u[2] * (v[0] * w[1] - v[1] * w[0])):
                break
    rng.shuffle(pts)
    used = set()
    if mode == 5:
        x, y = (rng.randint(-300, 300) for _ in range(2))
        stars = []
        while len(stars) < MOST_STARS:
            s = (x + rng.randint(-3, 3), y + rng.randint(-3, 3),
                 2400 + rng.randint(-3, 3))
            g = math.gcd(*s)
            direction = tuple(t // g for t in s)
            if direction not in used:
                used.add(direction)
                stars.append(s)
    elif mode == 6:
        faint = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1)
                 for z in (-1, 0, 1) if (x, y, z) != (0, 0, 0)]
        stars = rng.sample(faint, MOST_STARS)
    else:
        stars = [star(rng, used) for _ in range(MOST_STARS)]
    for p in pts:
        print(*p)
    print(len(stars))
    for s in stars:
        print(*s)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        targeted(rng, mode)
        return
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
