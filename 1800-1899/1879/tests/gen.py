"""Two partial strings from a seed and a mode: mode 1 short strings over
a few letters, 2 the longest strings over the whole alphabet, 3 the
longest strings over a few letters with many question marks, 4 only
question marks, 5 no question marks, 6 the longest strings where the
most common letters of s and t differ. The string t is never longer
than s."""

import random
import sys

LONGEST = 100000
LETTERS = 100000
FEW = 6


def word(rng, length, alphabet, blanks):
    return [0 if rng.random() < blanks else rng.choice(alphabet) for _ in range(length)]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, FEW)
        m = rng.randint(1, n)
    else:
        n = LONGEST
        m = rng.randint(1, LONGEST)
    if mode == 2:
        alphabet, blanks = range(1, LETTERS + 1), 0.1
    elif mode == 4:
        alphabet, blanks = [1], 1.0
    elif mode == 5:
        alphabet, blanks = range(1, FEW + 1), 0.0
    else:
        alphabet, blanks = range(1, FEW + 1), rng.random()
    s = word(rng, n, alphabet, blanks)
    t = word(rng, m, alphabet, blanks)
    if mode == 6:
        s = [c if c == 0 or rng.random() < 0.5 else 1 for c in s]
        t = [c if c == 0 or rng.random() < 0.5 else 2 for c in t]
    print(n)
    print(*s)
    print(m)
    print(*t)


main()
