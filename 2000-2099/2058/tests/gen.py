"""Generate maximal lowercase words: constant, alternating, two_runs, ruler, binary, letters.

Usage: gen.py seed mode; all modes have length 300000, seed affects random modes.
"""

import random
import sys

MAX_LENGTH = 300000
ALPHABET_SIZE = 26


def make(seed, mode):
    rng = random.Random(seed)
    n = MAX_LENGTH
    if mode == "constant":
        return "a" * n
    if mode == "alternating":
        return "ab" * (n // 2)
    if mode == "two_runs":
        return "a" * (n // 2) + "b" * (n // 2)
    if mode == "ruler":
        return "".join(chr(ord("a") + (i & -i).bit_length() - 1) for i in range(1, n + 1))
    alphabet = "ab" if mode == "binary" else "abcdefghijklmnopqrstuvwxyz"
    if mode not in ("binary", "letters"):
        raise ValueError("Unknown generation mode")
    return "".join(rng.choice(alphabet) for _ in range(n))


def main():
    print(make(int(sys.argv[1]), sys.argv[2]))


if __name__ == "__main__":
    main()
