"""A rule for 31 values, the largest table: a seed and a mode. Mode 1
gives a random rule, mode 2 one where a flat copies the flat above, mode
3 the largest of a flat and the one above, mode 4 the smallest of a flat
and the one below, mode 5 the rounded down mean of three flats."""

import random
import sys

TOP = 30


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    rules = {
        1: lambda i, j, k: rng.randint(0, TOP),
        2: lambda i, j, k: k,
        3: lambda i, j, k: max(j, k),
        4: lambda i, j, k: min(i, j),
        5: lambda i, j, k: (i + j + k) // 3,
    }
    s = TOP + 1
    print(TOP)
    for j in range(s):
        for i in range(s):
            row = [rules[mode](i, j, k) for k in range(s)]
            if i == j == 0:
                row[0] = 0  # nothing comes from nothing
            print(*row)


main()
