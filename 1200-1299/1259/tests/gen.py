"""N: a seed and a mode. Mode 1 draws any N, mode 2 a product of small
primes, mode 3 a prime power."""

import random
import sys

TOP = 100000
PRIMES = [2, 3, 5, 7, 11, 13, 17]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(3, TOP)
    elif mode == 2:
        n = 1
        while n < 3:
            n = 1
            for p in rng.sample(PRIMES, rng.randint(2, len(PRIMES))):
                if n * p <= TOP:
                    n *= p
    else:
        p = rng.choice(PRIMES)
        n = p
        while n * p <= TOP and rng.random() < 0.8:
            n *= p
        n = max(n, 4)
    sys.stdout.write("%d\n" % n)


if __name__ == "__main__":
    main()
