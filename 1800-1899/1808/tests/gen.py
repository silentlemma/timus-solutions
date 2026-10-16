"""One test from a seed and a mode: a planet, a refractive index and two
observers outside it looking into it, with integer coordinates. Only
clear cases are printed: chords that cross well inside the planet or
miss each other by a margin. Mode 1 a small planet and coordinates up
to 30, mode 2 any values up to 1000, mode 3 a large index, mode 4 an
index close to 1, mode 5 any values, kept only when the answer is No."""

import random
import sys
from math import hypot, sqrt

LIMIT = 1000
SMALL = 30
MARGIN = 1e-3


def chord(r, eta, x, y, dx, dy):
    a = dx * dx + dy * dy
    b = 2 * (x * dx + y * dy)
    c = x * x + y * y - r * r
    disc = b * b - 4 * a * c
    if a == 0 or disc <= MARGIN * a:
        return None
    t = (-b - sqrt(disc)) / (2 * a)
    if t <= 0:
        return None
    ex, ey = x + dx * t, y + dy * t
    length = hypot(dx, dy)
    ux, uy = dx / length, dy / length
    nx, ny = -ex / r, -ey / r
    along = ux * nx + uy * ny
    tx, ty = (ux - along * nx) / eta, (uy - along * ny) / eta
    inward = sqrt(max(0.0, 1 - tx * tx - ty * ty))
    vx, vy = inward * nx + tx, inward * ny + ty
    span = -2 * (ex * vx + ey * vy)
    return (ex, ey), (ex + vx * span, ey + vy * span), span


def verdict(r, eta, a, b):
    """True, False, or None when too close to call."""
    one, two = chord(r, eta, *a), chord(r, eta, *b)
    if one is None or two is None or one[2] < MARGIN or two[2] < MARGIN:
        return None
    (p1, q1, _), (p2, q2, _) = one, two
    d1 = (q1[0] - p1[0], q1[1] - p1[1])
    d2 = (q2[0] - p2[0], q2[1] - p2[1])
    w = (p2[0] - p1[0], p2[1] - p1[1])
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < MARGIN:
        return None
    s = (w[0] * d2[1] - w[1] * d2[0]) / den
    t = (w[0] * d1[1] - w[1] * d1[0]) / den
    inside = MARGIN < s < 1 - MARGIN and MARGIN < t < 1 - MARGIN
    outside = not (-MARGIN <= s <= 1 + MARGIN and -MARGIN <= t <= 1 + MARGIN)
    return True if inside else False if outside else None


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else LIMIT
    while True:
        r = rng.randint(1, top)
        if mode == 3:
            eta = rng.randint(1000, 10000) / 100
        elif mode == 4:
            eta = rng.randint(100, 110) / 100
        else:
            eta = rng.randint(100, 400) / 100
        people = []
        while len(people) < 2:
            x, y = rng.randint(-top, top), rng.randint(-top, top)
            if x * x + y * y <= r * r:
                continue
            # look roughly at a random point of the planet
            gx, gy = rng.uniform(-r, r) * 0.9, rng.uniform(-r, r) * 0.9
            dx, dy = round(gx - x), round(gy - y)
            scale = max(abs(dx), abs(dy), 1)
            if scale > LIMIT:
                dx, dy = round(dx * LIMIT / scale), round(dy * LIMIT / scale)
            people.append((x, y, dx, dy))
        if people[0][:2] == people[1][:2]:
            continue
        answer = verdict(r, eta, people[0], people[1])
        if answer is not None and not (mode == 5 and answer):
            break
    print(r, "%.2f" % eta)
    for person in people:
        print(*person)


main()
