"""One test from a seed and a mode: a count of ones. Mode 1 is any count
up to 10^18, mode 2 a count just below the total at a floor with many
ones, which cannot be told truthfully, mode 3 a count reached exactly at
a random floor."""

import random
import sys

TOP = 10**18
BASE = 10


def ones(x):
    total, p = 0, 1
    while p <= x:
        high, digit, low = x // (p * BASE), x // p % BASE, x % p
        total += high * p + (p if digit > 1 else low + 1 if digit == 1 else 0)
        p *= BASE
    return total


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        k = rng.randint(1, TOP)
    else:
        while True:
            floor = rng.randint(1, TOP // 2)
            if mode == 2:
                digits = list(str(floor))
                for i in rng.sample(range(len(digits)), len(digits) // 2):
                    digits[i] = "1"
                floor = int("".join(digits))
            k = ones(floor) - (1 if mode == 2 else 0)
            if 1 <= k <= TOP and str(floor).count("1") >= (2 if mode == 2 else 0):
                break
    print(k)


main()
