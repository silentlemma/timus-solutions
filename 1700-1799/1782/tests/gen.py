"""One test from a seed and a mode: mode 1 a short word made by random
phrases, kept only when free of the forbidden repeats, mode 2 a piece
of the Thue-Morse word of up to 5000 letters, mode 3 such a piece of
100 000 letters, reversed or with 0 and 1 swapped at random. Pieces of
that word have no overlaps at all, so they are always allowed."""

import random
import sys

FEW_PHRASES = 14
SHORT = 400
MIDDLE = 5000
MOST = 100000
HALF = 0.5
SWAP = str.maketrans("01", "10")


def free(s):
    """No factor with period p as long as 2p + ceil(p / 3)."""
    for p in range(1, len(s) // 2 + 1):
        need = p + -(-p // 3)
        run = 0
        for i in range(len(s) - p):
            run = run + 1 if s[i] == s[i + p] else 0
            if run >= need:
                return False
    return True


def double(s):
    return "".join("01" if c == "0" else "10" for c in s)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        while True:
            s = ""
            for _ in range(rng.randint(1, FEW_PHRASES)):
                pick = rng.random()
                if pick < HALF / 2 and s:
                    s = double(s)
                elif pick < HALF + HALF / 2:
                    s = rng.choice("01") + s
                else:
                    s = s + rng.choice("01")
            if s and len(s) <= SHORT and free(s):
                break
    else:
        word = "0"
        while len(word) < 2 * MOST + 2:
            word = double(word)
        size = rng.randint(1, MIDDLE) if mode == 2 else MOST
        start = rng.randrange(len(word) - size)
        s = word[start:start + size]
        if mode == 3 and rng.random() < HALF:
            s = s[::-1]
        if mode == 3 and rng.random() < HALF:
            s = s.translate(SWAP)
    print(s)


main()
