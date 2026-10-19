"""n from a seed.

Mode 1: a product of 20 random small primes (Yes when it fits). Mode 2: 19
small primes times a large prime. Mode 3: 18 small primes times two large
primes. Mode 4: a random n up to 10^18.
"""

import random
import sys

TOP = 10 ** 18
SMALL_PRIMES = [2, 3, 5, 7]
TARGET = 20
LARGE = [1000003, 999983, 2000003, 1999993, 3000017]
NEAR = [999983, 1000003]  # two of them still fit next to 2^18


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 4:
        print(rng.randint(1, TOP))
        return
    small = TARGET - (mode - 1)
    while True:
        n = 1
        for _ in range(small):
            # mostly twos, so that the product fits
            n *= rng.choice(SMALL_PRIMES) if rng.random() < 0.2 else 2
        for _ in range(mode - 1):
            n *= rng.choice(LARGE if mode == 2 else NEAR)
        if n <= TOP:
            break
    print(n)


main()
