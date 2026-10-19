"""Generate a lowercase word: gen.py seed mode.

Modes: constant, alternating_even, alternating_odd, period_three, two_runs,
max_ruler, max_binary, max_letters. All have length 300000 except
alternating_odd, which has length 299999. The seed affects random modes.
"""

import random
import sys

MAX_LENGTH = 300000
PERIOD_THREE = "abc"


def make(seed, mode):
    n = MAX_LENGTH
    if mode == "constant":
        return "a" * n
    if mode == "alternating_even":
        return "ab" * (n // 2)
    if mode == "alternating_odd":
        return "ab" * (n // 2 - 1) + "a"
    if mode == "period_three":
        return (PERIOD_THREE * ((n + len(PERIOD_THREE) - 1) // len(PERIOD_THREE)))[:n]
    if mode == "two_runs":
        return "a" * (n // 2) + "b" * (n - n // 2)
    if mode == "max_ruler":
        return "".join(chr(ord("a") + (i & -i).bit_length() - 1) for i in range(1, n + 1))
    if mode not in ("max_binary", "max_letters"):
        raise ValueError("Unknown mode")
    rng = random.Random(seed)
    alphabet = "ab" if mode == "max_binary" else "abcdefghijklmnopqrstuvwxyz"
    return "".join(rng.choice(alphabet) for _ in range(n))


def main():
    print(make(int(sys.argv[1]), sys.argv[2]))


if __name__ == "__main__":
    main()
