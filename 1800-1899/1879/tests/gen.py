"""Two partial strings from a seed and a mode: mode 1 short strings over
a few letters, 2 the longest strings over the whole alphabet, 3 the
longest strings over a few letters with many question marks, 4 only
question marks, 5 no question marks, 6 the longest strings where the
most common letters of s and t differ, 7 maximum equal lengths with
disjoint constant letters, 8 maximum s and singleton t with one blank,
9 near-maximum lengths over sparse letters with one blank in each.
The string t is never longer than s."""

import random
import sys

LONGEST = 100000
LETTERS = 100000
FEW = 6


def word(rng, length, alphabet, blanks):
    return [0 if rng.random() < blanks else rng.choice(alphabet) for _ in range(length)]


def targeted(rng, mode):
    if mode == 7:
        return [1] * LONGEST, [LETTERS] * LONGEST
    if mode == 8:
        s = [rng.choice([1, LETTERS - 1, LETTERS]) for _ in range(LONGEST)]
        s[rng.randrange(len(s))] = 0
        return s, [LETTERS]
    if mode == 9:
        alphabet = [1, 17, LETTERS - 1, LETTERS]
        s = [rng.choice(alphabet) for _ in range(LONGEST)]
        t = [rng.choice(alphabet) for _ in range(LONGEST - 1)]
        s[rng.randrange(len(s))] = 0
        t[rng.randrange(len(t))] = 0
        return s, t
    raise ValueError("unknown targeted mode")


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (7, 8, 9):
        s, t = targeted(rng, mode)
        print(len(s))
        print(*s)
        print(len(t))
        print(*t)
        return
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
