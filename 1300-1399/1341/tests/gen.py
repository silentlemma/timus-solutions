"""A start and a side: a seed and a mode. Mode 1 gives a random start and
side that stay away from the poles, mode 2 a long side that ends the
northern leg close to a pole."""

import math
import random
import sys

RADIUS = 6400.0
EDGE = 89.0  # how close to a pole the northern leg may end


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    w = rng.uniform(-80, 80)
    lon = rng.uniform(-180, 180)
    room = math.radians(EDGE - w) * RADIUS  # the longest side before the pole
    side = rng.uniform(0.9, 1) * room if mode == 2 else rng.uniform(0, room)
    print("%.6f" % w)
    print("%.6f" % lon)
    print("%.3f" % side)


main()
