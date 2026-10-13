"""One test from a seed and a mode: a random triangulation of the polygon
is built by splitting vertex intervals, and part of its diagonals are
given. Mode 1 is 50000 vertices with half the cuts given, mode 2 with
none, mode 3 with all, mode 4 is a fan of cuts from one vertex, mode 5
is a small polygon."""

import random
import sys

LARGEST = 50000
SMALL = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(3, SMALL) if mode == 5 else LARGEST
    if mode == 4:
        cuts = [(1, v) for v in range(3, n)]
    else:
        cuts = []
        stack = [(1, n)]
        while stack:
            a, b = stack.pop()
            if b - a < 2:
                continue
            c = rng.randint(a + 1, b - 1)
            for lo, hi in ((a, c), (c, b)):
                if hi - lo >= 2:
                    cuts.append((lo, hi))
                    stack.append((lo, hi))
    share = {1: 0.5, 2: 0.0, 3: 1.0, 4: 0.5, 5: rng.random()}[mode]
    given = [c if rng.random() < 0.5 else c[::-1] for c in cuts if rng.random() < share]
    rng.shuffle(given)
    print(n)
    print(len(given))
    for a, b in given:
        print(a, b)


main()
