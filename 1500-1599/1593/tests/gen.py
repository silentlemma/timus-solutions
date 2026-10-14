"""One test from a seed and a mode: a number N up to 10^15. Mode 1 is a
random N, mode 2 a product of two primes near the square root of 10^15,
mode 3 a perfect square times a small factor, mode 4 a number of the form
4^a (8b + 7), mode 5 a small N."""

import random
import sys

MOST = 10**15
NEAR = 31622776  # about the square root of 10^15
SMALL = 1000


def prime_near(rng, x):
    while True:
        x += 1
        if x > 1 and all(x % d for d in range(2, int(x**0.5) + 1)):
            if rng.random() < 0.5:
                return x


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, MOST)
    elif mode == 2:
        p = prime_near(rng, rng.randint(NEAR // 2, NEAR - 1000))
        q = prime_near(rng, rng.randint(NEAR // 2, NEAR - 1000))
        n = p * q
    elif mode == 3:
        r = rng.randint(1, NEAR // 3)
        n = r * r * rng.choice([1, 2, 3, 5, 6, 7])
    elif mode == 4:
        n = 8 * rng.randint(0, MOST // 8 // 64) + 7
        n *= 4 ** rng.randint(0, 3)
    else:
        n = rng.randint(1, SMALL)
    print(n)


main()
