"""One pair of rings from a seed and a mode: mode 1 any radii and
distance, mode 2 small radii close together, mode 3 a distance equal
to a sum or difference of two radii, so circles touch."""

import random
import sys

LIMIT = 15000
SMALL = 40


def ring(rng, top):
    inner = rng.randint(1, top - 1)
    return inner, rng.randint(inner + 1, top)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 2 else LIMIT
    r1, big1 = ring(rng, top)
    r2, big2 = ring(rng, top)
    if mode == 3:
        a, b = rng.choice((r1, big1)), rng.choice((r2, big2))
        options = [abs(a - b)] + ([a + b] if a + b <= LIMIT else [])
        d = rng.choice(options)
    else:
        d = rng.randint(0, 2 * top if mode == 2 else LIMIT)
    print(d, r1, big1, r2, big2)


main()
