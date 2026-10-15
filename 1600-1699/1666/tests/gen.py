"""One test from a seed and a mode: mode 1 random coefficients, mode 2 a
product of two quadratics, mode 3 a product of four linear factors, mode 4
two linear factors times a quadratic, mode 5 a squared quadratic. All
coefficients stay within 20000."""

import random
import sys

LIMIT = 20000


def multiply(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i + j] += x * y
    return out


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            poly = [1] + [rng.randint(-LIMIT, LIMIT) for _ in range(4)]
        else:
            span = rng.choice((5, 30, 150))

            def quad():
                return [1, rng.randint(-span, span), rng.randint(-span, span)]

            def line():
                return [1, rng.randint(-span, span)]

            if mode == 2:
                parts = [quad(), quad()]
            elif mode == 3:
                parts = [line() for _ in range(4)]
            elif mode == 4:
                parts = [line(), line(), quad()]
            else:
                q = quad()
                parts = [q, q]
            poly = [1]
            for part in parts:
                poly = multiply(poly, part)
        if all(abs(c) <= LIMIT for c in poly):
            break
    print(*poly[1:])


main()
