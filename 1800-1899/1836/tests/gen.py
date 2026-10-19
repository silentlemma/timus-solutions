"""Many aquariums from a seed and a mode: mode 1 a few small ones, mode
2 the most tests, mostly true planes cut at the bottom, mode 3 the most
tests with the largest sizes and levels, mode 4 the most tests with
random readings and many zeros, mode 5 all 10000 tuples of readings from
0 through 9 in seeded order with random sides."""

import random
import sys

LIMIT = 10000
TOP = 1000000
SMALL = 20


def plane(rng, top):
    # levels of a true plane at the four corners, read as max(0, level)
    f0, f1, f3 = (rng.randint(-top, top) for _ in range(3))
    f2 = f1 + f3 - f0
    return [min(TOP, max(0, v)) for v in (f0, f1, f2, f3)]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        from itertools import product

        readings = list(product(range(10), repeat=4))
        rng.shuffle(readings)
        print(len(readings))
        for levels in readings:
            print(rng.randint(1, TOP), *levels)
        return
    count = rng.randint(1, SMALL) if mode == 1 else LIMIT
    lines = []
    for _ in range(count):
        if mode == 3:
            side, top = rng.randint(TOP // 2, TOP), TOP
        else:
            side, top = rng.randint(1, SMALL), rng.choice((5, 50, TOP))
        if mode == 4:
            levels = [rng.choice((0, 0, rng.randint(1, top))) for _ in range(4)]
        else:
            levels = plane(rng, top)
        lines.append(" ".join(map(str, [side] + levels)))
    print(count)
    print("\n".join(lines))


main()
