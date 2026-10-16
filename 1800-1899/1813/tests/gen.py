"""One test from a seed and a mode: 100 values of m. Mode 1 any m below
10^9, mode 2 products of a few small primes and their powers, mode 3
squares and multiples of large primes, mode 4 distinct values in the
upper boundary strip, mode 5 triples around large prime squares, mode 6
products of two distinct primes between 20000 and 31622."""

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
    if mode == 4:
        values = rng.sample(range(LIMIT - 1000, LIMIT - 100), TESTS)
    elif mode == 5:
        primes = [p for p in range(30000, 31623) if is_prime(p)]
        for p in rng.sample(primes, (TESTS + 2) // 3):
            values.extend([p * p - 1, p * p, p * p + 1])
        values = values[:TESTS]
    elif mode == 6:
        primes = [p for p in range(20000, 31623) if is_prime(p)]
        seen = set()
        while len(values) < TESTS:
            p, q = rng.sample(primes, 2)
            m = p * q
            if m not in seen:
                seen.add(m)
                values.append(m)
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
