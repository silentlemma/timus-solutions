"""One test from a seed and a mode, numbers of up to 1000 digits. Mode 1
takes three random numbers of 1000 digits, mode 2 makes C one digit
longer than A and B, mode 3 makes C shorter than A, mode 4 is small,
mode 5 takes A + B = C exactly and then spoils a few digits."""

import random
import sys

LONGEST = 1000
SMALL = 4
SPOILED = 5


def number(rng, length):
    return str(rng.randint(1, 9)) + "".join(str(rng.randint(0, 9)) for _ in range(length - 1))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        lengths = (LONGEST, LONGEST, LONGEST)
    elif mode == 2:
        lengths = (LONGEST - 1, LONGEST - 1 - rng.randint(0, 2), LONGEST)
    elif mode == 3:
        lengths = (LONGEST, rng.randint(1, LONGEST), LONGEST - 1)
    elif mode == 4:
        lengths = tuple(rng.randint(1, SMALL) for _ in range(3))
    else:
        a, b = number(rng, LONGEST - 1), number(rng, LONGEST - 1)
        c = list(str(int(a) + int(b)))
        for _ in range(SPOILED):
            k = rng.randrange(1, len(c))
            c[k] = str(rng.randint(0, 9))
        print(a)
        print(b)
        print("".join(c))
        return
    for length in lengths:
        print(number(rng, length))


main()
