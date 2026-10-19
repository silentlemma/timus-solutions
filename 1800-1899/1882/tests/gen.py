"""A phone book from a seed and a mode: mode 1 a few short names over a
few letters, 2 as many short names as fit, 3 the chain a, aa, aaa, ...,
4 names sharing long prefixes, 5 random long names, 6 every name of
up to 12 letters over the slow letters s and z; 7 one name using the entire
length budget; 8 the maximum possible number of names, filling the budget;
9 random unequal prefix families including names that are prefixes of others;
10 a deep fork with a terminal prefix and an unrelated last name.
Usage: gen.py SEED MODE [BUDGET]. The optional budget (default 10^5) applies
only to modes 7-10; modes 9 and 10 need at least 32 and 4 respectively.
Names are distinct, sorted, of
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


def boundary_names(rng, mode, budget):
    if not 1 <= budget <= TOTAL:
        raise ValueError("budget must be between 1 and 100000")
    if mode == 7:
        return ["z" * budget]
    if mode == 10:
        if budget < 4:
            raise ValueError("mode 10 needs a budget of at least 4")
        depth = (budget - 2) // 2
        return ["a" * depth, "a" * depth + "z", "z" * (budget - 2 * depth - 1)]
    if mode == 8:
        # Shortest names first maximize their count under a length budget.
        out, total, width = [], 0, 1
        while True:
            for letters in product(string.ascii_lowercase, repeat=width):
                if total + width > budget:
                    out.sort()
                    out[-1] += "z" * (budget - total)
                    return out
                out.append("".join(letters))
                total += width
            width += 1
    if mode != 9 or budget < 32:
        raise ValueError("mode 9 needs a budget of at least 32")
    stems = ["a", "az", "d", "dj", "m", "ms", "p", "sz", "w", "zz"]
    out = set(stems)
    total = sum(map(len, out))
    while True:
        stem = rng.choices(stems, weights=range(1, len(stems) + 1))[0]
        word = stem + "".join(rng.choice(string.ascii_lowercase)
                              for _ in range(rng.randint(1, 10)))
        if word in out:
            continue
        if total + len(word) > budget:
            return out
        out.add(word)
        total += len(word)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (7, 8, 9, 10):
        budget = int(sys.argv[3]) if len(sys.argv) > 3 else TOTAL
        book = sorted(boundary_names(rng, mode, budget))
    else:
        book = sorted(names(rng, mode))
    print(len(book))
    print("\n".join(book))


main()
