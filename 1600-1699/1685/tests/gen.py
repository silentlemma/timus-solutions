"""One test from a seed and a mode: mode 1 a short text, mode 2 the
longest text, mode 3 a long text with spaces at both ends, mode 4 a text
of distinct-looking runs of one letter."""

import random
import string
import sys

LONGEST = 20000
ALPHABET = string.ascii_letters + " .,!?-:;"


def encode(text):
    """The father's way: the middle letter, then the left part, then the
    right part."""
    out = []
    stack = [(0, len(text) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo <= hi:
            mid = (lo + hi) // 2
            out.append(text[mid])
            stack.append((mid + 1, hi))
            stack.append((lo, mid - 1))
    return "".join(out)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        text = "".join(rng.choice(ALPHABET) for _ in range(rng.randint(1, 30)))
    elif mode == 2:
        text = "".join(rng.choice(ALPHABET) for _ in range(LONGEST))
    elif mode == 3:
        text = " " + "".join(rng.choice(ALPHABET) for _ in range(LONGEST - 2)) + " "
    else:
        text = "".join(rng.choice("ab") * rng.randint(1, 50) for _ in range(LONGEST))[:LONGEST]
    print(encode(text))


main()
