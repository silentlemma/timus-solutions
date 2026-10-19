"""A text from a seed and a mode: mode 1 a few short words on narrow
lines, 2 the most words of random length, 3 the most one-letter words on
the widest lines, 4 words exactly as long as a line, 5 words that fill
lines exactly with single spaces. Words use Latin letters and the marks
. , ! ?, and their total length stays within 10 000."""

import random
import string
import sys

MOST = 10000
WIDEST = 100
FEW = 8
CHARS = string.ascii_letters + ".,!?"


def word(rng, length):
    return "".join(rng.choice(CHARS) for _ in range(length))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    h = rng.randint(1, WIDEST)
    if mode == 1:
        w, n = rng.randint(1, FEW), rng.randint(1, FEW)
        lengths = [rng.randint(1, w) for _ in range(n)]
    elif mode == 2:
        w = rng.randint(1, WIDEST)
        lengths = []
        while sum(lengths) < MOST - w:
            lengths.append(rng.randint(1, w))
    elif mode == 3:
        w, lengths = WIDEST, [1] * MOST
    elif mode == 4:
        w = rng.randint(1, WIDEST)
        lengths = [w] * (MOST // w)
    else:
        w = rng.randint(2, WIDEST)
        lengths = []
        while sum(lengths) + w < MOST:
            cut = rng.randint(1, w - 1) if w > 2 else 1
            first = max(1, min(cut, w - 2))
            lengths += [first, w - 1 - first] if w - 1 - first > 0 else [w]
    words = [word(rng, k) for k in lengths]
    print(h, w, len(words))
    print("\n".join(words))


main()
