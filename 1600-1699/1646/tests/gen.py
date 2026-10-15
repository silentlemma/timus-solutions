"""One test from a seed and a mode: mode 1 a few days over two letters,
mode 2 100 days of doubling over two letters, mode 3 a long pattern over
all four letters, mode 4 a one-letter pattern."""

import random
import sys

MOST_DAYS = 100
LONGEST_PATTERN = 100
LONGEST_SAMPLE = 10


def word(rng, letters, low, high):
    return "".join(rng.choice(letters) for _ in range(rng.randint(low, high)))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    letters = "ACGT" if mode == 3 else rng.choice(["AC", "AG", "CT"])
    if mode == 4:
        pattern = rng.choice(letters)
    elif mode == 3:
        pattern = word(rng, letters, 1, LONGEST_PATTERN)
    else:
        pattern = word(rng, letters, 1, 6)
    first, second = word(rng, letters, 1, LONGEST_SAMPLE), word(rng, letters, 1, LONGEST_SAMPLE)
    m = rng.randint(1, 6) if mode == 1 else MOST_DAYS
    days = []
    for k in range(1, m + 1):
        if mode == 2 and rng.random() < 0.7:
            days.append((k + 1, k + 1))  # double the newest sample
        else:
            days.append((rng.randint(1, k + 1), rng.randint(1, k + 1)))
    print(pattern)
    print(first)
    print(second)
    print(m)
    for a, b in days:
        print(a, b)


main()
