"""Cockroaches and sweets from a seed and a mode, at least 0.001 apart within
each kind. Mode 1: a few points with small integer coordinates (many ties);
2: a lattice with sweets on lattice and half-lattice points; 3: 100 000
cockroaches on a circle of radius 10 000 and sweets near its centre; 4: the
largest uniform test, 8 digits after the point; 5: points with 21 digits after
the point, rings of almost equal distances around the sweets; 6: cockroaches
on one line; 7: cockroaches spread uniformly, sweets packed in a tiny square;
8: 100 000 cockroaches on two thin diagonal rails with two distant outliers;
9: 10 000 sweets near the bisectors of a thin three-cockroach triangle."""

import math
import random
import sys

LIMIT = 10000
MOST_COCKROACHES = 100000
MOST_SWEETS = 10000
GAP = 0.001


def fmt(v, digits):
    return ("%." + str(digits) + "f") % v


def spread(rng, count, make):
    """count distinct points from make(), rounded so that they stay apart"""
    seen, out = set(), []
    cell = GAP * 2
    while len(out) < count:
        x, y = make()
        if abs(x) > LIMIT or abs(y) > LIMIT:
            continue
        k = (math.floor(x / cell), math.floor(y / cell))
        if any((k[0] + a, k[1] + b) in seen for a in (-1, 0, 1) for b in (-1, 0, 1)):
            continue
        seen.add(k)
        out.append((x, y))
    return out


def main():
    seed, mode = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    digits = 3
    if mode == 1:
        span = rng.randint(2, 6)
        cells = [(x, y) for x in range(-span, span + 1) for y in range(-span, span + 1)]
        roaches = rng.sample(cells, rng.randint(1, min(30, len(cells))))
        sweets = rng.sample(cells, rng.randint(0, min(10, len(cells))))
        digits = 0
    elif mode == 2:
        side = 300
        roaches = [(x * 3 - 450, y * 3 - 450) for x in range(side) for y in range(side)]
        rng.shuffle(roaches)
        roaches = roaches[: rng.randint(80000, side * side)]
        sweets = list({(rng.randint(-900, 900) * 1.5, rng.randint(-900, 900) * 1.5) for _ in range(MOST_SWEETS)})
        digits = 1
    elif mode == 3:
        radius = LIMIT

        def on_circle():
            a = rng.uniform(0, 2 * math.pi)
            return radius * math.cos(a), radius * math.sin(a)

        def near_centre():
            a, d = rng.uniform(0, 2 * math.pi), math.sqrt(rng.random()) * 10
            return d * math.cos(a), d * math.sin(a)

        roaches = spread(rng, MOST_COCKROACHES, on_circle)
        sweets = spread(rng, MOST_SWEETS, near_centre)
        digits = 9
    elif mode == 4:
        roaches = spread(rng, MOST_COCKROACHES, lambda: (rng.uniform(-LIMIT, LIMIT), rng.uniform(-LIMIT, LIMIT)))
        sweets = spread(rng, MOST_SWEETS, lambda: (rng.uniform(-LIMIT, LIMIT), rng.uniform(-LIMIT, LIMIT)))
        digits = 8
    elif mode == 5:
        centres = [(rng.uniform(-9000, 9000), rng.uniform(-9000, 9000)) for _ in range(200)]

        def ring():
            cx, cy = rng.choice(centres)
            a, r = rng.uniform(0, 2 * math.pi), 500 + rng.choice((0, 1e-9, 2e-9, 1e-12))
            return cx + r * math.cos(a), cy + r * math.sin(a)

        roaches = spread(rng, 20000, ring)
        sweets = centres
        digits = 21
    elif mode == 6:
        dx, dy = rng.choice(((1, 0), (0, 1), (1, 1), (3, -2)))
        ts = rng.sample(range(-2000, 2000), 3000)
        roaches = [(t * dx * 1.25, t * dy * 1.25) for t in ts]
        sweets = spread(rng, 2000, lambda: (rng.uniform(-LIMIT, LIMIT), rng.uniform(-LIMIT, LIMIT)))
    elif mode == 8:
        roaches = [(i / 5 - 5000, i / 5 - 5000 + offset)
                   for i in range(49999) for offset in (-0.001, 0.001)]
        roaches += [(-LIMIT, LIMIT), (LIMIT, -LIMIT)]
        rng.shuffle(roaches)
        sweets = [(rng.uniform(-LIMIT, LIMIT), rng.uniform(-LIMIT, LIMIT))
                  for _ in range(48)]
        sweets += [(i / 5 - 5000, i / 5 - 5000) for i in (0, 1, 12345, 49998)]
    elif mode == 9:
        roaches = [(-LIMIT, 0), (LIMIT, 0), (0, 0.001)]
        ys = list(range(-9999, 10000, 2))
        rng.shuffle(ys)
        sweets = [(rng.choice((-1, 1)) *
                   (5000 + y / 10000000 - 0.00000000005 + rng.randint(-6, 6) * 1e-12), y)
                  for y in ys]
        digits = 12
    else:
        roaches = spread(rng, MOST_COCKROACHES, lambda: (rng.uniform(-LIMIT, LIMIT), rng.uniform(-LIMIT, LIMIT)))
        base = (rng.uniform(-9000, 9000), rng.uniform(-9000, 9000))
        side = 100
        sweets = [(base[0] + i * 0.002, base[1] + j * 0.002) for i in range(side) for j in range(side)]
        digits = 6
    out = [str(len(roaches))]
    out += [fmt(x, digits) + " " + fmt(y, digits) for x, y in roaches]
    out.append(str(len(sweets)))
    out += [fmt(x, digits) + " " + fmt(y, digits) for x, y in sweets]
    print("\n".join(out))


main()
