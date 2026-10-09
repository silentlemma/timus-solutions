"""Random rows: a seed, N, K and the shape (0 random orders, 1 nearly sorted
rows with a few swaps, 2 every row the same)."""

import random
import sys

RANDOM, NEARLY, SAME = 0, 1, 2


def main():
    seed, n, k, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    base = list(range(1, n + 1))
    rng.shuffle(base)
    rows = []
    for _ in range(k):
        row = list(range(1, n + 1))
        if shape == RANDOM:
            rng.shuffle(row)
        elif shape == NEARLY:
            for _ in range(rng.randint(0, n // 10)):
                i, j = rng.randrange(n), rng.randrange(n)
                row[i], row[j] = row[j], row[i]
        else:
            row = base[:]
        rows.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(["%d %d" % (n, k)] + rows) + "\n")


if __name__ == "__main__":
    main()
