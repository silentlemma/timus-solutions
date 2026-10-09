"""A random table: a seed, N and the share of plus signs in percent."""

import random
import sys

PERCENT = 100


def main():
    seed, n, share = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    size = 2 * n + 1
    rows = [
        "".join("+" if rng.randrange(PERCENT) < share else "-" for _ in range(size))
        for _ in range(size)
    ]
    sys.stdout.write("\n".join([str(n)] + rows) + "\n")


if __name__ == "__main__":
    main()
