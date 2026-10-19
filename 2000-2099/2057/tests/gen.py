"""Seed/family: constant, alternating_even, alternating_odd, unique_letter,
outer_letters, odd_defect, abba_blocks, random_lower, random_mixed, pal_blocks.
Lengths are 200000, or 199999 for odd families; generated fixtures only.
"""

import random
import sys

MAX_LENGTH = 200000


def generate(seed, family):
    n = MAX_LENGTH
    if family == "constant":
        word = "a" * n
    elif family == "alternating_even":
        word = "ab" * (n // 2)
    elif family == "alternating_odd":
        word = "ab" * (n // 2 - 1) + "a"
    elif family == "unique_letter":
        word = "a" * (n // 2) + "b" + "a" * (n // 2 - 1)
    elif family == "outer_letters":
        word = "a" + "b" * (n - 2) + "a"
    elif family == "odd_defect":
        word = "ab" * ((n - 3) // 2) + "aca"
    elif family == "abba_blocks":
        block = "abba"
        word = block * (n // len(block))
    elif family == "pal_blocks":
        block = "abcba"
        word = block * (n // len(block))
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if family == "random_mixed":
            alphabet += alphabet.upper()
        elif family != "random_lower":
            raise ValueError("unknown family")
        randomizer = random.Random(seed)
        word = "".join(randomizer.choice(alphabet) for _ in range(n))
    return word + "\n"


if __name__ == "__main__":
    sys.stdout.write(generate(int(sys.argv[1]), sys.argv[2]))
