"""One test from a seed and a mode: mode 1 a short random word over few
letters, mode 2 a zigzag a..z..a..z over up to 17 letters (universal) with
a few letters deleted, mode 3 copies of random orders of the letters,
mode 4 a long random word over many letters, mode 5 a 300-letter word
over 13 letters with one central m and random orders of a..l on both sides."""

import random
import sys

LONGEST = 300


def zigzag(n):
    letters = [chr(ord("a") + i) for i in range(n)]
    word = list(letters)
    for k in range(1, n):
        part = letters[-2::-1] if k % 2 else letters[1:]
        word += part
    return word


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, 6)
        word = [chr(ord("a") + rng.randrange(n)) for _ in range(rng.randint(1, 40))]
    elif mode == 2:
        n = rng.randint(8, 17)
        word = zigzag(n)
        for _ in range(rng.randint(0, 2)):
            del word[rng.randrange(len(word))]
    elif mode == 3:
        n = rng.randint(3, 16)
        letters = [chr(ord("a") + i) for i in range(n)]
        word = []
        while len(word) + n <= LONGEST:
            word += rng.sample(letters, n)
    elif mode == 5:
        n = 13
        letters = [chr(ord("a") + i) for i in range(n - 1)]
        left = []
        right = []
        for _ in range(n - 1):
            left += rng.sample(letters, n - 1)
            right += rng.sample(letters, n - 1)
        padding = [rng.choice(letters) for _ in range(LONGEST - 2 * len(left) - 1)]
        word = left + ["m"] + right + padding
    else:
        n = rng.randint(18, 24)
        word = [chr(ord("a") + rng.randrange(n)) for _ in range(LONGEST)]
    print(n)
    print("".join(word[:LONGEST]))


main()
