"""One test from a seed and a mode: 100 values of m. Mode 1 any m below
10^9, mode 2 products of a few small primes and their powers, mode 3
squares of large primes and large primes."""

import random
import sys

TESTS = 100
LIMIT = 10 ** 9
SMALL_PRIMES = [2, 3, 5, 7, 11, 13]


def is_prime(v):
    d = 2
    while d * d <= v:
        if v % d == 0:
            return False
        d += 1
    return v > 1


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    values = []
    while len(values) < TESTS:
        if mode == 1:
            m = rng.randint(2, LIMIT - 1)
        elif mode == 2:
            m = 1
            while True:
                p = rng.choice(SMALL_PRIMES)
                if m * p >= LIMIT:
                    break
                m *= p
                if rng.random() < 0.1:
                    break
        else:
            p = rng.randint(2, 31622)
            if not is_prime(p):
                continue
            m = p * p if rng.random() < 0.5 else p * rng.randint(1, (LIMIT - 1) // p)
        if 1 < m < LIMIT:
            values.append(m)
    print("\n".join(map(str, values)))


main()
