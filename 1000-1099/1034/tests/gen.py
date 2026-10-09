"""A random peaceful position of N queens, found by a min-conflicts search;
a seed and N. The queens are listed in random order."""

import random
import sys


def peaceful(rng, n):
    while True:
        col = list(range(n))
        rng.shuffle(col)
        for _ in range(100 * n):
            conflicts = [
                sum(1 for j in range(n) if j != i and abs(col[i] - col[j]) == abs(i - j))
                for i in range(n)
            ]
            bad = [i for i in range(n) if conflicts[i]]
            if not bad:
                return col
            i = rng.choice(bad)
            j = rng.randrange(n)
            col[i], col[j] = col[j], col[i]
            if (
                sum(
                    1
                    for a in (i, j)
                    for b in range(n)
                    if b != a and abs(col[a] - col[b]) == abs(a - b)
                )
                > conflicts[i] + conflicts[j]
            ):
                col[i], col[j] = col[j], col[i]


def main():
    seed, n = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    queens = [(x + 1, c + 1) for x, c in enumerate(peaceful(rng, n))]
    rng.shuffle(queens)
    print("\n".join([str(n)] + ["%d %d" % q for q in queens]))


if __name__ == "__main__":
    main()
