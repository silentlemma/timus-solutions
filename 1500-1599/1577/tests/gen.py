"""One test from a seed and a mode: two passwords of up to 2000 letters.
Mode 1 uses all 26 letters, mode 2 only a and b, mode 3 two equal
passwords, mode 4 passwords without a common letter, mode 5 short ones."""

import random
import sys

LONGEST = 2000
SHORT = 8
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def word(rng, letters, size):
    return "".join(rng.choice(letters) for _ in range(size))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        a, b = word(rng, LETTERS, LONGEST), word(rng, LETTERS, LONGEST)
    elif mode == 2:
        a, b = word(rng, "ab", LONGEST), word(rng, "ab", LONGEST)
    elif mode == 3:
        a = word(rng, "abc", LONGEST)
        b = a
    elif mode == 4:
        a, b = word(rng, "abc", LONGEST), word(rng, "xyz", LONGEST)
    else:
        a = word(rng, "abc", rng.randint(1, SHORT))
        b = word(rng, "abc", rng.randint(1, SHORT))
    print(a)
    print(b)


main()
