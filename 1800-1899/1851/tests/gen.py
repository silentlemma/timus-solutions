"""A string and a pattern from a seed and a mode: mode 1 short ones,
2 the longest string with a pattern of half its length and every third
character erased, 3 the longest string and pattern of equal length,
4 the longest string with a pattern of one character, 5 almost every
character erased, 6 erased characters in long runs."""

import random
import sys

MOST = 1000
SMALL = 8


def word(rng, length, erased):
    return "".join("?" if rng.random() < erased else rng.choice("01") for _ in range(length))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL)
        m = rng.randint(1, n)
        s, p = word(rng, n, 0.4), word(rng, m, 0.4)
    elif mode == 6:
        s = "".join(rng.choice(("?" * 50, "01" * 25, "1" * 50, "0" * 50)) for _ in range(20))
        p = "".join(rng.choice(("?" * 50, "10" * 25, "0" * 50)) for _ in range(10))
    else:
        m = {2: MOST // 2, 3: MOST, 4: 1}.get(mode, MOST // 2)
        erased = 0.95 if mode == 5 else 1 / 3
        s, p = word(rng, MOST, erased), word(rng, m, erased)
    print(s)
    print(p)


main()
