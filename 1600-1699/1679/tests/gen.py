"""One test from a seed and a mode: mode 1 random points, mode 2 points
on the square with vertices (±R, 0) and (0, ±R), mode 3 points on
squares with integer vertices (R from a Pythagorean triple), mode 4 a
point and its turn by a multiple of 90 degrees, mode 5 near misses,
mode 6 a mix of everything with small R, mode 7 maximal batches on
squares with nonintegral rational vertices and one-coordinate perturbations
at R = 9999 and R = 10000."""

import random
import sys

T = 1000
MOST_R = 10000
TRIPLES = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29),
           (12, 35, 37), (9, 40, 41), (28, 45, 53), (11, 60, 61), (33, 56, 65)]


def in_disc(r, rng):
    while True:
        x, y = rng.randint(-r, r), rng.randint(-r, r)
        if x * x + y * y <= r * r:
            return x, y


def on_diamond(r, rng):
    x = rng.randint(-r, r)
    y = (r - abs(x)) * rng.choice((-1, 1))
    return (x, y) if rng.random() < 0.5 else (y, x)


def on_square(rng, top):
    """R and a point on the square with vertices k(a, b), k(-b, a), ..."""
    a, b, c = rng.choice(TRIPLES)
    k = rng.randint(1, max(1, top // c))
    vertices = [(a, b), (-b, a), (-a, -b), (b, -a)]
    i = rng.randrange(4)
    (px, py), (qx, qy) = vertices[i], vertices[(i + 1) % 4]
    # points k * (P + j (Q - P) / k) for j = 0..k are integer
    j = rng.randint(0, k)
    return c * k, (k * px + j * (qx - px), k * py + j * (qy - py))


def rotate(p, rng):
    x, y = p
    return rng.choice(((x, y), (-x, -y), (-y, x), (y, -x)))


def line(mode, rng, top):
    if mode == 1:
        r = rng.randint(1, top)
        return (r,) + in_disc(r, rng) + in_disc(r, rng)
    if mode == 2:
        r = rng.randint(1, top)
        return (r,) + rotate(on_diamond(r, rng), rng) + on_diamond(r, rng)
    if mode == 3:
        r, p = on_square(rng, top)
        while True:
            r2, q = on_square(rng, top)
            if r2 == r:
                break
            r, p = r2, q
        return (r,) + rotate(p, rng) + q
    if mode == 4:
        r = rng.randint(1, top)
        p = in_disc(r, rng)
        return (r,) + p + rotate(p, rng)
    r = rng.randint(2, top)
    x, y = on_diamond(r, rng)
    x2, y2 = on_diamond(r, rng)
    dx, dy = rng.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
    if (x2 + dx) ** 2 + (y2 + dy) ** 2 <= r * r:
        x2, y2 = x2 + dx, y2 + dy
    return r, x, y, x2, y2


def rational_square(rng, index):
    """a*x + b*y = R*k is a side because a*a + b*b = 2*k*k."""
    r = MOST_R - index % 2
    a, b, k = rng.choice(((7, 17, 13), (7, 23, 17)))
    # Neither radius is divisible by k, so this square's vertices are nonintegral.
    x0 = (r * k * pow(a, -1, b)) % b
    y0 = (r * k - a * x0) // b
    points = []
    for t in range(-2 * r // b, 2 * r // b + 1):
        x, y = x0 + b * t, y0 - a * t
        if x * x + y * y <= r * r:
            points.append((x, y))
    p, q = rng.sample(points, 2)
    p, q = rotate(p, rng), rotate(q, rng)
    if index % 3 == 0:
        dx, dy = rng.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
        x, y = q[0] + dx, q[1] + dy
        if x * x + y * y <= r * r:
            q = x, y
    return (r,) + p + q


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = MOST_R if mode < 6 else 30
    print(T)
    for i in range(T):
        if mode == 7:
            print(*rational_square(rng, i))
            continue
        m = mode if mode < 6 else rng.randint(1, 5)
        print(*line(m, rng, top))


main()
