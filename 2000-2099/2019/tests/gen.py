"""Usage: seed mode. All modes use n=5000.
Modes: nested_upper_first, nested_lower_first, adjacent_upper_first,
adjacent_lower_first, random_valid_insertion, all_wrong_type,
balanced_counts_but_crossings, late_impossible_after_many_pairs.
Five modes construct valid noncrossing pairings; the last three are impossible.
"""

import random
import sys

COUNT = 5000
ALPHABET = 26


def generate(seed, mode):
    n = COUNT
    letters = "".join(chr(ord("A") + i % ALPHABET) for i in range(n))
    if mode == "nested_upper_first":
        word = letters + letters[::-1].lower()
    elif mode == "nested_lower_first":
        word = letters.lower() + letters[::-1]
    elif mode == "adjacent_upper_first":
        word = "Aa" * n
    elif mode == "adjacent_lower_first":
        word = "aA" * n
    elif mode == "all_wrong_type":
        word = "A" * n + "b" * n
    elif mode == "balanced_counts_but_crossings":
        word = "ABab" * (n // 2)
    elif mode == "late_impossible_after_many_pairs":
        word = "Aa" * (n - 1) + "Ab"
    elif mode == "random_valid_insertion":
        rng = random.Random(seed)
        word = ""
        for _ in range(n):
            letter = chr(ord("a") + rng.randrange(ALPHABET))
            pair = letter + letter.upper() if rng.randrange(2) else letter.upper() + letter
            at = rng.randrange(len(word) + 1)
            word = word[:at] + pair + word[at:]
    else:
        raise ValueError("unknown mode")
    return f"{n}\n{word}\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
