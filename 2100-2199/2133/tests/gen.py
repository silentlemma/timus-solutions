import random
import sys


MAX_SIZE = 100_000
MAX_HEIGHT = 1_000_000_000
ARGUMENT_COUNT = 3
SMALL_SIZE = 40
SMALL_QUERIES = 150
SMALL_HEIGHT = 20
MEDIUM_QUERIES = 400
HEIGHT_KINDS = 5
QUERY_DENOMINATOR = 4
RARE_QUERY_DENOMINATOR = 100
PLATEAU_WIDTH = 5
LARGE_STEP = 4_003

SMALL_RANDOM = 1
SMALL_DENSE = 2
INCREASING = 3
DECREASING = 4
ALTERNATING = 5
PLATEAUS = 6
ENDPOINTS = 7
REPEATED_UPDATES = 8
WIDE_HEIGHTS = 9
ALL_QUERIES = 10
MOSTLY_UPDATES = 11
MAX_MIXED = 12
MAX_ALTERNATING = 13
MAX_QUERIES = 14
MAX_UPDATES = 15
MAX_BUILDINGS = 16
MAX_SINGLETON = 17
MODE_COUNT = MAX_SINGLETON


def choose_height(rng, heights, wide):
    kind = rng.randrange(HEIGHT_KINDS)
    if kind == 0:
        return 1
    if kind == 1:
        return MAX_HEIGHT
    if kind == 2:
        return rng.choice(heights)
    if kind == HEIGHT_KINDS - 2:
        value = rng.choice(heights) + rng.choice((-1, 0, 1))
        return max(1, min(MAX_HEIGHT, value))
    return rng.randint(1, MAX_HEIGHT if wide else SMALL_HEIGHT)


def mixed_operations(rng, initial, count, mode):
    heights = initial[:]
    operations = []
    repeated_index = rng.randrange(len(heights))
    for step in range(count):
        if mode in (ALL_QUERIES, MAX_QUERIES):
            update = False
        elif mode in (MOSTLY_UPDATES, MAX_UPDATES):
            update = rng.randrange(RARE_QUERY_DENOMINATOR) != 0
        else:
            update = rng.randrange(QUERY_DENOMINATOR) != 0
        if step == count - 1:
            update = False

        if update:
            if mode == ENDPOINTS:
                index = rng.choice((0, len(heights) - 1))
            elif mode in (REPEATED_UPDATES, MAX_SINGLETON):
                index = repeated_index
            else:
                index = rng.randrange(len(heights))

            if mode == MAX_MIXED:
                value = MAX_HEIGHT - step * LARGE_STEP
            elif mode in (ALTERNATING, MAX_ALTERNATING):
                value = rng.choice((1, MAX_HEIGHT))
            elif mode in (SMALL_DENSE, PLATEAUS):
                value = rng.choice((1, 2, SMALL_HEIGHT))
            else:
                value = choose_height(rng, heights, mode >= WIDE_HEIGHTS)
            operations.append((1, index + 1, value))
            heights[index] = value
        else:
            if mode == MAX_MIXED:
                value = MAX_HEIGHT - step * LARGE_STEP + 1
            else:
                value = choose_height(rng, heights, mode >= WIDE_HEIGHTS)
            operations.append((2, value))
    return operations


def generate(mode, seed):
    rng = random.Random(seed)
    if mode >= MAX_MIXED:
        size = 1 if mode == MAX_SINGLETON else MAX_SIZE
        count = 1 if mode == MAX_BUILDINGS else MAX_SIZE
    else:
        size = rng.randint(1, SMALL_SIZE)
        count = rng.randint(1, SMALL_QUERIES)
        if mode in (ALL_QUERIES, MOSTLY_UPDATES):
            count = MEDIUM_QUERIES

    if mode == INCREASING:
        heights = list(range(1, size + 1))
    elif mode == DECREASING:
        heights = list(range(size, 0, -1))
    elif mode in (ALTERNATING, MAX_ALTERNATING):
        heights = [1 if index % 2 else MAX_HEIGHT for index in range(size)]
    elif mode == PLATEAUS:
        heights = [1 + index // PLATEAU_WIDTH % 2 for index in range(size)]
    elif mode == SMALL_DENSE:
        heights = [rng.choice((1, 2, SMALL_HEIGHT)) for _ in range(size)]
    elif mode == MAX_MIXED:
        heights = [1 + index * LARGE_STEP for index in range(size)]
    elif mode in (WIDE_HEIGHTS, ALL_QUERIES, MAX_QUERIES, MAX_BUILDINGS):
        heights = [rng.randint(1, MAX_HEIGHT) for _ in range(size)]
    else:
        heights = [rng.randint(1, SMALL_HEIGHT) for _ in range(size)]

    operations = mixed_operations(rng, heights, count, mode)
    lines = [str(size), " ".join(map(str, heights)), str(count)]
    lines.extend(" ".join(map(str, operation)) for operation in operations)
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = map(int, sys.argv[1:])
    if not 1 <= mode <= MODE_COUNT:
        raise SystemExit("unknown mode")
    sys.stdout.write(generate(mode, seed))


if __name__ == "__main__":
    main()
