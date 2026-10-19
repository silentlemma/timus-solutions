"""Generate seed/mode: 1 small; 2 prime; 3 composite; 4 wide alternating;
5 constant; 6 zero tail; 7 zero; 8 corrupted tail; 9 random; 10 stripped modulus;
11 decreasing geometric; 12 wide witness followed by an impossible extension."""

import random
import sys

MAX_COUNT = 10_000
MAX_VALUE = 1_000_000_000
PRIME_MODULUS = 999_999_937
PRIME_MULTIPLIER = 192_837_465
COMPOSITE_MODULUS = 999_999_936
COMPOSITE_MULTIPLIER = 123_456
WIDE_LEFT = 999_999_937
WIDE_RIGHT = 123_456_789
WIDE_PREFIX = [315_447_290, 935_357_822, 999_906_653, 0]


def recurrence(count, initial, modulus, multiplier):
    values = [initial]
    for _ in range(count - 1):
        values.append(values[-1] * multiplier % modulus)
    return values


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == 1:
        return [rng.randrange(5) for _ in range(10)]
    if mode in (2, 8):
        values = recurrence(MAX_COUNT, 7, PRIME_MODULUS, PRIME_MULTIPLIER)
        if mode == 8:
            values[-1] = (values[-1] + 1) % PRIME_MODULUS
        return values
    if mode == 3:
        return recurrence(MAX_COUNT, 23456, COMPOSITE_MODULUS, COMPOSITE_MULTIPLIER)
    if mode == 4:
        return [WIDE_LEFT if i % 2 == 0 else WIDE_RIGHT for i in range(MAX_COUNT)]
    if mode == 5:
        return [MAX_VALUE] * MAX_COUNT
    if mode == 6:
        return [123456789] + [0] * (MAX_COUNT - 1)
    if mode == 7:
        return [0] * MAX_COUNT
    if mode == 9:
        return [rng.randrange(MAX_VALUE + 1) for _ in range(MAX_COUNT)]
    if mode == 10:
        return recurrence(MAX_COUNT, 12, 13, 11)
    if mode == 11:
        return [1 << bit for bit in range(29, -1, -1)]
    if mode == 12:
        return WIDE_PREFIX + [
            rng.randrange(MAX_VALUE + 1) for _ in range(MAX_COUNT - len(WIDE_PREFIX))
        ]
    raise ValueError("Unknown mode")


def main():
    values = generate(*map(int, sys.argv[1:]))
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
