"""One test from a seed and a mode, N = 100000 unless small. Mode 1 takes
random letters, mode 2 only A and B, mode 3 copies a long piece of the
first speech into the second, mode 4 repeats one letter in both, mode 5
gives the speeches no common letter, mode 6 is small."""

import random
import string
import sys

LARGEST = 100000
SMALL = 12


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 6 else LARGEST
    letters = string.ascii_uppercase
    if mode == 2 or mode == 6:
        letters = "AB"

    def speech(alphabet):
        return "".join(rng.choice(alphabet) for _ in range(n))

    if mode == 4:
        a = b = "Q" * n
    elif mode == 5:
        a, b = speech(letters[:13]), speech(letters[13:])
    else:
        a, b = speech(letters), speech(letters)
        if mode == 3:
            size = rng.randint(n // 4, n // 2)
            src, dst = rng.randrange(n - size), rng.randrange(n - size)
            b = b[:dst] + a[src : src + size] + b[dst + size :]
    print(n)
    print(a)
    print(b)


main()
