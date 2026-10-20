"""Run python gen.py MODE SEED: 1 small, 2 random, 3 max N, 4 max M, 5 width transitions,
6 first position, 7 last position, 8 powers of two, 9 alternating bits, 10 max N and M,
11 huge N and tiny M, 12 near max M."""

import random
import sys

MAX_VALUE = 1_000_000_000
MAX_BITS = 30
MIN_DEEP_DEPTH = MAX_BITS + 1
MODE_SMALL = 1
MODE_RANDOM = 2
MODE_DEEPEST = 3
MODE_MAX_POSITION = 4
MODE_WIDTH_BOUNDARY = 5
MODE_FIRST = 6
MODE_LAST = 7
MODE_POWER_BOUNDARY = 8
MODE_ALTERNATING = 9
MODE_MAXIMUM = 10
MODE_TINY_POSITION = 11
MODE_NEAR_LIMIT = 12
MIN_OFFSET = -1
MAX_OFFSET = 1
NEAR_LIMIT_RANGE = 100


def position_limit(depth):
    if depth >= MIN_DEEP_DEPTH:
        return MAX_VALUE
    return 1 << (depth - 1)


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL:
        depth = rng.randint(1, 10)
        position = rng.randint(1, position_limit(depth))
    elif mode == MODE_RANDOM:
        depth = rng.randint(1, MAX_VALUE)
        position = rng.randint(1, position_limit(depth))
    elif mode == MODE_DEEPEST:
        depth = MAX_VALUE
        position = rng.randint(1, MAX_VALUE)
    elif mode == MODE_MAX_POSITION:
        depth = rng.randint(MIN_DEEP_DEPTH, MAX_VALUE)
        position = MAX_VALUE
    elif mode == MODE_WIDTH_BOUNDARY:
        depth = rng.choice((MAX_BITS, MIN_DEEP_DEPTH))
        limit = position_limit(depth)
        boundary = 1 << (MAX_BITS - 1)
        candidates = (1, 2, limit - 1, limit, boundary - 1, boundary, boundary + 1)
        position = rng.choice([value for value in candidates if value <= limit])
    elif mode == MODE_FIRST:
        depth = rng.randint(1, MAX_VALUE)
        position = 1
    elif mode == MODE_LAST:
        depth = rng.randint(1, MAX_BITS)
        position = position_limit(depth)
    elif mode == MODE_POWER_BOUNDARY:
        power = 1 << rng.randrange(MAX_BITS)
        position = max(1, power + rng.randint(MIN_OFFSET, MAX_OFFSET))
        depth = rng.randint((position - 1).bit_length() + 1, MAX_VALUE)
    elif mode == MODE_ALTERNATING:
        width = rng.randint(1, MAX_BITS)
        first_bit = rng.randrange(2)
        path = 0
        for index in range(width):
            path = 2 * path + (first_bit + index) % 2
        position = path + 1
        depth = rng.choice((width + 1, MAX_VALUE, rng.randint(width + 1, MAX_VALUE)))
    elif mode == MODE_MAXIMUM:
        depth = MAX_VALUE
        position = MAX_VALUE
    elif mode == MODE_TINY_POSITION:
        depth = rng.randint(MAX_VALUE // 2, MAX_VALUE)
        position = rng.randint(1, 10)
    elif mode == MODE_NEAR_LIMIT:
        depth = rng.choice((MIN_DEEP_DEPTH, MAX_VALUE))
        position = MAX_VALUE - rng.randrange(NEAR_LIMIT_RANGE)
    else:
        raise ValueError("unknown generator mode")
    return depth, position


def main():
    mode, seed = map(int, sys.argv[1:])
    print(*generate(mode, seed))


if __name__ == "__main__":
    main()
