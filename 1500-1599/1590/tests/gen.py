"""One test from a seed and a mode: a string of up to 5000 lowercase
letters. Mode 1 uses all 26 letters, mode 2 only a and b, mode 3 is one
letter repeated, mode 4 a short block repeated, mode 5 a Fibonacci word,
mode 6 a short random string."""

import random
import sys

MOST = 5000
LETTERS = "abcdefghijklmnopqrstuvwxyz"
SHORT = 12


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = "".join(rng.choice(LETTERS) for _ in range(MOST))
    elif mode == 2:
        s = "".join(rng.choice("ab") for _ in range(MOST))
    elif mode == 3:
        s = rng.choice(LETTERS) * MOST
    elif mode == 4:
        block = "".join(rng.choice(LETTERS) for _ in range(rng.randint(2, SHORT)))
        s = (block * MOST)[:MOST]
    elif mode == 5:
        a, b = "a", "ab"
        while len(b) < MOST:
            a, b = b, b + a
        s = b[:MOST]
    else:
        s = "".join(rng.choice("abc") for _ in range(rng.randint(1, SHORT)))
    print(s)


main()
