"""Eye, target and mirror: a seed and a mode. Mode 1 draws random points
with six decimals, mode 2 small integers (many rays through an end of
the mirror), mode 3 a ray built to pass exactly through an end of a
mirror on a vertical line, then one coordinate nudged by 10^-6 or left
alone. The answer is left to the reference solution."""

import random
import sys

TOP = 1000
SMALL = 6
STEP = 10**-6


def side(ax, ay, bx, by, px, py):
    return (bx - ax) * (py - ay) - (by - ay) * (px - ax)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            v = [round(rng.uniform(-TOP, TOP), 6) for _ in range(8)]
        elif mode == 2:
            v = [rng.randint(-SMALL, SMALL) for _ in range(8)]
        else:
            # mirror on x = c from y1 to y2; eye at distance d, target at
            # distance d * k on the same side; the image of the target is
            # mirrored, and the ray from the eye meets x = c at y2 exactly
            c, y1 = rng.randint(-100, 100), rng.randint(-100, 100)
            y2 = y1 + rng.randint(1, 100)
            d, k = rng.randint(1, 100), rng.randint(1, 10)
            ey = rng.randint(-100, 100)
            ty = y2 + k * (y2 - ey)
            sign = rng.choice([-1, 1])
            v = [c + sign * d, ey, c + sign * d * k, ty, c, y1, c, y2]
            if rng.random() < 0.5:
                v[rng.randrange(4)] += rng.choice([-1, 1]) * STEP
            v = [round(x, 6) for x in v]
        if (v[4], v[5]) == (v[6], v[7]):
            continue
        if side(*v[4:8], v[0], v[1]) == 0 or side(*v[4:8], v[2], v[3]) == 0:
            continue
        if all(abs(x) <= TOP for x in v):
            break
    text = ["%.6f" % x if mode != 2 else "%d" % x for x in v]
    sys.stdout.write("%s %s\n%s %s\n%s %s\n%s %s\n" % tuple(text))


if __name__ == "__main__":
    main()
