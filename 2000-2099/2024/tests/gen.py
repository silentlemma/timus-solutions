"""Usage: seed mode. Modes produce 100000 letters, except
max_binomial with 99996 letters so that all 26 frequencies are equal.
Modes: one_color_small_k, one_color_large_k, all_colors_all,
balanced_boundary, max_binomial, mandatory_and_ties, skewed, random, random_one.
"""

import random
import string
import sys

COUNT = 100000
ALPHABET = string.ascii_lowercase


def generate(seed, mode):
    rng = random.Random(seed)
    if mode in ("one_color_small_k", "one_color_large_k"):
        text = "z" * COUNT
        limit = 1 if mode == "one_color_small_k" else len(ALPHABET)
    elif mode == "all_colors_all":
        text = (ALPHABET * (COUNT // len(ALPHABET) + 1))[:COUNT]
        limit = len(ALPHABET)
    elif mode == "balanced_boundary":
        text = (ALPHABET * (COUNT // len(ALPHABET) + 1))[:COUNT]
        limit = len(ALPHABET) // 2
    elif mode == "max_binomial":
        text = ALPHABET * (COUNT // len(ALPHABET))
        limit = len(ALPHABET) // 2
    elif mode == "mandatory_and_ties":
        text = "a" * (COUNT // 2)
        tail = ALPHABET[1:]
        text += tail * ((COUNT - len(text)) // len(tail))
        limit = len(ALPHABET) // 2
    elif mode == "skewed":
        text = "a" * (COUNT - len(ALPHABET)) + ALPHABET
        limit = 2
    elif mode in ("random", "random_one"):
        text = "".join(rng.choices(ALPHABET, k=COUNT))
        limit = 1 if mode == "random_one" else len(ALPHABET) // 2
    else:
        raise ValueError("unknown mode")
    assert len(text) == (COUNT - COUNT % len(ALPHABET) if mode == "max_binomial" else COUNT)
    return text + "\n" + str(limit) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
