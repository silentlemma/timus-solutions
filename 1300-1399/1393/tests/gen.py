"""Strings of 250 000 capital letters: a seed and a mode. Mode 1 is
random, mode 2 is one letter, mode 3 is one letter but the last, mode 4
is a Fibonacci word, mode 5 repeats a random word of 7 letters, mode 6
uses two letters only, mode 7 repeats a random half."""

import random
import string
import sys

N = 250000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        text = "".join(rng.choice(string.ascii_uppercase) for _ in range(N))
    elif mode == 2:
        text = "Q" * N
    elif mode == 3:
        text = "A" * (N - 1) + "B"
    elif mode == 4:
        a, b = "A", "AB"
        while len(b) < N:
            a, b = b, b + a
        text = b[:N]
    elif mode == 5:
        word = "".join(rng.choice(string.ascii_uppercase) for _ in range(7))
        text = (word * N)[:N]
    elif mode == 6:
        text = "".join(rng.choice("XY") for _ in range(N))
    else:
        half = "".join(rng.choice("ABC") for _ in range(N // 2))
        text = half * 2
    print(N)
    print(text)


main()
