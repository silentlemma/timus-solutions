"""One test from a seed and a mode: mode 1 small with small entries (often
dependent), mode 2 100 x 100 random, mode 3 large but of low rank (rows are
combinations of a few rows), mode 4 large rectangular in either shape,
mode 5 small with repeated, opposite and zero rows."""

import random
import sys

TOP = 100
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(1, 6), rng.randint(1, 6)
        rows = [[rng.randint(-3, 3) for _ in range(n)] for _ in range(m)]
    elif mode == 2:
        n = m = MOST
        rows = [[rng.randint(-TOP, TOP) for _ in range(n)] for _ in range(m)]
    elif mode == 3:
        n, m = rng.randint(60, MOST), rng.randint(60, MOST)
        base = [[rng.randint(-5, 5) for _ in range(n)] for _ in range(rng.randint(1, 8))]
        rows = []
        for _ in range(m):
            coef = [rng.randint(-2, 2) for _ in base]
            rows.append([max(-TOP, min(TOP, sum(c * r[j] for c, r in zip(coef, base))))
                         for j in range(n)])
    elif mode == 4:
        n, m = rng.choice(((MOST, rng.randint(1, 40)), (rng.randint(1, 40), MOST)))
        rows = [[rng.randint(-TOP, TOP) for _ in range(n)] for _ in range(m)]
    else:
        n, m = rng.randint(2, 8), rng.randint(2, 8)
        rows = []
        for _ in range(m):
            pick = rng.random()
            if rows and pick < 0.3:
                rows.append(list(rng.choice(rows)))
            elif rows and pick < 0.5:
                rows.append([-x for x in rng.choice(rows)])
            elif pick < 0.6:
                rows.append([0] * n)
            else:
                rows.append([rng.randint(-TOP, TOP) for _ in range(n)])
    b = [rng.randint(-TOP, TOP) for _ in range(n)]
    print(n, m)
    for row in rows:
        print(*row)
    print(*b)


main()
