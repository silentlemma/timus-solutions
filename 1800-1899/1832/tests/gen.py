"""One number of artists from a seed and a mode: mode 1 a random one,
mode 2 a large one with many divisors (its least non-divisor is up to
13, so all 26 colours may be needed), mode 3 a large prime or twice a
prime, mode 4 a large power of two or three."""

import random
import sys

LIMIT = 300000
RICH = [27720, 55440, 83160, 110880, 166320, 221760, 277200, 288288, 294840]
POWERS = [2 ** 18, 3 ** 11, 2 ** 17 * 2, 5 ** 7]


def prime(v):
    return v > 1 and all(v % q for q in range(2, int(v ** 0.5) + 1))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        n = rng.choice(RICH)
    elif mode == 3:
        while True:
            q = rng.randint(LIMIT // 4, LIMIT // 2)
            if prime(q):
                break
        n = q * rng.choice((1, 2))
    elif mode == 4:
        n = rng.choice(POWERS)
    else:
        n = rng.randint(2, LIMIT)
    print(n)


main()
