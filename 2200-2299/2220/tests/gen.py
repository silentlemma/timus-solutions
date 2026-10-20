"""Generate one valid size: small, medium, random, square, power, smooth,
cutoff, large, max, or fixed (where the seed itself is the size)."""

import math
import random
import sys

MAX_N = 10**7
SMALL_LIMIT = 10**3
MEDIUM_LIMIT = 10**5
LARGE_WINDOW = 10**4
SIEVE_LIMIT = 10**5
NEIGHBOR_RADIUS = 2
PRIMES = (2, 3, 5, 7)
POWER_BASES = PRIMES + (10,)
ARGUMENT_COUNT = 3


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        return rng.randint(1, SMALL_LIMIT)
    if mode == "medium":
        return rng.randint(1, MEDIUM_LIMIT)
    if mode == "random":
        return rng.randint(1, MAX_N)
    if mode == "square":
        root = rng.randint(1, math.isqrt(MAX_N))
        return max(1, min(MAX_N, root * root + rng.choice((-1, 0, 1))))
    if mode == "power":
        base = rng.choice(POWER_BASES)
        powers = [1]
        while powers[-1] * base <= MAX_N:
            powers.append(powers[-1] * base)
        return max(1, min(MAX_N, rng.choice(powers) + rng.choice((-1, 0, 1))))
    if mode == "smooth":
        n = 1
        while True:
            prime = rng.choice(PRIMES)
            if n * prime > MAX_N:
                return n
            n *= prime
    if mode == "cutoff":
        pivot = rng.choice((SIEVE_LIMIT, SIEVE_LIMIT + 1, 2 * (SIEVE_LIMIT + 1)))
        return pivot + rng.randint(-NEIGHBOR_RADIUS, NEIGHBOR_RADIUS)
    if mode == "large":
        return MAX_N - rng.randrange(LARGE_WINDOW)
    if mode == "max":
        return MAX_N
    if mode == "fixed" and 1 <= seed <= MAX_N:
        return seed
    raise ValueError("unknown mode or invalid fixed size")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    print(generate(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
