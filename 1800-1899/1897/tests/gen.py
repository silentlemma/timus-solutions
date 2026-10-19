"""Deterministic generator: seed mode.

Modes: 0 small random; 1 maximal even constant; 2 maximal odd constant;
3 alternating; 4 period three; 5 random alphabet; 6 random binary;
7 rare defects; 8 repeated mirrored block; 9 full-alphabet periodic;
10 a single central defect; 11 sparse binary with probability 1/101 for b.
Modes 1 through 11 use maximal input lengths.
"""

import random
import string
import sys

MAX_LENGTH = 100_000
SMALL_MAX = 24
RARE_PERIOD = 997
MIRROR_BLOCK_LENGTH = 97
SPARSE_DENOMINATOR = 101
ARGUMENT_COUNT = 3
MODE_SMALL = 0
MODE_CONSTANT_EVEN = 1
MODE_CONSTANT_ODD = 2
MODE_ALTERNATING = 3
MODE_PERIOD_THREE = 4
MODE_RANDOM_ALPHABET = 5
MODE_RANDOM_BINARY = 6
MODE_RARE = 7
MODE_MIRROR = 8
MODE_ALPHABET_PERIODIC = 9
MODE_CENTRAL_DEFECT = 10
MODE_SPARSE_BINARY = 11


def repeat_to_length(pattern, size):
    return (pattern * ((size + len(pattern) - 1) // len(pattern)))[:size]


def generate(seed, mode):
    rng = random.Random(seed)
    size = MAX_LENGTH - (mode == MODE_CONSTANT_ODD)
    rank = size // 2
    if mode == MODE_SMALL:
        size = rng.randint(1, SMALL_MAX)
        text = "".join(rng.choice("abc") for _ in range(size))
        rank = rng.randint(1, size * (size + 1) // 2 + 2)
    elif mode in (MODE_CONSTANT_EVEN, MODE_CONSTANT_ODD):
        text = "a" * size
        rank = (size + 1) // 2
    elif mode == MODE_ALTERNATING:
        text = repeat_to_length("ab", size)
    elif mode == MODE_PERIOD_THREE:
        text = repeat_to_length("abc", size)
    elif mode == MODE_RANDOM_ALPHABET:
        text = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
    elif mode == MODE_RANDOM_BINARY:
        text = "".join(rng.choice("ab") for _ in range(size))
    elif mode == MODE_RARE:
        letters = ["a"] * size
        for index in range(seed % RARE_PERIOD, size, RARE_PERIOD):
            letters[index] = "b"
        letters[size // 2] = "c"
        text = "".join(letters)
    elif mode == MODE_MIRROR:
        block = "".join(rng.choice("abc") for _ in range(MIRROR_BLOCK_LENGTH))
        text = repeat_to_length(block + block[::-1], size)
    elif mode == MODE_ALPHABET_PERIODIC:
        text = repeat_to_length(string.ascii_lowercase, size)
    elif mode == MODE_CENTRAL_DEFECT:
        text = "a" * (size // 2 - 1) + "b" + "a" * (size - size // 2)
    elif mode == MODE_SPARSE_BINARY:
        text = "".join("b" if rng.randrange(SPARSE_DENOMINATOR) == 0 else "a"
                       for _ in range(size))
    else:
        raise ValueError("Unknown generator mode")
    return text, rank


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit(__doc__)
    text, rank = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(text)
    print(rank)


if __name__ == "__main__":
    main()
