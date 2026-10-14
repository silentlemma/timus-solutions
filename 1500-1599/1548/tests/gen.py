"""A picture of N x M pixels where the black pixels of every column form at
most one run, from a seed and a mode. Mode 1 draws runs at random, mode 2
makes a few bands of equal runs, mode 3 makes nested runs that grow and
shrink like hills, mode 4 a sparse picture of short runs. Sizes are 50."""

import random
import sys

SIZE = 50
BANDS = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = m = SIZE
    runs = []
    if mode == 1:
        for _ in range(m):
            a = rng.randrange(n)
            runs.append((a, rng.randrange(a, n)) if rng.random() < 0.9 else None)
    elif mode == 2:
        shapes = []
        for _ in range(BANDS):
            a = rng.randrange(n)
            shapes.append((a, rng.randrange(a, n)))
        runs = [rng.choice(shapes) for _ in range(m)]
    elif mode == 3:
        height = rng.randrange(n // 2)
        for _ in range(m):
            height = max(0, min(n // 2 - 1, height + rng.choice((-2, -1, 0, 1, 2))))
            runs.append((n // 2 - 1 - height, n // 2 + height))
    else:
        for _ in range(m):
            a = rng.randrange(n)
            runs.append((a, min(n - 1, a + rng.randrange(3))) if rng.random() < 0.4 else None)
    rows = [["0"] * m for _ in range(n)]
    for col, run in enumerate(runs):
        if run:
            for r in range(run[0], run[1] + 1):
                rows[r][col] = "1"
    print(n, m)
    print("\n".join("".join(r) for r in rows))


main()
