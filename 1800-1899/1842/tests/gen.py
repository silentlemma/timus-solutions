"""One word from a seed and a mode: mode 1 a short random word over two
letters, 2 the longest random word, 3 the longest word over two letters,
4 one letter repeated, 5 a random block repeated, 6 a Fibonacci word,
7 one b in the middle of a's, 8 a Thue-Morse word, 9 a random palindrome
of length 299999, 10 an alternating word broken by a final c, 11 two
equal runs of a and z. Modes 10 and 11 have the maximum length."""

import random
import string
import sys

MOST = 300000
SHORT = 20
BLOCK = 1000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        word = "".join(rng.choice("ab") for _ in range(rng.randint(2, SHORT)))
    elif mode == 2:
        word = "".join(rng.choice(string.ascii_lowercase) for _ in range(MOST))
    elif mode == 3:
        word = "".join(rng.choice("ab") for _ in range(MOST))
    elif mode == 4:
        word = "z" * MOST
    elif mode == 5:
        block = "".join(rng.choice("abc") for _ in range(rng.randint(2, BLOCK)))
        word = (block * (MOST // len(block) + 1))[:MOST]
    elif mode == 6:
        a, b = "a", "ab"
        while len(b) < MOST:
            a, b = b, b + a
        word = b[:MOST]
    elif mode == 7:
        half = MOST // 2
        word = "a" * (half - 1) + "b" + "a" * half
    elif mode == 9:
        half = "".join(rng.choice(string.ascii_lowercase) for _ in range(MOST // 2 - 1))
        word = half + rng.choice(string.ascii_lowercase) + half[::-1]
    elif mode == 10:
        word = ("ab" * (MOST // 2))[:-1] + "c"
    elif mode == 11:
        word = "a" * (MOST // 2) + "z" * (MOST // 2)
    else:
        bits = [0]
        while len(bits) < MOST:
            bits += [1 - v for v in bits]
        word = "".join("ab"[v] for v in bits[:MOST])
    print(word)


main()
