"""The digits of the first months: a seed and a mode. A random 12-digit
prime is chosen and a random number of its leading digits is given, so
an answer exists. Mode 1 gives any length, mode 2 a long prefix, mode 3
a prefix starting with zeros."""

import random
import sys

DIGITS = 12
BASES = (2, 3, 5, 7, 11, 13)


def is_prime(n):
    if n < 2:
        return False
    for p in BASES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d // 2, s + 1
    for a in BASES:
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


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = 10**6 if mode == 3 else 10**DIGITS
    n = rng.randrange(top)
    while not is_prime(n):
        n = rng.randrange(top)
    count = rng.randint(9, 11) if mode == 2 else rng.randint(0, DIGITS)
    text = str(n).zfill(DIGITS)
    print(count)
    print(text[:count])


main()
