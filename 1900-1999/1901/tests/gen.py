"""Deterministic generator: seed mode.

Modes: 0 small random; 1 all light; 2 all heavy; 3 random large weights;
4 threshold ties; 5 many small values with fewer universal heavy values;
6 capacity one; 7 sorted random; 8 reverse-sorted random; 9 alternating
minimum and maximum weights. Modes 1 through 9 use 100000 passengers.
"""

import random
import sys

MAX_COUNT = 100_000
MAX_CAPACITY = 1_000_000_000
SMALL_COUNT = 9
STAR_PERIOD = 3
STAR_SMALL = 4
STAR_LARGE = 7
STAR_CAPACITY = 10
ARGUMENT_COUNT = 3
MODE_SMALL = 0
MODE_LIGHT = 1
MODE_HEAVY = 2
MODE_RANDOM = 3
MODE_THRESHOLD = 4
MODE_STAR = 5
MODE_UNIT = 6
MODE_SORTED = 7
MODE_REVERSED = 8
MODE_EXTREMES = 9


def generate(seed, mode):
    rng = random.Random(seed)
    count, capacity = MAX_COUNT, MAX_CAPACITY
    if mode == MODE_SMALL:
        count = SMALL_COUNT
        capacity = rng.randint(1, STAR_CAPACITY * 2)
        values = [rng.randint(1, capacity) for _ in range(count)]
    elif mode == MODE_LIGHT:
        values = [1] * count
    elif mode == MODE_HEAVY:
        values = [rng.randint(capacity // 2 + 1, capacity) for _ in range(count)]
    elif mode in (MODE_RANDOM, MODE_SORTED, MODE_REVERSED):
        values = [rng.randint(1, capacity) for _ in range(count)]
        if mode != MODE_RANDOM:
            values.sort(reverse=mode == MODE_REVERSED)
    elif mode == MODE_THRESHOLD:
        values = [capacity // 2 + (index % 2) for index in range(count)]
    elif mode == MODE_STAR:
        capacity = STAR_CAPACITY
        values = [STAR_LARGE if index % STAR_PERIOD == 0 else STAR_SMALL
                  for index in range(count)]
    elif mode == MODE_UNIT:
        capacity, values = 1, [1] * count
    elif mode == MODE_EXTREMES:
        values = [1 if index % 2 == 0 else capacity for index in range(count)]
    else:
        raise ValueError("Unknown generator mode")
    return count, capacity, values


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit(__doc__)
    count, capacity, values = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(count, capacity)
    print(*values)


if __name__ == "__main__":
    main()
