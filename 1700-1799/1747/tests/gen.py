"""One test from a seed and a mode: mode 1 a random n and modulus, mode 2
the largest n with a modulus made of small primes, mode 3 a small n."""

import random
import sys

LARGEST = 10 ** 5
MODULUS = 10 ** 9 + 7
SMALL_PRIMES = (2, 3, 5, 7)
SMALL = 30


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        n, p = LARGEST, 1
        while True:
            factor = rng.choice(SMALL_PRIMES)
            if p * factor > MODULUS:
                break
            p *= factor
    else:
        n = rng.randint(3, SMALL if mode == 3 else LARGEST)
        p = rng.randint(1, MODULUS)
    print(n, p)


main()
