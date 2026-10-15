"""One test from a seed and a mode: mode 1 any N, mode 2 N = 2^a times a
prime, mode 3 N = 2^a times a product of two primes or times 1, mode 4
large primes and their doubles, mode 5 the largest 100 values shuffled,
mode 6 powers of two times odd squares and their near neighbors, mode 7
powers of two times three distinct odd primes."""

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
    if mode == 5:
        ns = list(range(TOP - TESTS + 1, TOP + 1))
        rng.shuffle(ns)
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
        elif mode == 6:
            a = rng.choice([1, 3, 5, 7])
            room = TOP >> a
            p = prime_below(rng, int((room - 4) ** 0.5))
            n = 2 ** a * (p * p + rng.choice([-4, -2, 0, 2, 4]))
        elif mode == 7:
            a = rng.randint(0, 14)
            primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
            p, q, r = rng.sample(primes, 3)
            n = 2 ** a * p * q * r
        else:
            p = prime_below(rng, TOP)
            n = 2 * p if 2 * p <= TOP and rng.random() < 0.5 else p
        if 1 <= n <= TOP:
            ns.append(n)
    print(len(ns))
    print("\n".join(map(str, ns)))


main()
