"""A picture of one figure: a seed and a mode. Mode 1 gives a circle,
mode 2 a slightly oval circle, mode 3 a turned square, mode 4 a triangle
with no angle under 10 degrees, mode 5 a thin triangle, mode 6 a
turned square across a picture of 1000 x 1000; sizes and places are
random and the width differs from the height. Mode 7 gives a circle
touching all sides of a 1000 x 1000 picture, mode 8 a solid square
filling that picture, mode 9 a right triangle spanning that picture,
and mode 10 a random obtuse triangle with every angle at least 10
degrees and every altitude at least 30 pixels."""

import math
import random
import sys

SMALLEST = 30
LARGEST = 1000
MARGIN = 3
MIN_ANGLE = 10
THIN = 15  # mode 5 wants an angle under this many degrees
BIG = 6  # mode 6 is a square across the largest picture


def convex(points):
    def inside(x, y):
        sign = 0
        for i, (ax, ay) in enumerate(points):
            bx, by = points[(i + 1) % len(points)]
            c = (bx - ax) * (y - ay) - (by - ay) * (x - ax)
            if c and sign and (c > 0) != (sign > 0):
                return False
            sign = sign or c
        return True

    return inside


def smallest(points):
    angles = []
    for i in range(3):
        (ax, ay), (bx, by), (qx, qy) = points[i], points[i - 1], points[i - 2]
        u, v = (bx - ax, by - ay), (qx - ax, qy - ay)
        cos = (u[0] * v[0] + u[1] * v[1]) / math.hypot(*u) / math.hypot(*v)
        angles.append(math.degrees(math.acos(max(-1.0, min(1.0, cos)))))
    return min(angles)


def angles_ok(points):
    return smallest(points) >= MIN_ANGLE


def special(rng, mode):
    sys.stdout.reconfigure(newline="\n")
    if mode in (7, 8, 9):
        w = h = LARGEST
        points = [(0, 0), (w, 0), (0, h)]
    else:
        while True:
            length = rng.randint(180, 240)
            x, y = rng.randint(40, length - 40), rng.randint(30, 45)
            points = [(0, 0), (length, 0), (x, y)]
            # The apex angle is at least 120 degrees when cos <= -1/2.
            dot = x * (x - length) + y * y
            product = (x * x + y * y) * ((length - x) ** 2 + y * y)
            area2 = length * y
            sides2 = [length * length, x * x + y * y, (length - x) ** 2 + y * y]
            if (dot < 0 and 4 * dot * dot >= product and angles_ok(points)
                    and all(area2 * area2 >= SMALLEST * SMALLEST * s for s in sides2)):
                break
        dx, dy = rng.randint(1, 40), rng.randint(1, 40)
        points = [(px + dx, py + dy) for px, py in points]
        w, h = length + dx + rng.randint(1, 40), max(32, y + dy + rng.randint(1, 40))
    print(w, h)
    for y in range(h):
        row = []
        for x in range(w):
            if mode == 7:
                filled = (2 * x + 1 - w) ** 2 + (2 * y + 1 - h) ** 2 <= w * w
            elif mode == 8:
                filled = True
            else:
                crosses = [
                    (bx - ax) * (2 * y + 1 - 2 * ay)
                    - (by - ay) * (2 * x + 1 - 2 * ax)
                    for (ax, ay), (bx, by) in zip(points, points[1:] + points[:1])
                ]
                filled = all(c >= 0 for c in crosses)
            row.append("1" if filled else "0")
        print("".join(row))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if 7 <= mode <= 10:
        special(rng, mode)
        return
    size = rng.randint(SMALLEST, LARGEST // 3)
    w = rng.randint(size + 2 * MARGIN, min(LARGEST, size * 3))
    h = rng.randint(size + 2 * MARGIN, min(LARGEST, size * 3))
    if mode == BIG:
        size, w, h, mode = LARGEST - 2 * MARGIN - 2, LARGEST, LARGEST, 3
    cx = rng.uniform(size / 2 + MARGIN, w - size / 2 - MARGIN)
    cy = rng.uniform(size / 2 + MARGIN, h - size / 2 - MARGIN)
    if mode in (1, 2):
        rx = size / 2
        ry = rx * (rng.uniform(0.88, 0.95) if mode == 2 else 1)

        def inside(x, y):
            return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1

    elif mode == 3:
        a, r = rng.uniform(0, math.pi / 2), size / 2
        inside = convex(
            [
                (cx + r * math.cos(a + k * math.pi / 2), cy + r * math.sin(a + k * math.pi / 2))
                for k in range(4)
            ]
        )
    else:
        while True:
            pts = [
                (cx + rng.uniform(-size, size) / 2, cy + rng.uniform(-size, size) / 2)
                for _ in range(3)
            ]
            longest = max(math.dist(pts[i], pts[i - 1]) for i in range(3))
            if longest >= SMALLEST and angles_ok(pts) and (mode == 4 or smallest(pts) < THIN):
                break
        inside = convex(pts)
    print(w, h)
    for y in range(h):
        print("".join("1" if inside(x + 0.5, y + 0.5) else "0" for x in range(w)))


main()
