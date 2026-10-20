"""Sender type and v from a seed: mode 1 a random v, mode 2 a v with zero
bytes, mode 3 a palindromic byte order that maps to itself."""

import random
import sys

TOP = 2 ** 32 - 1
BYTE = 255
DIGITS = 4


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    kind = rng.choice(["GOOD", "BAD"])
    if mode == 1:
        v = rng.randint(0, TOP)
    elif mode == 2:
        digits = [rng.choice([0, rng.randint(1, BYTE)]) for _ in range(DIGITS)]
        v = int.from_bytes(bytes(digits), "big")
    else:
        a, b = rng.randint(0, BYTE), rng.randint(0, BYTE)
        v = int.from_bytes(bytes([a, b, b, a]), "big")
    print(kind)
    print(v)


main()
