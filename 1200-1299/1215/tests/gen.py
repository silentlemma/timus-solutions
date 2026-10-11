"""A target and a shot: a seed, the number of random points whose hull is
the target, a coordinate range and a mode. Mode 1 shoots anywhere in the
range, mode 2 inside the target, mode 3 at its corners."""

import random
import sys

LIMIT = 2000


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    pts = sorted(set(points))
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def main():
    seed, count, size, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    while True:
        poly = hull([(rng.randint(-size, size), rng.randint(-size, size)) for _ in range(count)])
        if 3 <= len(poly) <= 100:
            break
    if mode == 2:
        a, b, c = rng.sample(poly, 3)
        shot = ((a[0] + b[0] + c[0]) // 3, (a[1] + b[1] + c[1]) // 3)
    elif mode == 3:
        shot = rng.choice(poly)
    else:
        shot = (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT))
    start = rng.randrange(len(poly))
    poly = poly[start:] + poly[:start]
    lines = ["%d %d %d" % (shot[0], shot[1], len(poly))] + ["%d %d" % p for p in poly]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
