"""Usage: seed mode. Every mode produces 100000 positions.
Modes: all_free, plus_only, minus_only, all_types_fixed, all_fixed_feasible,
all_fixed_impossible, one_hole_feasible, one_hole_impossible,
random_dense, few_fixed_many_new.
"""

import random
import string
import sys

COUNT = 100000
ALPHABET = string.ascii_lowercase
MIN_THREE_TYPES = 3


def generate(seed, mode):
    rng = random.Random(seed)
    limit = len(ALPHABET)
    if mode == "all_free":
        text = "?" * COUNT
    elif mode == "plus_only":
        text = "?a" * (COUNT // 2)
    elif mode == "minus_only":
        text = "z?" * (COUNT // 2)
    elif mode == "all_types_fixed":
        text = ALPHABET + "?" * (COUNT - len(ALPHABET))
    elif mode in ("all_fixed_feasible", "all_fixed_impossible"):
        text = "az" * (COUNT // 2)
        limit = 2 if mode == "all_fixed_feasible" else MIN_THREE_TYPES
    elif mode in ("one_hole_feasible", "one_hole_impossible"):
        text = "z" * (COUNT // 2) + "?" + "z" * (COUNT // 2 - 1)
        limit = 2 if mode == "one_hole_feasible" else MIN_THREE_TYPES
    elif mode == "random_dense":
        text = "".join("?" if rng.random() < 0.75 else rng.choice(ALPHABET) for _ in range(COUNT))
    elif mode == "few_fixed_many_new":
        block = "?m??"
        text = block * (COUNT // len(block))
    else:
        raise ValueError("unknown mode")
    assert len(text) == COUNT
    return text + "\n" + str(limit) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
