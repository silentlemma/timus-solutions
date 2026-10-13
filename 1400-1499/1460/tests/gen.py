"""Batches of 100 sets of four pins: a seed, the coordinate range and a
mode. Mode 1 draws pins anywhere in the range, mode 2 near a square of
random size, mode 3 near a line."""

import random
import sys

TESTS = 100
PINS = 4


def main():
    seed, top, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    lines = [str(TESTS)]
    for _ in range(TESTS):
        pins = set()
        while len(pins) < PINS:
            if mode == 1:
                p = (rng.randint(-top, top), rng.randint(-top, top))
            elif mode == 2:
                r = rng.randint(1, top)
                corner = rng.choice([(-r, -r), (-r, r), (r, -r), (r, r)])
                p = (corner[0] + rng.randint(-1, 1), corner[1] + rng.randint(-1, 1))
            else:
                x = rng.randint(-top, top)
                p = (x, rng.randint(-1, 1))
            if max(abs(p[0]), abs(p[1])) <= top:
                pins.add(p)
        lines += ["%d %d" % p for p in pins] + [""]
    print("\n".join(lines[:-1]))


main()
