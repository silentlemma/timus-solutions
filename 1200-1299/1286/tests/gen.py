"""A ship and a target: a seed and a mode. Mode 1 draws everything up to
2 * 10^9 in absolute value, mode 2 steps sharing a factor and targets on
or off its lattice, mode 3 steps that are both odd after dividing by
their gcd."""

import random
import sys

TOP = 2 * 10**9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        p, q = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
        start = (rng.randint(-TOP, TOP), rng.randint(-TOP, TOP))
        goal = (rng.randint(-TOP, TOP), rng.randint(-TOP, TOP))
    else:
        g = rng.randint(1, 1000)
        while True:
            a, b = rng.randint(-1000, 1000), rng.randint(-1000, 1000)
            if mode == 2 or (a % 2 and b % 2):
                break
        p, q = g * a, g * b
        start = (rng.randint(-(10**6), 10**6), rng.randint(-(10**6), 10**6))
        step = (rng.randint(-(10**5), 10**5), rng.randint(-(10**5), 10**5))
        goal = (start[0] + g * step[0] + rng.choice([0, 0, 1]), start[1] + g * step[1])
    sys.stdout.write("%d %d\n%d %d\n%d %d\n" % (p, q, *start, *goal))


if __name__ == "__main__":
    main()
