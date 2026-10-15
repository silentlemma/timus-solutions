"""One test from a seed and a mode: mode 1 a random regular triangle in the
box, mode 2 one with the shortest side 10, mode 3 the largest one that fits
around the origin, mode 4 a small one near a corner of the box, mode 5 a
rotated triangle nearly spanning the box, mode 6 a short triangle with a
vertex extremely close to the origin."""

import math
import random
import sys

BOX = 100
SHORTEST = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    turn = rng.uniform(0, 2 * math.pi)
    if mode in (5, 6):
        if mode == 5:
            unit = [(math.cos(turn + k * 2 * math.pi / 3),
                     math.sin(turn + k * 2 * math.pi / 3)) for k in range(3)]
            xmin, xmax = min(x for x, _ in unit), max(x for x, _ in unit)
            ymin, ymax = min(y for _, y in unit), max(y for _, y in unit)
            radius = min(2 * BOX / (xmax - xmin), 2 * BOX / (ymax - ymin))
            radius *= rng.uniform(0.999, 0.999999)
            cx = rng.uniform(-BOX - radius * xmin, BOX - radius * xmax)
            cy = rng.uniform(-BOX - radius * ymin, BOX - radius * ymax)
            vertices = [(cx + radius * x, cy + radius * y) for x, y in unit]
        else:
            x, y = rng.uniform(-1e-8, 1e-8), rng.uniform(-1e-8, 1e-8)
            side = rng.uniform(SHORTEST + 1e-5, 25)
            vertices = [(x, y), (x + side * math.cos(turn), y + side * math.sin(turn)),
                        (x + side * math.cos(turn + math.pi / 3),
                         y + side * math.sin(turn + math.pi / 3))]
        rng.shuffle(vertices)
        for x, y in vertices:
            print("%.12f %.12f" % (x, y))
        return
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
