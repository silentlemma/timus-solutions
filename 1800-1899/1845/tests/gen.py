"""One matrix and modulus from a seed and a mode: mode 1 a small random
matrix with small numbers, 2 the largest random matrix and modulus, 3 the
largest matrix with two equal rows, so the determinant is 0, 4 the
largest matrix with a unit modulus, 5 the largest matrix with a real
modulus, 6 the largest matrix with a modulus that is a multiple of 1 + i
and of an integer, 7 the largest sparse matrix, where pivots are often
zero, 8 the largest matrix of real numbers."""

import random
import sys

MOST = 50
LIMIT = 10000
SMALL = 5
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else MOST
    top = SMALL if mode == 1 else LIMIT

    def entry():
        if mode == 7 and rng.random() < 0.9:
            return 0, 0
        return rng.randint(-top, top), 0 if mode == 8 else rng.randint(-top, top)

    rows = [[entry() for _ in range(n)] for _ in range(n)]
    if mode == 3:
        a, b = rng.sample(range(n), 2)
        rows[a] = list(rows[b])
    p = (0, 0)
    while p == (0, 0):
        p = (rng.randint(-top, top), rng.randint(-top, top))
    if mode == 4:
        p = rng.choice(UNITS)
    elif mode == 5:
        p = (rng.randint(LIMIT // 2, LIMIT), 0)
    elif mode == 6:
        g = rng.randint(2, LIMIT // 2)
        p = (g, g)
    print(n)
    for row in rows:
        print(" ".join("%d %d" % x for x in row))
    print(*p)


main()
