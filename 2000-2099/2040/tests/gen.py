"""Generate a binary word: seed mode.

Maximum modes: unary_a, unary_b, alternating_a, alternating_b, periodic_aab,
periodic_nonrich, random_binary, one_separator, long_blocks, thue_morse, fibonacci.
Mode boundary uses the seed as length and emits an alternating word.
"""

import random
import sys

SIZE = 5000000
HALF = SIZE // 2
BLOCKS = 17


def repeated(pattern, length):
    return (pattern * ((length + len(pattern) - 1) // len(pattern)))[:length]


def build(seed, mode):
    if mode == "unary_a":
        return b"a" * SIZE
    if mode == "unary_b":
        return b"b" * SIZE
    if mode == "alternating_a":
        return repeated(b"ab", SIZE)
    if mode == "alternating_b":
        return repeated(b"ba", SIZE)
    if mode == "periodic_aab":
        return repeated(b"aab", SIZE)
    if mode == "periodic_nonrich":
        return repeated(b"aababbaa", SIZE)
    if mode == "random_binary":
        rng = random.Random(seed)
        return bytes(rng.getrandbits(1) + ord("a") for _ in range(SIZE))
    if mode == "one_separator":
        return b"a" * HALF + b"b" + b"a" * (SIZE - HALF - 1)
    if mode == "long_blocks":
        block = SIZE // BLOCKS
        return repeated(b"a" * block + b"b" * block, SIZE)
    if mode == "thue_morse":
        word = b"a"
        translation = bytes.maketrans(b"ab", b"ba")
        while len(word) < SIZE:
            word += word.translate(translation)
        return word[:SIZE]
    if mode == "fibonacci":
        previous, current = b"b", b"a"
        while len(current) < SIZE:
            previous, current = current, current + previous
        return current[:SIZE]
    if mode == "boundary" and 1 <= seed <= SIZE:
        return repeated(b"ab", seed)
    raise ValueError("Unknown mode or invalid length")


def main():
    sys.stdout.buffer.write(build(int(sys.argv[1]), sys.argv[2]))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
