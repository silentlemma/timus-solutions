"""One test from a seed and a mode:
1: a few solutions of a few authors.
2: 1000 solutions of 300 authors with long names.
3: 1000 distinct authors with random verdicts across the whole old test range.
"""

import random
import string
import sys

MOST = 1000
AUTHORS = 300
LONGEST = 30
NAME_CHARS = string.ascii_letters + string.digits + "_()[]"
TESTS = 7


def verdict(rng):
    kind = rng.choice(("AC", "CE", "ML", "TL", "WA", "WA", "TL"))
    if kind in ("AC", "CE"):
        return kind
    return "%s %d" % (kind, rng.randint(1, TESTS))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        records = [("[Author_(%04d)]" % i, verdict(rng)) for i in range(MOST)]
        rng.shuffle(records)
        print(MOST)
        for name, result in records:
            print(name, result)
        return
    if mode == 1:
        n, names = rng.randint(1, 8), ["a", "b", "c(1)"]
    else:
        n = MOST
        names = set()
        while len(names) < AUTHORS:
            names.add("".join(rng.choice(NAME_CHARS) for _ in range(rng.randint(1, LONGEST))))
        # no two names may differ only in case
        names = list({w.lower(): w for w in names}.values())
    print(n)
    for _ in range(n):
        print(rng.choice(names), verdict(rng))


main()
