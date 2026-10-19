import random
import sys

MAX_TYPES = 60
MAX_WEIGHT = 10**18
MAX_TARGET = 4 * MAX_WEIGHT
SMALL_TYPES = 10
SMALL_FIRST = 8
SMALL_GAP = 9
LONG_MIN = 45
NEAR_GAP = 1000
GAP_TYPES = 20
MIN_RATIO = 3
MAX_RATIO = 8
DIGIT_CHOICES = 3
BINARY_PREFIX_TYPES = 25
TAIL_TYPES = MAX_TYPES - BINARY_PREFIX_TYPES
TAIL_SLACK = 10**6

SMALL = 1
DOUBLING = 2
NEAR_DOUBLING = 3
LARGE_GAPS = 4
PLANTED = 5
UNREACHABLE = 6
ZERO = 7
FULL = 8
BEYOND = 9
HIGH_COUNT = 10
MAX_LENGTH = 11
MAX_LAST = 12
MAX_SUM = 13
PREFIX_BOUNDARY = 14
WEIGHT_BOUNDARY = 15
MIXED_CHAINS = 16


def sequence(rng, size, limit=MAX_WEIGHT, gap=None):
    values = [rng.randint(1, limit >> (size - 1))]
    for index in range(1, size):
        low = 2 * values[-1]
        high = limit >> (size - index - 1)
        if gap is not None:
            high = min(high, low + gap)
        values.append(rng.randint(low, high))
    return values


def planted(rng, values):
    return sum(value * rng.randrange(DIGIT_CHOICES) for value in values)


def generate(mode, seed):
    rng = random.Random(seed)
    size = rng.randint(1, MAX_TYPES)
    if mode == SMALL:
        size = rng.randint(1, SMALL_TYPES)
        values = [rng.randint(1, SMALL_FIRST)]
        for _ in range(1, size):
            values.append(2 * values[-1] + rng.randint(0, SMALL_GAP))
        target = rng.randint(0, 2 * sum(values) + 1)
    elif mode == DOUBLING:
        first = rng.randint(1, MAX_WEIGHT >> (size - 1))
        values = [first << index for index in range(size)]
        target = first * rng.randint(0, 2 * ((1 << size) - 1) + 1)
    elif mode == NEAR_DOUBLING:
        size = rng.randint(LONG_MIN, MAX_TYPES)
        values = sequence(rng, size, gap=NEAR_GAP)
        target = planted(rng, values)
    elif mode == LARGE_GAPS:
        size = rng.randint(1, GAP_TYPES)
        values = [rng.randint(1, SMALL_FIRST)]
        for index in range(1, size):
            low = 2 * values[-1]
            high = MAX_WEIGHT >> (size - index - 1)
            value = values[-1] * rng.randint(MIN_RATIO, MAX_RATIO)
            value += rng.randint(0, SMALL_GAP)
            values.append(min(high, max(low, value)))
        target = rng.randint(0, 2 * sum(values))
    elif mode == PLANTED:
        values = sequence(rng, size)
        target = planted(rng, values)
    elif mode == UNREACHABLE:
        size = rng.randint(1, MAX_TYPES - 1)
        values = [2 * value for value in sequence(rng, size, MAX_WEIGHT // 2)]
        target = rng.randint(0, 2 * sum(values)) | 1
    elif mode == ZERO:
        values = sequence(rng, size)
        target = 0
    elif mode == FULL:
        values = sequence(rng, size)
        target = 2 * sum(values)
    elif mode == BEYOND:
        values = sequence(rng, size)
        total = 2 * sum(values)
        target = rng.randint(total + 1, MAX_TARGET)
    elif mode == HIGH_COUNT:
        size = MAX_TYPES
        values = [1 << index for index in range(size)]
        target = (1 << (size + 1)) // DIGIT_CHOICES
    elif mode == MAX_LENGTH:
        size = MAX_TYPES
        values = sequence(rng, size)
        target = planted(rng, values)
    elif mode == MAX_LAST or mode == MAX_SUM:
        values = sequence(rng, size - 1, MAX_WEIGHT // 2) if size > 1 else []
        values.append(MAX_WEIGHT)
        target = planted(rng, values) if mode == MAX_LAST else MAX_TARGET
    elif mode == PREFIX_BOUNDARY:
        values = sequence(rng, size, gap=NEAR_GAP)
        end = rng.randint(1, size)
        target = max(0, 2 * sum(values[:end]) + rng.choice((-1, 0, 1)))
    elif mode == WEIGHT_BOUNDARY:
        values = sequence(rng, size, gap=NEAR_GAP)
        target = max(0, rng.choice(values) + rng.choice((-1, 0, 1)))
    elif mode == MIXED_CHAINS:
        rng.seed(seed)
        values = [1 << index for index in range(BINARY_PREFIX_TYPES)]
        for _ in range(TAIL_TYPES):
            values.append(2 * values[-1] + rng.randrange(1, TAIL_SLACK))
        target = sum(value for index, value in enumerate(values) if index % 2 == 0)
    else:
        raise SystemExit("unknown mode")
    return values, target


def main():
    mode, seed = map(int, sys.argv[1:])
    values, target = generate(mode, seed)
    print(len(values), target)
    print(*values)


if __name__ == "__main__":
    main()
