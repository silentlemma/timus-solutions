"""An odd number from a seed and a mode: mode 1 a small odd number,
2 a large prime, 3 the square of a large prime, 4 the product of two
large primes, 5 a product of many small primes, 6 the square of a large
prime times small primes, 7 the largest allowed number."""

import random
import sys

LIMIT = 10 ** 18 - 1
WITNESSES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def prime(n):
    if n < 2:
        return False
    for p in WITNESSES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1
    for a in WITNESSES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def random_prime(rng, low, high):
    while True:
        p = rng.randrange(low, high) | 1
        if prime(p):
            return p


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randrange(1, 10 ** 5, 2)
    elif mode == 2:
        n = random_prime(rng, LIMIT // 2, LIMIT)
    elif mode == 3:
        n = random_prime(rng, 10 ** 8, 10 ** 9) ** 2
    elif mode == 4:
        n = random_prime(rng, 10 ** 8, 10 ** 9) * random_prime(rng, 10 ** 8, 10 ** 9)
    elif mode == 5:
        n = 1
        while True:
            p = rng.choice((3, 5, 7, 11, 13, 17, 19, 23))
            if n * p > LIMIT:
                break
            n *= p
    elif mode == 6:
        n = random_prime(rng, 10 ** 6, 10 ** 7) ** 2
        while n * 9 <= LIMIT:
            n *= rng.choice((3, 5, 7))
    else:
        n = LIMIT
    print(n)


main()
