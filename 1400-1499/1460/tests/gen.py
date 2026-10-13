"""Batches of 100 sets of four pins: seed, coordinate range, mode.

Mode 1: uniform random pins.
Mode 2: pins near corners of squares.
Mode 3: pins near a horizontal line.
Mode 4: acute triangles with a fourth pin strictly inside.
Mode 5: slanted parallelograms with nonperpendicular sides.
Mode 6: trapezoids with a unit top edge and a wide base.
Mode 7: one pin on each board edge, excluding the corners.
"""

import random
import sys

TESTS = 100
PINS = 4


def structured(rng, top, mode):
    if mode == 4:
        r = rng.randint(3, top)
        y = rng.randint(-r + 1, r - 2)
        width = (r - y - 1) // 2
        x = rng.randint(-width, width)
        pins = [(-r, -r), (r, -r), (0, r), (x, y)]
    elif mode == 5:
        while True:
            ux, uy = rng.randint(1, top // 2), rng.randint(1, top // 2)
            vx, vy = rng.randint(-top // 2, top // 2), rng.randint(1, top // 2)
            if ux * vy != uy * vx and ux * vx + uy * vy != 0:
                break
        pins = [(-ux - vx, -uy - vy), (ux - vx, uy - vy),
                (ux + vx, uy + vy), (-ux + vx, -uy + vy)]
    elif mode == 6:
        r, h = rng.randint(2, top), rng.randint(1, top)
        x = rng.randint(-r, r - 1)
        pins = [(-r, -h), (r, -h), (x, h), (x + 1, h)]
    elif mode == 7:
        pins = [(-top, rng.randint(1 - top, top - 1)),
                (rng.randint(1 - top, top - 1), top),
                (top, rng.randint(1 - top, top - 1)),
                (rng.randint(1 - top, top - 1), -top)]
    else:
        raise ValueError('unknown structured mode')
    rng.shuffle(pins)
    return pins


def main():
    seed, top, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    lines = [str(TESTS)]
    for _ in range(TESTS):
        if mode in (4, 5, 6, 7):
            pins = structured(rng, top, mode)
            lines += ["%d %d" % p for p in pins] + [""]
            continue
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
