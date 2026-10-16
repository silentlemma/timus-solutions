"""One test from a seed and a mode: mode 1 a small grid and a short
route, mode 2 50 dimensions, 10^5 values, a route of up to 10^9 moves and
a random modulus, mode 3 the same with modulus 1, mode 4 routes of
length 0, mode 5 all parameter maxima with varied distances and a repeated
cell, mode 6 a random moderate grid with a composite modulus sharing a
factor with the number of coordinate values."""

import random
import sys

DIMENSIONS = 50
VALUES = 10 ** 5
MOVES = 10 ** 9
MODULUS = 10 ** 9
POINTS = 50
SMALL = 3
SHORT = 5


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        n, m, d, mod, q = DIMENSIONS, VALUES, MOVES, MODULUS, POINTS
        base = [rng.randrange(m) for _ in range(n)]
        points = [base, base[:], [(x + 1) % m for x in base]]
        for h in range(1, q - 2):
            cell = base[:]
            for i in rng.sample(range(n), h):
                cell[i] = (cell[i] + rng.randrange(1, m)) % m
            points.append(cell)
        print(n, m, d, mod, q)
        for cell in points:
            print(" ".join(map(str, cell)))
        return
    if mode == 6:
        n, m, d = rng.randint(2, 5), rng.randint(2, 4), rng.randint(6, 20)
        mod, q = m * rng.choice([4, 9, 25, 72]), POINTS
        print(n, m, d, mod, q)
        for _ in range(q):
            print(" ".join(str(rng.randrange(m)) for _ in range(n)))
        return
    if mode == 1:
        n, m, d = rng.randint(1, SMALL), rng.randint(2, SMALL), rng.randint(0, SHORT)
        q = rng.randint(2, SMALL + 2)
        mod = rng.randint(1, MODULUS)
    else:
        n, m, q = DIMENSIONS, VALUES, POINTS
        d = 0 if mode == 4 else rng.randint(MOVES // 2, MOVES)
        mod = 1 if mode == 3 else rng.randint(1, MODULUS)
    print(n, m, d, mod, q)
    for _ in range(q):
        print(" ".join(str(rng.randint(0, m - 1)) for _ in range(n)))


main()
