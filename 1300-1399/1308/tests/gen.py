"""A target point: a seed and a mode. Mode 1 gives any point within 25 of
the start, mode 2 a point near the edge of that circle, mode 3 a point
close to the start."""

import math
import random
import sys

REACH = 25


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        r = REACH * math.sqrt(rng.random())
    elif mode == 2:
        r = REACH - rng.random()
    else:
        r = rng.random() * 2
    angle = rng.uniform(0, 2 * math.pi)
    print("%.10f %.10f" % (r * math.cos(angle), r * math.sin(angle)))


main()
