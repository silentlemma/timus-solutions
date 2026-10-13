"""One test from a seed and a mode. Mode 1 scatters 1000 pieces with two
decimals over a table of radius 100 at random, mode 2 makes the pieces
heavier towards the centre, so many heavy cells miss the edge, mode 3
puts pieces on a lattice with the weight falling with the distance from
the centre, mode 4 is small with integer coordinates, mode 5 puts most
pieces on the edge itself around a heavy middle."""

import math
import random
import sys

LARGEST = 1000
RADIUS = 100
HEAVIEST = 10000
CENTS = 100
SMALL = 6


def inside(rng, r):
    while True:
        x, y = rng.uniform(-r, r), rng.uniform(-r, r)
        if x * x + y * y <= r * r:
            return x, y


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    r = RADIUS
    pieces = {}
    if mode == 3:
        step = rng.randint(SMALL, SMALL * 2)
        for x in range(-r, r + 1, step):
            for y in range(-r, r + 1, step):
                if x * x + y * y <= r * r:
                    pieces[(str(x), str(y))] = HEAVIEST - int(math.hypot(x, y) * (HEAVIEST - 1) / r)
    elif mode == 4:
        r = rng.randint(2, SMALL)
        k = rng.randint(2, SMALL)
        while len(pieces) < k:
            x, y = rng.randint(-r, r), rng.randint(-r, r)
            if x * x + y * y <= r * r:
                pieces[(str(x), str(y))] = rng.randint(1, SMALL)
    elif mode == 5:
        pieces[("0", "0")] = HEAVIEST
        while len(pieces) < LARGEST:
            angle = rng.uniform(0, 2 * math.pi)
            x, y = r * math.cos(angle), r * math.sin(angle)
            # rounded inwards so that the piece stays on the table
            x, y = math.trunc(x * CENTS) / CENTS, math.trunc(y * CENTS) / CENTS
            pieces[("%.2f" % x, "%.2f" % y)] = rng.randint(1, HEAVIEST - 1)
    else:
        while len(pieces) < LARGEST:
            x, y = inside(rng, r - 1)
            key = ("%.2f" % x, "%.2f" % y)
            if mode == 2:
                pieces[key] = HEAVIEST - int(math.hypot(x, y) * (HEAVIEST - 1) / r)
            else:
                pieces[key] = rng.randint(1, HEAVIEST)
    print(r, len(pieces))
    for (x, y), w in pieces.items():
        print(x, y, w)


main()
