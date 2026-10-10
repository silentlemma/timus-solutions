"""Random queries a, n with a prime n below 32768 and a not divisible by n:
a seed, K and a mode. Mode 0 takes random primes and numbers, mode 1 the
primes with n - 1 divisible by 2^8 and mostly residues, the hardest case
for Tonelli-Shanks, mode 2 small primes with a larger than n, mode 3 the
largest prime with residues only."""

import random
import sys

LIMIT = 32768
DEEP = 256
SHARE = 0.9


def primes():
    sieve = [True] * LIMIT
    sieve[0] = sieve[1] = False
    for i in range(2, LIMIT):
        if sieve[i]:
            for j in range(i * i, LIMIT, i):
                sieve[j] = False
    return [i for i in range(LIMIT) if sieve[i]]


def residue(rng, p):
    x = rng.randrange(1, p)
    a = x * x % p if p > 2 else 1
    return a + p * rng.randrange((LIMIT - 1 - a) // p + 1)


def other(rng, p):
    while True:
        a = rng.randrange(1, LIMIT)
        if a % p:
            return a


def main():
    seed, k, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    every = primes()
    pool = every
    if mode == 1:
        pool = [p for p in every if (p - 1) % DEEP == 0]
    elif mode == 2:
        pool = every[:10]
    elif mode == 3:
        pool = every[-1:]
    lines = [str(k)]
    for _ in range(k):
        p = rng.choice(pool)
        if mode == 3 or mode == 1 and rng.random() < SHARE:
            a = residue(rng, p)
        else:
            a = other(rng, p)
        lines.append("%d %d" % (a, p))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
