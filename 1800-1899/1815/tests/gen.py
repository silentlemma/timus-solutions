"""Usage: gen.py SEED MODE [COUNT], with COUNT used only by modes 5-7.

Mode 1: legacy small coordinates and costs, often coincident or collinear.
Mode 2: legacy coordinates up to 1000 and costs up to 3000.
Mode 3: legacy equal costs. Mode 4: legacy one cost far above the others.
Mode 5: determinant-one thin triangles, up to 10000 cases by default.
Mode 6: integer interior optima with balanced 3:4:5 forces.
Mode 7: prices exactly on, or one unit beside, a city-optimum boundary.
"""

import random
import sys

TESTS = 10000
LIMIT = 1000
SMALL = 3
CITIES = 3


def targeted(rng, mode, count):
    assert 1 <= count <= TESTS
    lines = [str(count)]
    for i in range(count):
        if mode == 5:
            k = rng.randint(2, LIMIT)
            points = [(0, 0), (k, k - 1), (k - 1, k - 2)]
            costs = [rng.randint(1, LIMIT) for _ in range(CITIES)]
            if i % 3 == 0:
                costs = [rng.randint(1, LIMIT)] * CITIES
        elif mode == 6:
            a, b, c = rng.randint(1, 700), rng.randint(1, 700), rng.randint(1, 180)
            points = [(a, 0), (0, b), (-3 * c, -4 * c)]
            m = rng.randint(1, LIMIT // 5)
            costs = [3 * m, 4 * m, 5 * m]
        else:
            a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)])
            scale = rng.randint(1, LIMIT // max(a, b))
            points = [(0, 0), (a * scale, b * scale), (a * scale, -b * scale)]
            m = rng.randint(1, (LIMIT - 1) // max(2 * a, c))
            costs = [2 * a * m + rng.choice([-1, 0, 1]), c * m, c * m]
        sx, sy = rng.choice([-1, 1]), rng.choice([-1, 1])
        points = [(sx * x, sy * y) for x, y in points]
        if rng.randrange(2):
            points = [(y, x) for x, y in points]
        tx = rng.randint(-LIMIT - min(x for x, y in points),
                         LIMIT - max(x for x, y in points))
        ty = rng.randint(-LIMIT - min(y for x, y in points),
                         LIMIT - max(y for x, y in points))
        cities = list(zip([(x + tx, y + ty) for x, y in points], costs))
        rng.shuffle(cities)
        lines.extend("%d %d" % p for p, w in cities)
        lines.append(" ".join(str(w) for p, w in cities))
    print("\n".join(lines))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        targeted(rng, mode, int(sys.argv[3]) if len(sys.argv) > 3 else TESTS)
        return
    top = SMALL if mode == 1 else LIMIT
    lines = [str(TESTS)]
    for _ in range(TESTS):
        for _ in range(CITIES):
            lines.append("%d %d" % (rng.randint(-top, top), rng.randint(-top, top)))
        if mode == 3:
            costs = [rng.randint(1, LIMIT)] * CITIES
        elif mode == 4:
            costs = [rng.randint(1, 10) for _ in range(CITIES)]
            costs[rng.randrange(CITIES)] = rng.randint(LIMIT // 2, LIMIT)
        else:
            costs = [rng.randint(1, top * 3) for _ in range(CITIES)]
        lines.append(" ".join(map(str, costs)))
    print("\n".join(lines))


main()
