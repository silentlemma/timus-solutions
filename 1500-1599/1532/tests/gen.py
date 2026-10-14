"""One test from a seed and a mode, K = 5000 distinct words unless small.
Mode 1 takes random words of 1 to 15 letters, mode 2 misspells a few base
words by one to three edits, mode 3 takes 15 letters a and b, mode 4 four
letters, mode 5 is small with letters a to c, mode 6 grows words by
inserting letters, mode 7 takes random words of 15 letters, mode 8 takes
5000 length-15 words sharing a 12-letter head and random distinct suffixes."""

import random
import sys

LARGEST = 5000
LONGEST = 15
SMALL = 12
SHORT = 4
MISTAKES = 3


def misspell(rng, w, letters):
    for _ in range(rng.randint(1, MISTAKES)):
        i = rng.randint(0, len(w))
        kind = rng.randint(0, 2)
        if kind == 0 and len(w) < LONGEST:
            w = w[:i] + rng.choice(letters) + w[i:]
        elif kind == 1 and len(w) > 1 and i < len(w):
            w = w[:i] + w[i + 1 :]
        elif i < len(w):
            w = w[:i] + rng.choice(letters) + w[i + 1 :]
    return w


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 8:
        letters = "abcdefghijklmnopqrstuvwxyz"
        suffixes = rng.sample(range(len(letters) ** 3), LARGEST)
        print(LARGEST)
        for value in suffixes:
            suffix = ""
            for _ in range(3):
                value, digit = divmod(value, len(letters))
                suffix = letters[digit] + suffix
            print("abcdefghijkl" + suffix)
        return
    k = rng.randint(1, SMALL) if mode == 5 else LARGEST
    letters = "abc" if mode == 5 else ("ab" if mode == 3 else "abcdefghijklmnopqrstuvwxyz")
    seen = set()
    words = []
    while len(words) < k:
        if mode == 2 and words and rng.random() < 0.9:
            w = misspell(rng, rng.choice(words), letters)
        elif mode in (3, 7):
            w = "".join(rng.choice(letters) for _ in range(LONGEST))
        elif mode == 4:
            w = "".join(rng.choice(letters) for _ in range(SHORT))
        elif mode == 6 and words and rng.random() < 0.5:
            w = rng.choice(words)
            while len(w) < LONGEST and rng.random() < 0.7:
                i = rng.randint(0, len(w))
                w = w[:i] + rng.choice(letters) + w[i:]
        else:
            w = "".join(
                rng.choice(letters) for _ in range(rng.randint(1, SHORT if mode == 5 else LONGEST))
            )
        if w not in seen:
            seen.add(w)
            words.append(w)
    print(k)
    print("\n".join(words))


main()
