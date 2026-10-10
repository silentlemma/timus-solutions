"""Beacons and control points: a seed, the number of beacons, the number
of control points and a mode. Mode 0 places everything at random, mode 1
puts the beacons near the border of the field, mode 2 measures one beacon
per point, mode 3 sometimes puts a control point on a beacon."""

import random
import sys

SIDE = 200
EDGE = 3
LARGEST_ID = 30000
CHANCE = 0.3


def main():
    seed, beacons, points, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    ids = rng.sample(range(1, LARGEST_ID + 1), beacons)
    if mode == 1:
        spots = [
            (
                rng.choice([rng.randint(1, EDGE), SIDE - rng.randint(0, EDGE - 1)]),
                rng.randint(1, SIDE),
            )
            for _ in ids
        ]
    else:
        spots = [(rng.randint(1, SIDE), rng.randint(1, SIDE)) for _ in ids]
    lines = [str(points)]
    for _ in range(points):
        if mode == 3 and rng.random() < CHANCE:
            x, y = rng.choice(spots)
        else:
            x, y = rng.randint(1, SIDE), rng.randint(1, SIDE)
        count = 1 if mode == 2 else rng.randint(1, beacons)
        chosen = rng.sample(range(beacons), count)
        parts = [
            "%d-%d" % (ids[k], max(abs(x - spots[k][0]), abs(y - spots[k][1]))) for k in chosen
        ]
        lines.append("%d,%d:%s" % (x, y, ",".join(parts)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
