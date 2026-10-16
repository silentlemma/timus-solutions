"""One test from a seed and a mode: mode 1 a few hundred short strings
over two or three letters, mode 2 one random string of 100000 letters
over a few letters, mode 3 one long repetitive string (a run of one
letter, a short period repeated, or a Fibonacci word), mode 4 strings
of a few hundred letters, mode 5 100000 strings of one letter,
mode 6 two equally long runs of different letters, mode 7 two runs
of one letter separated by a single other letter, mode 8 a long
two-run string among short strings and a final unary string, mode 9
random strings with shared blocks over wider alphabets. Modes 6-8
accept an optional total length (at least 1000 for mode 8); otherwise
the total length is 100000. Usage: gen.py SEED MODE [TOTAL_LENGTH]."""

import random
import string
import sys

TOTAL = 100000
SHORT = 9
MEDIUM = 300


def fibonacci_word(length):
    a, b = "a", "ab"
    while len(b) < length:
        a, b = b, b + a
    return b[:length]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        letters = "abc"[:rng.randint(2, 3)]
        words = ["".join(rng.choice(letters) for _ in range(rng.randint(1, SHORT)))
                 for _ in range(rng.randint(1, MEDIUM))]
    elif mode == 2:
        letters = string.ascii_lowercase[:rng.choice([2, 3, 4, 26])]
        words = ["".join(rng.choice(letters) for _ in range(TOTAL))]
    elif mode == 3:
        kind = rng.randint(0, 2)
        if kind == 0:
            words = ["a" * TOTAL]
        elif kind == 1:
            period = "".join(rng.choice("ab") for _ in range(rng.randint(2, SHORT)))
            words = [(period * TOTAL)[:TOTAL]]
        else:
            words = [fibonacci_word(TOTAL)]
    elif mode == 4:
        words = []
        left = TOTAL
        while left > 0:
            length = min(left, rng.randint(1, MEDIUM))
            letters = string.ascii_lowercase[:rng.randint(1, 4)]
            words.append("".join(rng.choice(letters) for _ in range(length)))
            left -= length
    elif mode == 6:
        total = int(sys.argv[3]) if len(sys.argv) > 3 else TOTAL
        words = ["a" * (total // 2) + "z" * (total - total // 2)]
    elif mode == 7:
        total = int(sys.argv[3]) if len(sys.argv) > 3 else TOTAL
        words = ["a" * (total // 2) + "z" + "a" * (total - total // 2 - 1)]
    elif mode == 8:
        total = int(sys.argv[3]) if len(sys.argv) > 3 else TOTAL
        words = ["z", "abacaba"]
        long_length = min(total * 9 // 10, total - 300)
        words.append("a" * (long_length // 2) + "b" * (long_length - long_length // 2))
        words.extend("".join(rng.choice("abcxyz") for _ in range(rng.randint(1, 12)))
                     for _ in range(20))
        words.extend(["a" * (total - sum(map(len, words)) - 1), "z"])
    elif mode == 9:
        words = []
        for index in range(200):
            letters = rng.choice([string.ascii_lowercase, "acmxyz", "abz"])
            block = "".join(rng.choice(letters) for _ in range(rng.randint(4, 16)))
            middle = rng.choice(letters)
            if index % 3 == 0:
                words.append(block + middle + block)
            elif index % 3 == 1:
                words.append(block + block[::-1] + middle)
            else:
                words.append(block + middle + block[1:] + block[:3])
    else:
        words = [rng.choice(string.ascii_lowercase) for _ in range(TOTAL)]
    print(len(words))
    print("\n".join(words))


main()
