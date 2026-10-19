import random
import sys

MAX_LENGTH = 100000
FULL_ALPHABET = b"abcdefghijklmnopqrstuvwxyz"


def generate(seed, mode):
    rng = random.Random(seed)
    count = MAX_LENGTH

    def word(size, alphabet):
        return bytes(rng.choice(alphabet) for _ in range(size))

    if mode in (1, 5, 6):
        shorter = count // 2 if mode == 6 else count - 1
        alphabet = b"ab" if mode == 5 else FULL_ALPHABET
        outer = word(shorter, alphabet)
        remaining = count - shorter
        half = word(remaining // 2, alphabet)
        middle = half + (b"z" if remaining % 2 else b"") + half[::-1]
        original = outer + middle
        first = original[1:] + original[:1]
        second = outer[::-1]
        shift = shorter // 2
        second = second[shift:] + second[:shift]
    elif mode == 2:
        first = word(count, b"ab")
        second = b"c" + word(count - 2, FULL_ALPHABET)
    elif mode == 3:
        first, second = b"a" * count, b"a" * (count - 2)
    elif mode == 4:
        first, second = b"a" * (count - 3) + b"bcd", b"a"
    elif mode == 7:
        first, second = b"a" * (count - 2) + b"bc", b"a" * (count // 2)
    else:
        raise ValueError("unknown generator mode")
    return first, second


if __name__ == "__main__":
    initial_seed, family = map(int, sys.argv[1:])
    left, right = generate(initial_seed, family)
    sys.stdout.buffer.write(left + b"\n" + right + b"\n")
