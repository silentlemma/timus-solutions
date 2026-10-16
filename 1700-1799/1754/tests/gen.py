"""One test from a seed and a mode: mode 1 a random pyramid with
coordinates up to 30, mode 2 one with coordinates up to 1000, mode 3 a
pyramid with its apex above a right-angled corner of the base, so that
two walls stand upright and the distances to them are whole numbers.
Mode 4 is a random thin pyramid at the minimum valid height H = 2,
with h = 1, mana = 2, and shuffled base corners.
In modes 1-3 the mana is set right at the cost of the nearest wall or
floor, give or take one, so both answers come up."""

import math
import random
import sys

SMALL = 30
LARGE = 1000
CORNERS = 3


def side(a, b, c, p):
    """Sign of p against the plane through a, b and c."""
    u = [b[j] - a[j] for j in range(len(a))]
    w = [c[j] - a[j] for j in range(len(a))]
    n = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
    s = sum(n[j] * (p[j] - a[j]) for j in range(len(a)))
    return (s > 0) - (s < 0), n, s


def inside(base, apex, p):
    faces = [(base[0], base[1], base[2], apex)]
    for i in range(CORNERS):
        faces.append((base[i], base[i - 1], apex, base[i - 2]))
    for a, b, c, other in faces:
        if side(a, b, c, p)[0] * side(a, b, c, other)[0] <= 0:
            return False
    return True


def nearest(base, apex, p):
    best = p[2]
    for i in range(CORNERS):
        _, n, s = side(base[i], base[i - 1], apex, p)
        best = min(best, abs(s) / math.sqrt(sum(c * c for c in n)))
    return best


def pyramid(rng, mode):
    if mode == 3:
        bx, by = rng.randint(-LARGE // 2, 0), rng.randint(-LARGE // 2, 0)
        p, q = rng.randint(2, LARGE // 2), rng.randint(2, LARGE // 2)
        base = [(bx, by, 0), (bx + p * rng.choice([1, -1]), by, 0),
                (bx, by + q * rng.choice([1, -1]), 0)]
        return base, (bx, by, rng.randint(2, LARGE))
    span = SMALL if mode == 1 else LARGE
    while True:
        base = [(rng.randint(-span, span), rng.randint(-span, span), 0) for _ in range(CORNERS)]
        a, b, c = base
        if (b[0] - a[0]) * (c[1] - a[1]) != (b[1] - a[1]) * (c[0] - a[0]):
            apex = (rng.randint(-span, span), rng.randint(-span, span), rng.randint(2, LARGE))
            return base, apex


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        ax, ay = rng.randint(-400, 400), rng.randint(-400, 400)
        width, depth = rng.randint(1, 500), rng.randint(1, 500)
        # At height 1 the inverse image of (0, 0) in the base is (-ax, -ay).
        base = [(-ax - width, -ay - depth), (-ax + width, -ay - depth),
                (-ax, -ay + depth)]
        rng.shuffle(base)
        print(2, 1, 2)
        for x, y in [(0, 0)] + base + [(ax, ay)]:
            print(x, y)
        return
    while True:
        base, apex = pyramid(rng, mode)
        xs = [v[0] for v in base]
        ys = [v[1] for v in base]
        for _ in range(SMALL):
            p = (rng.randint(min(xs), max(xs)), rng.randint(min(ys), max(ys)),
                 rng.randint(1, apex[2] - 1))
            if inside(base, apex, p):
                break
        else:
            continue
        break
    cost = p[2] + nearest(base, apex, p)
    mana = max(1, min(LARGE, math.floor(cost) + rng.choice([-1, 0, 0, 1])))
    print(mana, p[2], apex[2])
    for v in [p] + base + [apex]:
        print(v[0], v[1])


main()
