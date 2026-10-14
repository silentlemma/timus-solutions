"""One test from a seed and a mode. Mode 1 takes 100000 words over the
letters a to d and 15000 prefixes of them, mode 2 the same with counts
from 1 to 3, mode 3 a few short words and queries, mode 4 queries that
mostly match nothing, mode 5 words of 15 letters over all letters."""

import random
import sys

LARGEST = 100000
QUERIES = 15000
LONGEST = 15
TOP = 10**6
FEW = 10
TIES = 3


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    small = mode == 3
    letters = "abcdefghijklmnopqrstuvwxyz" if mode in (4, 5) else ("ab" if small else "abcd")
    n = rng.randint(1, FEW) if small else LARGEST
    m = rng.randint(1, FEW) if small else QUERIES
    words = set()
    while len(words) < n:
        length = LONGEST if mode == 5 else rng.randint(1, 4 if small else LONGEST)
        candidate = "".join(rng.choice(letters) for _ in range(length))
        words.add(candidate)
    words = sorted(words)
    rng.shuffle(words)
    top = TIES if mode == 2 else TOP
    lines = ["%s %d" % (w, rng.randint(1, top)) for w in words]
    queries = []
    for _ in range(m):
        if mode == 4 and rng.random() < 0.9:
            queries.append("".join(rng.choice(letters) for _ in range(rng.randint(1, LONGEST))))
        else:
            w = rng.choice(words)
            queries.append(w[: rng.randint(1, len(w))])
    print(len(lines))
    print("\n".join(lines))
    print(m)
    print("\n".join(queries))


main()
