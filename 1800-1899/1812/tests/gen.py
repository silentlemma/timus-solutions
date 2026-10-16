"""One test from a seed and a mode: radii, a number of rounds and a
circle. Mode 1 radii g p^2 and g q^2, so the inner radii are rational,
mode 2 any radii, mode 3 rational radii after 30 rounds."""

import random
import sys

LIMIT = 1000
ROUNDS = 30
SMALL = 5
SHARE = 30


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        r1, r2 = rng.randint(1, LIMIT), rng.randint(1, LIMIT)
    else:
        while True:
            g = rng.randint(1, SHARE)
            p, q = rng.randint(1, SMALL), rng.randint(1, SMALL)
            r1, r2 = g * p * p, g * q * q
            if max(r1, r2) <= LIMIT:
                break
    n = ROUNDS if mode == 3 else rng.randint(0, ROUNDS)
    print(r1, r2, n, rng.randint(1, 2 ** n + 1))


main()
