"""Strings of 250 000 characters: a seed and a mode. Mode 1 rotates a
random string over "ab", mode 2 turns a string of all a's and one b, mode
3 rotates a random string of characters from 128 to 255, mode 4 changes
one character of a rotation so that the answer is -1. The text is
written in UTF-8 and the tests turn it into Latin-1 bytes."""

import random
import sys

N = 250000
HIGH = "".join(map(chr, range(128, 256)))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = "".join(rng.choice("ab") for _ in range(N))
    elif mode == 2:
        s = "a" * (N - 1) + "b"
    elif mode == 3:
        s = "".join(rng.choice(HIGH) for _ in range(N))
    else:
        s = "".join(rng.choice("abc") for _ in range(N))
    x = rng.randrange(N)
    t = list(s[N - x :] + s[: N - x])
    if mode == 4:
        i = rng.randrange(N)
        t[i] = "d"
    print(N)
    print(s)
    print("".join(t))


main()
