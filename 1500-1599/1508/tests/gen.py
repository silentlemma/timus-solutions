"""One test from a seed and a mode, with L = 400 unless small. Mode 1 draws
a random picture line and reveals some of its cells, so an answer exists,
mode 2 leaves every cell unknown and packs the groups tightly, mode 3
reveals random cells regardless of the groups, mode 4 is small and
random, mode 5 asks for as many groups as cells, mode 6 has no groups."""

import random
import sys

LARGEST = 400
SMALL = 12


def runs(cells):
    out, run = [], 0
    for black in cells + [False]:
        if black:
            run += 1
        elif run:
            out.append(run)
            run = 0
    return out


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 4 else LARGEST
    if mode == 2:
        groups = []
        room = n + 1
        while room > 2:
            g = rng.randint(1, min(room - 1, SMALL))
            groups.append(g)
            room -= g + 1
        line = "?" * n
    elif mode == 5:
        groups, line = [1] * n, "?" * n
    elif mode == 6:
        groups, line = [], "?" * n
    else:
        density = rng.random()
        cells = [rng.random() < density for _ in range(n)]
        groups = runs(cells)
        shown = rng.random()
        if mode == 1:
            line = "".join(("X" if c else ".") if rng.random() < shown else "?" for c in cells)
        else:
            line = "".join(rng.choice("X.") if rng.random() < shown / 4 else "?" for _ in cells)
    print(n, len(groups))
    print(" ".join(map(str, groups)))
    print(line)


main()
