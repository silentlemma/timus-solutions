"""One test from a seed and a mode: mode 1 small random coefficients and
amounts, mode 2 coefficients up to 100 and amounts up to 1000, mode 3
like mode 2 with some coefficients or amounts set to zero, mode 4 the
two of them agreeing on worth up to a factor."""

import random
import sys

LOW = 5
COEF = 100
MASS = 1000
ZERO = 0.3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top_c, top_m = (LOW, LOW) if mode == 1 else (COEF, MASS)
    coefs = [rng.randint(0, top_c) for _ in range(4)]
    mass = [rng.randint(0, top_m) for _ in range(2)]
    if mode == 3:
        coefs = [0 if rng.random() < ZERO else c for c in coefs]
        mass = [0 if rng.random() < ZERO else v for v in mass]
    if mode == 4:
        k = rng.randint(1, LOW)
        coefs[0], coefs[1] = rng.randint(0, COEF // LOW), rng.randint(0, COEF // LOW)
        coefs[2], coefs[3] = coefs[0] * k, coefs[1] * k
    print(*coefs)
    print(*mass)


main()
