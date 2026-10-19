"""Sorted distinct words from a seed, total length up to 10^6.

Mode 1: a dozen short words over "ab". Mode 2: all words over "ab" of length up
to 15 and some of length 16. Mode 3: one word of length 10^6. Mode 4: 1000 words
of length 1000 that share a long prefix and a long suffix. Mode 5: random words
of lengths 1 to 8 over the whole alphabet. Mode 6: words a^k b a^j, which share
prefixes and suffixes in many ways.
"""

import itertools
import random
import string
import sys

TOTAL = 10 ** 6
SMALL = 12
SHORT = 7
BINARY = 15
LONG = 1000
SHARED = 450
RANDOM_LENGTH = 8
RUN = 180


def words_for(mode, rng):
    if mode == 1:
        return {"".join(rng.choice("ab") for _ in range(rng.randint(1, SHORT)))
                for _ in range(SMALL)}
    if mode == 2:
        words = set()
        for k in range(1, BINARY + 1):
            words.update("".join(p) for p in itertools.product("ab", repeat=k))
        total = sum(map(len, words))
        while total + BINARY + 1 <= TOTAL:
            w = "".join(rng.choice("ab") for _ in range(BINARY + 1))
            if w not in words:
                words.add(w)
                total += len(w)
        return words
    if mode == 3:
        return {"".join(rng.choice("ab") for _ in range(TOTAL))}
    if mode == 4:
        prefix = "a" * SHARED
        suffix = "b" * SHARED
        words = set()
        while len(words) < LONG:
            middle = "".join(rng.choice("ab") for _ in range(LONG - 2 * SHARED))
            words.add(prefix + middle + suffix)
        return words
    if mode == 5:
        words, total = set(), 0
        while total + RANDOM_LENGTH <= TOTAL:
            w = "".join(rng.choice(string.ascii_lowercase)
                        for _ in range(rng.randint(1, RANDOM_LENGTH)))
            if w not in words:
                words.add(w)
                total += len(w)
        return words
    return {"a" * k + "b" + "a" * j for k in range(RUN) for j in range(RUN)
            if k + j + 1 <= RUN and (k + j) % 2 == 0}


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    words = sorted(words_for(mode, random.Random(seed)))
    sys.stdout.write("%d\n%s\n" % (len(words), "\n".join(words)))


main()
