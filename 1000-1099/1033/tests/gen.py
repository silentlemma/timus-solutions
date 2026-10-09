"""A random maze; a seed, N and the percentage of wall cells. The two corner
entrances are always empty."""

import random
import sys

PERCENT = 100


def main():
    seed, n, walls = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    rows = [["#" if rng.randrange(PERCENT) < walls else "." for _ in range(n)] for _ in range(n)]
    rows[0][0] = rows[n - 1][n - 1] = "."
    print("\n".join([str(n)] + ["".join(r) for r in rows]))


if __name__ == "__main__":
    main()
