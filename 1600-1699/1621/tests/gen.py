"""One test from a seed and a mode: a quartic with integer coefficients of
absolute value at most 10^6, no real roots and no repeated roots. Mode 1
multiplies two random quadratics without real roots, mode 2 puts a pair of
roots close to the real axis far from the origin, mode 3 takes x^2 + 1
times a quadratic with an extreme coefficient, mode 4 flips the sign of a product."""

import random
import sys

TOP = 10**6


def product(p, q):
    """coefficients of p * q, lowest first"""
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def quadratic(rng, span):
    """b x^2 + c x + d with c^2 < 4 b d and b, d > 0: no real roots"""
    while True:
        b, d = rng.randint(1, span), rng.randint(1, span)
        c = rng.randint(-span, span)
        if c * c < 4 * b * d:
            return [d, c, b]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 2:
            a = rng.randint(100, 999)
            first, second = [a * a + 1, -2 * a, 1], quadratic(rng, 20)
        elif mode == 3:
            first, second = rng.choice([([1, 0, 1], [1, 0, TOP - 1]), ([TOP - 1, 0, 1], [1, 0, 1])])
        else:
            first, second = quadratic(rng, 30), quadratic(rng, 30)
        # equal factors would give repeated roots
        if first == second:
            continue
        p = product(first, second)
        if mode == 4:
            p = [-c for c in p]
        if max(abs(c) for c in p) <= TOP:
            break
    print(" ".join(map(str, p)))


main()
