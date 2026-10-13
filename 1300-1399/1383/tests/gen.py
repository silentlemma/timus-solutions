"""Flower-bed projects: a seed and a mode. Mode 1 gives up to 10 000 small
projects, many of them images of others under maps of either sign,
mode 2 one project of 200 000 points that a quarter turn keeps, mode 3
2 000 projects of 100 points in twin pairs. Mode 4 gives two equivalent
100 000-point lines, mode 5 gives 10 000 mixed-rank projects of 20 points,
and mode 6 gives irregular convex hulls and images of both orientations."""

import random
import sys

TOP = 1000
SMALL = 4
BIG = 200_000


def mapped(rng, points, sign):
    """The points under a random integer map whose determinant has this sign,
    or None if they would leave the allowed square."""
    while True:
        a, b, c, d = (rng.randint(-2, 2) for _ in range(4))
        if (a * d - b * c) * sign > 0:
            break
    tx, ty = rng.randint(-20, 20), rng.randint(-20, 20)
    out = [(a * x + b * y + tx, c * x + d * y + ty) for x, y in points]
    if any(abs(v) > TOP for p in out for v in p):
        return None
    rng.shuffle(out)
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    projects = []
    if mode == 1:
        while len(projects) < 10000:
            base = [
                (rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL))
                for _ in range(rng.randint(1, 8))
            ]
            projects.append(base)
            for _ in range(rng.randint(0, 3)):
                image = mapped(rng, base, rng.choice((1, -1)))
                if image is not None and len(projects) < 10000:
                    projects.append(image)
    elif mode == 2:
        pts = [(TOP, TOP), (-TOP, TOP), (-TOP, -TOP), (TOP, -TOP)]
        while len(pts) < BIG:
            x, y = rng.randint(-TOP + 1, TOP - 1), rng.randint(-TOP + 1, TOP - 1)
            pts += [(x, y), (-y, x), (-x, -y), (y, -x)]
        projects.append(pts[:BIG])
    elif mode == 4:
        base = [(-TOP, 0), (TOP, 0)]
        base += [(rng.randint(-TOP, TOP), 0) for _ in range(BIG // 2 - 2)]
        image = [(0, -x) for x, _ in base]
        rng.shuffle(base)
        rng.shuffle(image)
        projects = [base, image]
    elif mode == 5:
        bases = [
            [(0, 0)] * 20,
            [(0, 0)] * 10 + [(3, 1)] * 10,
            [(0, 0)] * 5 + [(3, 1)] * 15,
            [(0, 0)] * 2 + [(3, 0)] * 5 + [(0, 4)] * 13,
            [(0, 0)] * 2 + [(3, 0)] * 5 + [(7, 0)] * 13,
        ]
        for i in range(10000):
            projects.append(mapped(rng, bases[i % len(bases)], rng.choice((1, -1))))
        rng.shuffle(projects)
    elif mode == 6:
        xs = sorted(rng.sample(range(-31, 32), 60))
        base = [(x, x * x - 500) for x in xs]
        projects = [base, [(-x, -y) for x, y in base],
                    [(-x, y) for x, y in base], [(y, x) for x, y in base]]
        for points in projects:
            rng.shuffle(points)
    else:
        while len(projects) < 2000:
            base = [(rng.randint(-100, 100), rng.randint(-100, 100)) for _ in range(100)]
            image = mapped(rng, base, rng.choice((1, -1)))
            if image is not None:
                projects += [base, image]
        rng.shuffle(projects)
    print(len(projects))
    for p in projects:
        print(len(p))
        for x, y in p:
            print(x, y)


main()
