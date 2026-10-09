"""Queries: a seed, how many, the largest n and the order (0 random, 1 every
n from the largest down to 1, ignoring the count)."""

import random
import sys

RANDOM, ALL = 0, 1


def main():
    seed, k, top, order = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if order == ALL:
        queries = list(range(top, 0, -1))
    else:
        queries = [rng.randint(1, top) for _ in range(k)]
    sys.stdout.write("\n".join(map(str, [len(queries)] + queries)) + "\n")


if __name__ == "__main__":
    main()
