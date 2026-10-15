"""One test from a seed and a mode: mode 1 any radius and angle, mode 2
angles below 0.1 degree, so that the walk has thousands of chords,
mode 3 an angle that divides 180 degrees exactly, mode 4 a radius just
below 1000 and a tiny angle that does not divide 180, mode 5 an angle
one thousandth above an interior divisor of 180 degrees."""

import random
import sys

SCALE = 1000
LOW_R, HIGH_R = 1 * SCALE, 1000 * SCALE
HIGH_A = 45 * SCALE
SMALL_A = 100
HALF_TURN = 180 * SCALE


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    r = rng.randint(LOW_R, HIGH_R)
    if mode == 2:
        a = rng.randint(1, SMALL_A)
    elif mode == 3:
        a = rng.choice([d for d in range(1, HIGH_A + 1) if HALF_TURN % d == 0])
    elif mode == 4:
        r = rng.randint(HIGH_R - SCALE + 1, HIGH_R - 1)
        a = rng.choice([7, 11, 13, 17, 19, 23, 29, 31])
    elif mode == 5:
        a = rng.choice([18000, 20000, 22500, 30000, 36000]) + 1
    else:
        a = rng.randint(1, HIGH_A)
    print("%d.%03d %d.%03d" % (r // SCALE, r % SCALE, a // SCALE, a % SCALE))


main()
