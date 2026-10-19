"""Modes:
SEED: 100 random contests (the original seeded mode).
max: maximum input size, 100 longest names and 100 longest verdicts per log.
sparse SEED: shuffled problem counts 1 through 13, with few random submits.
"""

import random
import string
import sys

CONTESTS = 100
NAME_LENGTH = 30
LETTERS = "ABCDEFGHIJKLM"
MAX_SUBMITS = 100
VERDICTS = ["Accepted", "Wrong Answer", "Runtime Error", "Time Limit Exceeded",
            "Memory Limit Exceeded", "Compilation Error"]
DAYS = 28
MONTHS = 12
YEARS = 100


def main():
    if sys.argv[1] == "max":
        print(CONTESTS)
        for i in range(CONTESTS):
            print("Maximum Contest " + str(i).zfill(14))
            print("31.12.99")
            print(len(LETTERS), MAX_SUBMITS)
            for j in range(MAX_SUBMITS):
                print(LETTERS[j % len(LETTERS)], "Memory Limit Exceeded")
        return
    if sys.argv[1] == "sparse":
        rng = random.Random(int(sys.argv[2]))
        counts = list(range(1, len(LETTERS) + 1)) * 2
        rng.shuffle(counts)
        print(len(counts))
        for i, p in enumerate(counts):
            print("Sparse log " + str(i))
            print("%02d.%02d.%02d" % (rng.randint(1, DAYS), rng.randint(1, MONTHS),
                                      rng.randrange(YEARS)))
            s = rng.randint(0, p)
            print(p, s)
            for _ in range(s):
                print(LETTERS[rng.randrange(p)], rng.choice(VERDICTS))
        return
    rng = random.Random(int(sys.argv[1]))
    symbols = string.ascii_letters + string.digits + " "
    print(CONTESTS)
    for _ in range(CONTESTS):
        length = rng.randint(1, NAME_LENGTH)
        name = "".join(rng.choice(symbols) for _ in range(length)).strip() or "x"
        print(name)
        print("%02d.%02d.%02d" % (rng.randint(1, DAYS), rng.randint(1, MONTHS),
                                  rng.randrange(YEARS)))
        p, s = rng.randint(1, len(LETTERS)), rng.randint(0, MAX_SUBMITS)
        print(p, s)
        for _ in range(s):
            print(LETTERS[rng.randrange(p)], rng.choice(VERDICTS))


main()
