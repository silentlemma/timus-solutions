"""Contest logs from a seed: 100 contests with random names, dates, problem
counts and up to 100 submits each."""

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
