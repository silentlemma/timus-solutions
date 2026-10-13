"""One test from a seed and a mode, a polynomial of degree up to 5 with
coefficients in [-100, 100]. Mode 1 takes random coefficients of degree
5, mode 2 multiplies linear factors q x - p with repeats, mode 3 squares
a quadratic with two irrational roots, mode 4 multiplies quadratics
with irrational or no real roots by linear ones, mode 5 takes random
small coefficients of a random degree. Products are redrawn until every
coefficient fits."""

import random
import sys

LIMIT = 100
DEGREE = 5
SMALL = 3


def times(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def linear(rng):
    return [rng.randint(1, SMALL), rng.randint(-LIMIT // 10, LIMIT // 10)]


def irrational_quadratic(rng):
    while True:
        b, d = rng.randint(-SMALL * 2, SMALL * 2), rng.randint(-SMALL * 3, SMALL * 3)
        disc = b * b - 4 * d
        if disc > 0 and round(disc**0.5) ** 2 != disc:
            return [1, b, d]


def draw(rng, mode):
    if mode == 1:
        coeffs = [rng.randint(-LIMIT, LIMIT) for _ in range(DEGREE + 1)]
        coeffs[0] = coeffs[0] or 1
        return coeffs
    if mode == 5:
        degree = rng.randint(1, DEGREE)
        coeffs = [rng.randint(-SMALL, SMALL) for _ in range(degree + 1)]
        coeffs[0] = coeffs[0] or 1
        return coeffs
    if mode == 2:
        factors = []
        while len(factors) < DEGREE:
            factor = linear(rng)
            factors += [factor] * rng.randint(1, DEGREE - len(factors))
    elif mode == 3:
        quad = irrational_quadratic(rng)
        factors = [quad, quad, linear(rng)]
    else:
        factors = [irrational_quadratic(rng), [1, 0, rng.randint(1, SMALL)], linear(rng)]
    poly = [rng.choice([-1, 1])]
    for factor in factors:
        poly = times(poly, factor)
    return poly


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        poly = draw(rng, mode)
        if max(abs(c) for c in poly) <= LIMIT:
            break
    print(len(poly) - 1)
    print("\n".join(map(str, poly)))


main()
