"""A phone book from a seed and a mode: mode 1 a few short names over a
few letters, 2 as many short names as fit, 3 the chain a, aa, aaa, ...,
4 names sharing long prefixes, 5 random long names, 6 every name of
up to 12 letters over the slow letters s and z. Names are distinct, sorted, of
lowercase letters, with total length at most 10^5."""

import random
import string
import sys
from itertools import product

TOTAL = 10 ** 5
FEW = 8
SHORT = 4
LONG = 200
SLOW = "sz"
DEEP = 12


def names(rng, mode):
    if mode == 1:
        alpha = rng.choice(["ab", "adgj", string.ascii_lowercase])
        return {"".join(rng.choice(alpha) for _ in range(rng.randint(1, SHORT)))
                for _ in range(rng.randint(1, FEW))}
    out, total = set(), 0
    if mode == 6:
        return {"".join(bits) for k in range(1, DEEP + 1) for bits in product(SLOW, repeat=k)}
    if mode == 3:
        k = 1
        while total + k <= TOTAL:
            out.add("a" * k)
            total += k
            k += 1
        return out
    stems = ["".join(rng.choice(string.ascii_lowercase) for _ in range(LONG)) for _ in range(SHORT)]
    while True:
        if mode == 2:
            w = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, SHORT)))
        elif mode == 4:
            w = rng.choice(stems)[:rng.randint(1, LONG)] + rng.choice(string.ascii_lowercase)
        else:
            w = "".join(rng.choice("aeiouz") for _ in range(rng.randint(1, LONG)))
        if w in out:
            if mode == 2 and rng.random() < 0.01 and total > TOTAL - LONG:
                return out
            continue
        if total + len(w) > TOTAL:
            return out
        out.add(w)
        total += len(w)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    book = sorted(names(rng, mode))
    print(len(book))
    print("\n".join(book))


main()
