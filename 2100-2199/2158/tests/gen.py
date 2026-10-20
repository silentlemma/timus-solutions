"""Generate impossible instances, whose only valid output is -1."""

import random
import sys

MAX_SIZE = 50000
MAX_VALUE = 1000000000
SMALL_MIN = 7
SMALL_MAX = 12
SMALL_VALUE = 40
CORE_SIZE = 6
HOLE_COUNT = 3
QUARTERS = 4
MODE_SMALL = 1
MODE_ZEROS = 2
MODE_DUPLICATES = 3
MODE_DISTINCT = 4
MODE_ALMOST = 5


def arithmetic(values):
    return len(values) <= 2 or len({b - a for a, b in zip(values, values[1:])}) == 1


def geometric(values):
    if 0 in values:
        return all(value == 0 for value in values)
    return all(a * c == b * b for a, b, c in zip(values, values[1:], values[2:]))


def possible(values):
    size = len(values)
    for mask in range(1, (1 << size) - 1):
        first = [value for i, value in enumerate(values) if mask >> i & 1]
        if not arithmetic(first):
            continue
        second = [value for i, value in enumerate(values) if not (mask >> i & 1)]
        if geometric(second):
            return True
    return False


def generate(mode, rng):
    if mode == MODE_SMALL:
        while True:
            size = rng.randint(SMALL_MIN, SMALL_MAX)
            values = sorted(rng.randrange(SMALL_VALUE + 1) for _ in range(size))
            if not possible(values):
                break
    elif mode == MODE_ZEROS:
        # A zero GP is constant; two other copies and a distinct value cannot fit the AP.
        values = [0, 0, 1, 1, 2, MAX_VALUE]
        values += [rng.randrange(MAX_VALUE + 1) for _ in range(MAX_SIZE - CORE_SIZE)]
    elif mode == MODE_DUPLICATES:
        repeated, other, distinct = rng.sample(range(1, MAX_VALUE), HOLE_COUNT)
        # Three copies force one progression constant, leaving an impossible other side.
        values = [repeated] * HOLE_COUNT + [other] * 2 + [distinct]
        values += [rng.randint(1, MAX_VALUE) for _ in range(MAX_SIZE - CORE_SIZE - 1)]
        values.append(MAX_VALUE)
    elif mode == MODE_DISTINCT:
        span = MAX_SIZE + HOLE_COUNT - 1
        first = MAX_VALUE - span
        holes = {first + span * part // QUARTERS for part in range(1, QUARTERS)}
        # Here a distinct integer GP triple has a span greater than this entire interval.
        values = [value for value in range(first, MAX_VALUE + 1) if value not in holes]
    elif mode == MODE_ALMOST:
        values = list(range(1, MAX_SIZE - CORE_SIZE + 1))
        values += [MAX_VALUE] * HOLE_COUNT + [MAX_VALUE - 1] * 2 + [MAX_VALUE - 2]
    else:
        raise ValueError("unknown mode")
    rng.shuffle(values)
    return values


def main():
    mode, seed = map(int, sys.argv[1:])
    values = generate(mode, random.Random(seed))
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
