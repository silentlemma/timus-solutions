"""One test from a seed and a mode. Mode 1 takes three random numbers of
1 to 8 digits and a random K, mode 2 the same with K up to 5, mode 3 a
true sum of three 8-digit numbers with a few digits changed, mode 4 a
true sum with a few digits changed and K up to 10, mode 5 numbers made
of one repeated digit."""

import random
import sys

LONGEST = 8
TOP_K = 100
SMALL_K = 5
MEDIUM_K = 10
CHANGES = 3


def number(rng, length):
    low = 0 if length == 1 else 10 ** (length - 1)
    return str(rng.randint(low, 10**length - 1))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    k = rng.randint(0, TOP_K)
    if mode in (1, 2):
        text = "+".join(number(rng, rng.randint(1, LONGEST)) for _ in range(2))
        text += "=" + number(rng, rng.randint(1, LONGEST))
        if mode == 2:
            k = rng.randint(0, SMALL_K)
    elif mode in (3, 4):
        if mode == 3:
            low = 10 ** (LONGEST - 1)
            x = rng.randint(low, 10**LONGEST - 1 - low)
            y = rng.randint(low, 10**LONGEST - 1 - x)
        else:
            length = rng.randint(1, LONGEST - 1)
            x, y = int(number(rng, length)), int(number(rng, length))
        chars = list("%d+%d=%d" % (x, y, x + y))
        for _ in range(rng.randint(1, CHANGES)):
            i = rng.randrange(len(chars))
            if chars[i].isdigit():
                chars[i] = str(rng.randint(1, 9))
        text = "".join(chars)
        if mode == 4:
            k = rng.randint(0, MEDIUM_K)
    else:
        digit = str(rng.randint(0, 9))
        lengths = [rng.randint(1, LONGEST) for _ in range(3)]
        if digit == "0":
            lengths = [1, 1, 1]
        text = digit * lengths[0] + "+" + digit * lengths[1] + "=" + digit * lengths[2]
    print(text)
    print(k)


main()
