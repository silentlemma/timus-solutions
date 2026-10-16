"""One test from a seed and a mode: mode 1 any n up to 10^9, mode 2 a
product of small primes with many divisors, mode 3 a power of a prime."""

import random
import sys

LIMIT = 10 ** 9
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, LIMIT)
    elif mode == 2:
        n = 1
        while True:
            p = rng.choice(SMALL_PRIMES)
            if n * p > LIMIT:
                break
            n *= p
    else:
        p = rng.choice(SMALL_PRIMES)
        n = p
        while n * p <= LIMIT and rng.random() < 0.9:
            n *= p
    print(max(n, 2))


main()
