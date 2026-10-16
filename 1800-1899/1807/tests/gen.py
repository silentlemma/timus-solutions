"""One test from a seed and a mode: n = boxes times cartridges per box,
at least 2 boxes of at least 100 cartridges and n up to 10^9. Mode 1
any such n, mode 2 the square of a prime, so the smallest prime factor
is as large as possible, mode 3 a prime times a larger number."""

import random
import sys

LIMIT = 10 ** 9
BOX = 100


def is_prime(v):
    if v < 2:
        return False
    d = 2
    while d * d <= v:
        if v % d == 0:
            return False
        d += 1
    return True


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            boxes = rng.randint(2, LIMIT // BOX)
            n = boxes * rng.randint(BOX, LIMIT // boxes)
        elif mode == 2:
            p = rng.randint(BOX, int(LIMIT ** 0.5))
            n = p * p if is_prime(p) else 0
        else:
            p = rng.randint(2, int(LIMIT ** 0.5))
            n = p * rng.randint(p, LIMIT // p) if is_prime(p) else 0
        if n >= 2 * BOX:
            break
    print(n)


main()
