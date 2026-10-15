"""One test from a seed and a mode: mode 1 small coordinates, mode 2 any
coordinates up to 1000, mode 3 a book with sides along the axes, mode 4
the disk centered on a corner of the book, mode 5 the mouse on the far
side of the book from where the disk sticks out."""

import math
import random
import sys

LIMIT = 1000
SMALL = 20
SIDES = 4


def side(corners, i, x, y):
    (ax, ay), (bx, by) = corners[i], corners[(i + 1) % SIDES]
    return (bx - ax) * (y - ay) - (by - ay) * (x - ax)


def book(rng, top, straight):
    while True:
        if straight:
            a, b = rng.randint(1, top), 0
        else:
            a, b = rng.randint(-top, top), rng.randint(-top, top)
        if a == 0 and b == 0:
            continue
        g = math.gcd(a, b)
        m = rng.randint(1, top)
        u, v = (a, b), (-b // g * m, a // g * m)
        px, py = rng.randint(-top, top), rng.randint(-top, top)
        corners = [(px, py), (px + u[0], py + u[1]),
                   (px + u[0] + v[0], py + u[1] + v[1]), (px + v[0], py + v[1])]
        if all(abs(x) <= LIMIT and abs(y) <= LIMIT for x, y in corners):
            return corners


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else LIMIT // 2
    while True:
        corners = book(rng, top, mode == 3)
        xs, ys = [x for x, _ in corners], [y for _, y in corners]
        if mode == 4:
            cx, cy = rng.choice(corners)
        else:
            cx, cy = rng.randint(min(xs), max(xs)), rng.randint(min(ys), max(ys))
        if any(side(corners, i, cx, cy) < 0 for i in range(SIDES)):
            continue
        # the disk must stick out of the book
        reach = min(side(corners, i, cx, cy) / math.dist(corners[i], corners[(i + 1) % SIDES])
                    for i in range(SIDES))
        low = math.floor(reach) + 1
        r = rng.randint(low, max(low, int(reach * 2) + 2))
        if r > LIMIT:
            continue
        for _ in range(100):
            mx, my = rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)
            if mode == 1:
                mx, my = rng.randint(-SMALL * 3, SMALL * 3), rng.randint(-SMALL * 3, SMALL * 3)
            if (mx - cx) ** 2 + (my - cy) ** 2 <= r * r:
                continue
            if all(side(corners, i, mx, my) >= 0 for i in range(SIDES)):
                continue
            if mode == 5:
                # the far side: the book lies between the mouse and the center
                far = max(range(SIDES), key=lambda i: -side(corners, i, mx, my))
                if side(corners, far, cx, cy) / math.dist(corners[far], corners[(far + 1) % SIDES]) < r:
                    continue
            print(" ".join("%d %d" % p for p in corners))
            print(cx, cy, r)
            print(mx, my)
            return


main()
