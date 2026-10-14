"""One test from a seed and a mode. Mode 1 takes 100000 words over the
letters a to d and 15000 prefixes of them, mode 2 the same with counts
from 1 to 3, mode 3 a few short words and queries, mode 4 queries that
mostly match nothing, mode 5 words of 15 letters over all letters,
mode 6 maximal input with a shared 11-letter stem and repeated queries,
mode 7 random families with exactly 9, 10, or 11 matches each."""

import random
import sys

LARGEST = 100000
QUERIES = 15000
LONGEST = 15
TOP = 10**6
FEW = 10
TIES = 3


def families(rng, mode):
    letters = "abcdefghijklmnopqrstuvwxyz"
    if mode == 6:
        stem = "abcdefghijk"
        words = []
        for number in range(LARGEST):
            suffix = ""
            for _ in range(4):
                suffix = letters[number % 26] + suffix
                number //= 26
            words.append(stem + suffix)
        choices = [stem[:length] for length in range(1, len(stem) + 1)]
        choices += [stem + "a", stem + "az", words[0], words[-1]]
        queries = [choices[i % len(choices)] for i in range(QUERIES)]
        rng.shuffle(queries)
        frequencies = [1, TOP - 1, TOP]
    else:
        words = []
        for i, first in enumerate(letters):
            family = set()
            while len(family) < 9 + i % 3:
                tail = "".join(rng.choice(letters) for _ in range(rng.randint(1, 14)))
                family.add(first + tail)
            words.extend(sorted(family))
        queries = list(letters)
        for _ in range(300):
            word = rng.choice(words)
            queries.append(word[:rng.randint(1, len(word))])
        rng.shuffle(queries)
        frequencies = [1, 2, 3, TOP - 1, TOP]
    rng.shuffle(words)
    print(len(words))
    for word in words:
        print(word, rng.choice(frequencies))
    print(len(queries))
    print("\n".join(queries))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7):
        families(rng, mode)
        return
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
