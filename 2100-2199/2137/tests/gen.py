"""Deterministic binary strings: python gen.py MODE SEED.

Modes 1 and 2 generate short and medium random strings. Modes 3 through 9
generate maximal random, unary, alternating, periodic, damaged periodic,
recursively bordered and long-period strings. Mode 10 covers the search split
boundary, mode 11 damages a maximal unary string, and mode 12 makes short
strings with overlapping periods.
"""

import random
import sys

MAX_LENGTH = 100_000
MEDIUM_LENGTH = 2_000
SHORT_LENGTH = 50
EXTENSION = 25
ALPHABET = ".X"

MODE_SHORT = 1
MODE_MEDIUM = 2
MODE_RANDOM = 3
MODE_UNARY = 4
MODE_ALTERNATING = 5
MODE_PERIODIC = 6
MODE_DAMAGED = 7
MODE_RECURSIVE = 8
MODE_LONG_PERIOD = 9
MODE_BOUNDARY = 10
MODE_ONE_CHANGE = 11
MODE_OVERLAP = 12


def random_word(rng, length):
    return "".join(rng.choices(ALPHABET, k=length))


def repeat(block, length):
    return (block * ((length + len(block) - 1) // len(block)))[:length]


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SHORT:
        return random_word(rng, rng.randint(0, SHORT_LENGTH))
    if mode == MODE_MEDIUM:
        return random_word(rng, rng.randint(SHORT_LENGTH + 1, MEDIUM_LENGTH))
    if mode == MODE_RANDOM:
        return random_word(rng, MAX_LENGTH)
    if mode == MODE_UNARY:
        return rng.choice(ALPHABET) * MAX_LENGTH
    if mode == MODE_ALTERNATING:
        return repeat(rng.choice((ALPHABET, ALPHABET[::-1])), MAX_LENGTH)
    if mode in (MODE_PERIODIC, MODE_DAMAGED):
        block = random_word(rng, rng.randint(1, EXTENSION))
        word = repeat(block, MAX_LENGTH)
        if mode == MODE_DAMAGED:
            position = rng.choice(
                (rng.randrange(MAX_LENGTH), MAX_LENGTH - 1 - rng.randrange(EXTENSION))
            )
            other = ALPHABET[1 - ALPHABET.index(word[position])]
            word = word[:position] + other + word[position + 1 :]
        return word
    if mode == MODE_RECURSIVE:
        word = rng.choice(ALPHABET)
        while len(word) < MAX_LENGTH:
            word = word + rng.choice(ALPHABET) + word
        return word[:MAX_LENGTH]
    if mode == MODE_LONG_PERIOD:
        block = random_word(rng, rng.randint(EXTENSION + 1, MAX_LENGTH // 2))
        return repeat(block, MAX_LENGTH)
    if mode == MODE_BOUNDARY:
        length = EXTENSION + rng.choice((-2, -1, 0, 1, 2))
        return random_word(rng, length)
    if mode == MODE_ONE_CHANGE:
        symbol = rng.choice(ALPHABET)
        position = rng.choice((rng.randrange(EXTENSION), MAX_LENGTH - 1))
        return (
            symbol * position
            + ALPHABET[1 - ALPHABET.index(symbol)]
            + (symbol * (MAX_LENGTH - position - 1))
        )
    if mode == MODE_OVERLAP:
        length = rng.randint((EXTENSION + 1) // 2, SHORT_LENGTH)
        word = rng.choice(ALPHABET) * length
        if rng.randrange(2):
            position = rng.randrange(length)
            word = word[:position] + ALPHABET[1 - ALPHABET.index(word[0])] + (word[position + 1 :])
        return word
    raise ValueError("unknown mode")


def main():
    mode, seed = map(int, sys.argv[1:])
    sys.stdout.write(generate(mode, seed) + "\n")


if __name__ == "__main__":
    main()
