"""Texts of 100 000 characters: a seed and a mode. Mode 1 is random
letters and spaces with rare punctuation, N 7 and M 160, mode 2 random
characters of every allowed kind, mode 3 one long run of letters with
N 1 and M 10 000, mode 4 punctuation every few letters."""

import random
import string
import sys

L = 100000
GOOD = string.ascii_letters + " "
BAD = string.digits + '.,;:!?-"'


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = 7, 160
        text = "".join(
            rng.choice(BAD) if rng.random() < 0.002 else rng.choice(GOOD) for _ in range(L)
        )
    elif mode == 2:
        n, m = rng.randint(1, 50), rng.randint(50, 200)
        text = "".join(rng.choice(GOOD + BAD) for _ in range(L))
    elif mode == 3:
        n, m = 1, 10000
        text = "".join(rng.choice(GOOD) for _ in range(L))
    else:
        n, m = 3, 11
        text = "".join(rng.choice(BAD) if i % rng.randint(4, 15) == 0 else "a" for i in range(L))
    print(n, m)
    print(text)


main()
