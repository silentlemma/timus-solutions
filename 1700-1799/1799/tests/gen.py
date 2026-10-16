"""One test from a seed and a mode: mode 1 a few hundred short strings
over two or three letters, mode 2 one random string of 100000 letters
over a few letters, mode 3 one long repetitive string (a run of one
letter, a short period repeated, or a Fibonacci word), mode 4 strings
of a few hundred letters, mode 5 100000 strings of one letter."""

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
    else:
        words = [rng.choice(string.ascii_lowercase) for _ in range(TOTAL)]
    print(len(words))
    print("\n".join(words))


main()
