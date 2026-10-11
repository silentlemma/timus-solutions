"""A box and points with distinct coordinates: a seed and a mode. Mode 1
gives a small box with up to 8 points, mode 2 50 random points in a
large box, mode 3 points with many coordinates on the faces of the box,
mode 4 50 points near the main diagonal, mode 5 50 points anywhere up
to 1000, many of them outside a smaller box."""

import random
import sys

SCALE = 100
TOP = 1000 * SCALE - 1  # every side is below 1000
MOST = 50


def show(value):
    return "%d.%02d" % (value // SCALE, value % SCALE)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        sides = [rng.randint(SCALE, TOP // 2) for _ in range(3)]
        print(*(show(s) for s in sides))
        print(MOST)
        axes = [rng.sample(range(0, TOP + 2), MOST) for _ in range(3)]
        for x, y, z in zip(*axes):
            print(show(x), show(y), show(z))
        return
    if mode == 1:
        sides = [rng.randint(1, 3 * SCALE) for _ in range(3)]
        n = rng.randint(1, 8)
    else:
        sides = [rng.randint(TOP // 2, TOP) for _ in range(3)]
        n = MOST
    n = min([n] + [s + 1 for s in sides])
    if mode == 4:
        cut = sorted(rng.sample(range(1, min(sides)), n))
        axes = [[c + rng.randint(0, 2) for c in cut] for _ in range(3)]
        for a in axes:
            rng.shuffle(a[: n // 10])
    else:
        axes = []
        for side in sides:
            values = rng.sample(range(0, side + 1), n)
            if mode == 3:
                # put a third of the points on a face of the box
                for i in range(n // 3):
                    values[i] = rng.choice([0, side])
                values = list(dict.fromkeys(values))
                while len(values) < n:
                    extra = rng.randint(1, side - 1)
                    if extra not in values:
                        values.append(extra)
            rng.shuffle(values)
            axes.append(values)
    print(*(show(s) for s in sides))
    print(n)
    for x, y, z in zip(*axes):
        print(show(x), show(y), show(z))


main()
