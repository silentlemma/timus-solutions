"""One test from a seed and a mode: mode 1 a short word over a few
letters, mode 2 4000 letters over two, mode 3 4000 copies of one letter,
mode 4 4000 letters over 26, mode 5 palindromes glued together."""

import random
import sys

LONGEST = 4000
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = "".join(rng.choice("abc") for _ in range(rng.randint(1, 30)))
    elif mode == 2:
        s = "".join(rng.choice("ab") for _ in range(LONGEST))
    elif mode == 3:
        s = rng.choice(LETTERS) * LONGEST
    elif mode == 4:
        s = "".join(rng.choice(LETTERS) for _ in range(LONGEST))
    else:
        s = ""
        while len(s) < LONGEST:
            half = "".join(rng.choice("abc") for _ in range(rng.randint(1, 60)))
            s += half + half[-2::-1] if rng.random() < 0.5 else half + half[::-1]
        s = s[:LONGEST]
    print(s)


main()
