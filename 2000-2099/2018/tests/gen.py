"""Usage: seed mode. All modes set n=50000.
Modes: balanced, a_one, b_one, both_one, near_equal, a_large_b_small,
a_small_b_large, random. Both run limits are between 1 and 300.
"""

import random
import sys

MAX_LENGTH = 50000
MAX_RUN = 300


def generate(seed, mode):
    pairs = {
        "balanced": (MAX_RUN, MAX_RUN),
        "a_one": (1, MAX_RUN),
        "b_one": (MAX_RUN, 1),
        "both_one": (1, 1),
        "near_equal": (MAX_RUN - 1, MAX_RUN),
        "a_large_b_small": (MAX_RUN, 2),
        "a_small_b_large": (2, MAX_RUN),
    }
    rng = random.Random(seed)
    pairs["random"] = (rng.randint(1, MAX_RUN), rng.randint(1, MAX_RUN))
    a, b = pairs[mode]
    return f"{MAX_LENGTH} {a} {b}\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
