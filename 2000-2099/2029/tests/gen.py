"""Usage: seed mode. Every mode produces a valid 50-disk state.
Modes: all_a, all_b, all_c, smallest_b, largest_c, alternating, random, small_prefix.
"""

import random
import sys

DISKS = 50
SMALL_PREFIX = 10


def generate(seed, mode):
    rng = random.Random(seed)
    if mode in ("all_a", "all_b", "all_c"):
        state = mode[-1].upper() * DISKS
    elif mode == "smallest_b":
        state = "B" + "A" * (DISKS - 1)
    elif mode == "largest_c":
        state = "A" * (DISKS - 1) + "C"
    elif mode == "alternating":
        state = ("ABC" * DISKS)[:DISKS]
    elif mode == "random":
        state = "".join(rng.choices("ABC", k=DISKS))
    elif mode == "small_prefix":
        state = "".join(rng.choices("ABC", k=SMALL_PREFIX)) + "A" * (DISKS - SMALL_PREFIX)
    else:
        raise ValueError("unknown mode")
    return str(DISKS) + "\n" + state + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
