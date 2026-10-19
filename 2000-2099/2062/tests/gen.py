"""Generate one experiment: gen.py seed mode.

Modes: wide_repeat, prefix_repeat, mixed_indices, all_unique_queries,
n1_overflow, all_updates, narrow_random, square_mixed.
All use q=300000; n=300000 except n1_overflow, where n=1.
The seed selects narrow random intervals/queries. Other modes are fixed.
"""

import random
import sys

MAX_SIZE = 300000
MAX_POWER = 1000000
SMALL_PREFIX = 1000
RADIATION_START = 17
NARROW_WIDTH = 4
DIVISIBLE = (277200, 221760, 249480, 166320, 196560, 240240, 262080, 294840)
ROOTS = (1, 2, 3, 7, 13, 17, 31, 64, 127, 256, 527, 547)


def make(seed, mode):
    size = 1 if mode == "n1_overflow" else MAX_SIZE
    yield str(size)
    yield " ".join([str(MAX_POWER)] * size)
    yield str(MAX_SIZE)
    if mode == "all_unique_queries":
        for index in range(1, size + 1):
            yield f"1 {index}"
        return
    if mode == "all_updates":
        for _ in range(MAX_SIZE):
            yield f"2 1 {size} {MAX_POWER}"
        return
    rng = random.Random(seed)
    for step in range(1, MAX_SIZE // 2 + 1):
        left, right, power = 1, size, MAX_POWER
        index = DIVISIBLE[0]
        if mode == "prefix_repeat":
            right = SMALL_PREFIX
        elif mode == "mixed_indices":
            left, right = 2, size - 1
            index = DIVISIBLE[(step - 1) % len(DIVISIBLE)]
        elif mode == "n1_overflow":
            index = 1
        elif mode == "narrow_random":
            left = rng.randrange(1, size + 1)
            right = min(size, left + rng.randrange(NARROW_WIDTH))
            power = rng.randrange(MAX_POWER + 1)
            index = rng.randrange(1, size + 1)
        elif mode == "square_mixed":
            left, right = RADIATION_START, SMALL_PREFIX
            power = step % MAX_POWER
            root = ROOTS[(step - 1) % len(ROOTS)]
            index = root * root
        elif mode != "wide_repeat":
            raise ValueError("Unknown mode")
        yield f"2 {left} {right} {power}"
        yield f"1 {index}"


def main():
    for line in make(int(sys.argv[1]), sys.argv[2]):
        print(line)


if __name__ == "__main__":
    main()
