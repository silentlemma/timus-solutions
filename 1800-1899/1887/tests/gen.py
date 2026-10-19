"""Coefficients from a seed and a mode: mode 1 a few digits with random
coefficients, 2 the most digits with random coefficients, 3 the most
digits where most factors are always 1, so that the last digits are far
from even, 4 the most digits with small coefficients, often making a last
digit impossible, 5 the most digits with two distinct digit roots per
factor, making nonzero check digits rare."""

import random
import sys

MOST = 25
FEW = 5
TOP = 9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    rows = [[0] * n for _ in range(3)]
    if mode == 5:
        choices = [
            (a, b, c)
            for a in range(1, TOP + 1)
            for b in range(TOP + 1)
            for c in range(TOP + 1)
            if sum((a * x * x + b * x + c) % 11 == 0 for x in range(10)) == 2
        ]
    for i in range(n):
        if mode == 5:
            rows[0][i], rows[1][i], rows[2][i] = rng.choice(choices)
        elif mode == 3 and rng.random() < 0.8:
            # a = b = 0 and c = 1 makes the factor 1 whatever the digit
            rows[0][i], rows[1][i], rows[2][i] = 0, 0, 1
        elif mode == 4:
            rows[0][i], rows[1][i], rows[2][i] = (rng.randint(0, 1) for _ in range(3))
        else:
            rows[0][i], rows[1][i], rows[2][i] = (rng.randint(0, TOP) for _ in range(3))
    print(n)
    for row in rows:
        print(*row)


main()
