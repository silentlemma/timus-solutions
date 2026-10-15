"""One test from a seed and a mode: mode 1 any radius and angle, mode 2
angles below 0.1 degree, so that the walk has thousands of chords,
mode 3 an angle that divides 180 degrees exactly."""

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
    else:
        a = rng.randint(1, HIGH_A)
    print("%d.%03d %d.%03d" % (r // SCALE, r % SCALE, a // SCALE, a % SCALE))


main()
