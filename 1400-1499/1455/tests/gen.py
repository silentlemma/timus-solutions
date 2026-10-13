"""Dictionaries: a seed, N, the longest word, the alphabet size and a mode.
Mode 1 draws random different words, mode 2 is the prefix code a^i b, mode
3 the suffix code b a^i (both have no ambiguous text). Mode 4 draws random
different words all of the longest length. Mode 5 draws random different
words with lengths from longest - 2 to longest, with a minimum of 1.
Modes 4 and 5 sort before shuffling for independence from hash randomization."""

import random
import string
import sys


def main():
    seed, n, longest, letters, mode = (int(a) for a in sys.argv[1:6])
    rng = random.Random(seed)
    if mode == 1:
        alphabet = string.ascii_lowercase[:letters]
        words = set()
        while len(words) < n:
            words.add("".join(rng.choice(alphabet) for _ in range(rng.randint(1, longest))))
        words = list(words)
    elif mode == 2:
        words = ["a" * i + "b" for i in range(n)]
    elif mode in (4, 5):
        alphabet = string.ascii_lowercase[:letters]
        shortest = longest if mode == 4 else max(1, longest - 2)
        words = set()
        while len(words) < n:
            size = rng.randint(shortest, longest)
            words.add("".join(rng.choice(alphabet) for _ in range(size)))
        words = sorted(words)
    else:
        words = ["b" + "a" * i for i in range(n)]
    rng.shuffle(words)
    print(n)
    print("\n".join(words))


main()
