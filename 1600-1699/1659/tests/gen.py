"""One test from a seed and a mode: mode 1 a random regular triangle in the
box, mode 2 one with the shortest side 10, mode 3 the largest one that fits
around the origin, mode 4 a small one near a corner of the box."""

import math
import random
import sys

BOX = 100
SHORTEST = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    turn = rng.uniform(0, 2 * math.pi)
    shortest_radius = SHORTEST / math.sqrt(3)
    if mode == 3:
        cx = cy = 0.0
        radius = BOX
    else:
        radius = shortest_radius if mode == 2 else rng.uniform(shortest_radius, BOX / 2)
        room = BOX - radius
        if mode == 4:
            cx, cy = rng.choice((-1, 1)) * room, rng.choice((-1, 1)) * room
        else:
            cx, cy = rng.uniform(-room, room), rng.uniform(-room, room)
    sign = rng.choice((-1, 1))
    for k in range(3):
        a = turn + sign * k * 2 * math.pi / 3
        print("%.10f %.10f" % (cx + radius * math.cos(a), cy + radius * math.sin(a)))


main()
