"""Modes: coprime SEED LOW HIGH chooses N in [LOW, HIGH] and a random unit A.

The modulus range must satisfy 3 <= LOW <= HIGH <= 10**9; A is in [2, N-1].
"""

from math import gcd
import random
import sys


def main():
    mode, seed, low, high = sys.argv[1:]
    seed, low, high = int(seed), int(low), int(high)
    if mode != "coprime" or not 3 <= low <= high <= 10**9:
        raise ValueError("expected: coprime SEED LOW HIGH, 3 <= LOW <= HIGH <= 10**9")
    rng = random.Random(seed)
    n = rng.randint(low, high)
    while True:
        a = rng.randint(2, n - 1)
        if gcd(a, n) == 1:
            break
    sys.stdout.reconfigure(newline="\n")
    print(a, n)


if __name__ == "__main__":
    main()
