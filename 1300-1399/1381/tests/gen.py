"""A rule for 31 values, the largest table: a seed and a mode. Mode 1
gives a random rule, mode 2 one where a flat copies the flat above, mode
3 the largest of a flat and the one above, mode 4 the smallest of a flat
and the one below, mode 5 the rounded down mean of three flats. Mode 6
copies the flat below except for one birth at (below, self, above) =
(0, 30, 30). Mode 7 takes the largest neighbour except on the three
triples of the repeating pattern 1, 15, 30, where each flat loses one.
Mode 8 conserves the total using seeded random transfers between flats.
Mode 9 copies the flat above and adds a seeded random nonnegative gain."""

import random
import sys

TOP = 30


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    transfer = None
    if mode == 8:
        transfer = [
            [rng.randint(0, min(a, TOP - b)) for b in range(TOP + 1)]
            for a in range(TOP + 1)
        ]
    rules = {
        1: lambda i, j, k: rng.randint(0, TOP),
        2: lambda i, j, k: k,
        3: lambda i, j, k: max(j, k),
        4: lambda i, j, k: min(i, j),
        5: lambda i, j, k: (i + j + k) // 3,
        6: lambda i, j, k: i + int((i, j, k) == (0, TOP, TOP)),
        7: lambda i, j, k: j - 1
        if (i, j, k) in ((TOP, 1, TOP // 2), (1, TOP // 2, TOP), (TOP // 2, TOP, 1))
        else max(i, j, k),
        8: lambda i, j, k: j - transfer[j][k] + transfer[i][j],
        9: lambda i, j, k: k + rng.randint(0, TOP - k),
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
