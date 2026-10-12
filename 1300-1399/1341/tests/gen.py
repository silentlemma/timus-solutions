"""A start and a side: a seed and a mode.

Mode 1: random start and side that stay away from the poles.
Mode 2: long side that ends the northern leg close to a pole.
Mode 3: long equator crossing with nearly symmetric parallels and small drift.
"""

import math
import random
import sys

RADIUS = 6400.0
EDGE = 89.0  # how close to a pole the northern leg may end


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        w = -rng.uniform(1, 60)
        lon = rng.uniform(-180, 180)
        north = -w + rng.choice((-1, 1)) * rng.uniform(0.0001, 0.001)
        side = math.radians(north - w) * RADIUS
        print("%.6f" % w)
        print("%.6f" % lon)
        print("%.3f" % side)
        return
    w = rng.uniform(-80, 80)
    lon = rng.uniform(-180, 180)
    room = math.radians(EDGE - w) * RADIUS  # the longest side before the pole
    side = rng.uniform(0.9, 1) * room if mode == 2 else rng.uniform(0, room)
    print("%.6f" % w)
    print("%.6f" % lon)
    print("%.3f" % side)


main()
