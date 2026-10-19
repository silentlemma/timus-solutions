"""Generate a maximum-size case: gen.py seed mode.
Modes: uniform, alternating_even, distinct_cycle, five_given_palindromes,
zimin, binary_random. All modes are deterministic for the given seed.
"""

import random
import sys

SIZE = 100000
PARTS = 5
ALPHABET = b"abcdefghijklmnopqrstuvwxyz"


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "uniform":
        return b"a" * SIZE
    if mode == "alternating_even":
        return b"ab" * (SIZE // 2)
    if mode == "distinct_cycle":
        return (ALPHABET * (SIZE // len(ALPHABET) + 1))[:SIZE]
    if mode == "five_given_palindromes":
        half = bytes(rng.choice(b"abcde") for _ in range(SIZE // (2 * PARTS)))
        return (half + half[::-1]) * PARTS
    if mode == "zimin":
        text = b"a"
        for letter in ALPHABET[1:]:
            text = text + bytes([letter]) + text
            if len(text) >= SIZE:
                return text[:SIZE]
    if mode == "binary_random":
        return bytes(rng.choice(b"ab") for _ in range(SIZE))
    raise ValueError("unknown mode")


if __name__ == "__main__":
    seed, mode = sys.argv[1:]
    sys.stdout.buffer.write(generate(int(seed), mode) + b"\n")
