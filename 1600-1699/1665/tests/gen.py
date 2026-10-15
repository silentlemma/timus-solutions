"""One test from a seed and a mode: mode 1 any N, mode 2 N = 2^a times a
prime, mode 3 N = 2^a times a product of two primes or times 1, mode 4
large primes and their doubles."""

import random
import sys

TOP = 2 ** 25 - 1
TESTS = 100


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_below(rng, top):
    while True:
        p = rng.randint(3, max(3, top))
        if p % 2 and is_prime(p):
            return p


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    ns = []
    while len(ns) < TESTS:
        if mode == 1:
            n = rng.randint(1, TOP)
        elif mode == 2:
            a = rng.randint(0, 22)
            n = 2 ** a * prime_below(rng, TOP >> a)
        elif mode == 3:
            a = rng.randint(0, 24)
            room = TOP >> a
            if room < 9 or rng.random() < 0.2:
                n = 2 ** a
            else:
                p = prime_below(rng, int(room ** 0.5))
                n = 2 ** a * p * prime_below(rng, room // p)
        else:
            p = prime_below(rng, TOP)
            n = 2 * p if 2 * p <= TOP and rng.random() < 0.5 else p
        if 1 <= n <= TOP:
            ns.append(n)
    print(len(ns))
    print("\n".join(map(str, ns)))


main()
