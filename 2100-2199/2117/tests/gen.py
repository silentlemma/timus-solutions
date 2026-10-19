"""C from a seed: mode 1 a random C up to 10^18, mode 2 a square of a large
prime times a small number, mode 3 a product of small squares, mode 4 a
product of two different large primes."""

import random
import sys

TOP = 10 ** 18
LARGE = [999983, 1000003, 999979, 1000033]
SMALL = 30


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        c = rng.randint(0, TOP)
    elif mode == 2:
        p = rng.choice(LARGE)
        c = p * p * rng.randint(1, TOP // (p * p))
    elif mode == 3:
        c = 1
        while True:
            k = rng.randint(2, SMALL)
            if c * k * k > TOP:
                break
            c *= k * k
    else:
        p, q = rng.sample(LARGE, 2)
        c = p * q * rng.randint(1, SMALL)
    print(c)


main()
