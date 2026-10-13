"""One test from a seed and a mode. The token is the drawn triangle moved
by: mode 1 a quarter, half or three-quarter turn and a shift, mode 2 a
turn by a Pythagorean angle (exact on integer points), mode 3 a mirror
image or an unrelated triangle, mode 4 only a shift, mode 5 a turn of an
isosceles triangle. The token's vertices come in a random order."""

import random
import sys

REACH = 2000
TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (20, 21, 29), (1599, 80, 1601)]


def rotate(p, cos, sin, scale):
    return ((p[0] * cos - p[1] * sin) // scale, (p[0] * sin + p[1] * cos) // scale)


def inside(points):
    return all(abs(c) <= REACH for p in points for c in p)


def triangle(rng, reach, step=1):
    while True:
        pts = [
            (rng.randint(-reach, reach) * step, rng.randint(-reach, reach) * step) for _ in range(3)
        ]
        a, b, c = pts
        if (b[0] - a[0]) * (c[1] - a[1]) != (b[1] - a[1]) * (c[0] - a[0]):
            return pts


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 2:
            cos, sin, hyp = rng.choice(TRIPLES)
            if rng.random() < 0.5:
                cos, sin = -sin, cos
            drawn = triangle(rng, max(1, REACH // (2 * hyp)), hyp)
            token = [rotate(p, cos, sin, hyp) for p in drawn]
        elif mode == 5:
            h, w = rng.randint(1, REACH // 4), rng.randint(1, REACH // 4)
            drawn = [(-w, 0), (w, 0), (0, h)]
            cos, sin = rng.choice([(0, 1), (-1, 0), (0, -1)])
            token = [rotate(p, cos, sin, 1) for p in drawn]
        else:
            drawn = triangle(rng, REACH // 2)
            if mode == 1:
                cos, sin = rng.choice([(0, 1), (-1, 0), (0, -1)])
                token = [rotate(p, cos, sin, 1) for p in drawn]
            elif mode == 3:
                token = (
                    [(-x, y) for x, y in drawn] if rng.random() < 0.5 else triangle(rng, REACH // 2)
                )
            else:
                token = list(drawn)
        dx, dy = rng.randint(-REACH // 2, REACH // 2), rng.randint(-REACH // 2, REACH // 2)
        token = [(x + dx, y + dy) for x, y in token]
        if inside(drawn) and inside(token):
            break
    rng.shuffle(token)
    print(" ".join("%d %d" % p for p in drawn))
    print(" ".join("%d %d" % p for p in token))


main()
