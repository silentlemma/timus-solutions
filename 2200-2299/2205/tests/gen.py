"""Generate one valid input: python gen.py MODE SEED, with modes 1 through 10."""

import random
import sys


MAX_VALUE = 10_000_000
MAX_QUERIES = 500_000
SMALL_MODE = 1
RANDOM_MODE = 2
STRUCTURED_MODE = 3
BOUNDARY_MODE = 4
MAX_RANDOM_MODE = 5
MAX_RESIDUAL_MODE = 6
MAX_SHARED_MODE = 7
MAX_EQUAL_MODE = 8
MAX_COPRIME_MODE = 9
EXHAUSTIVE_MODE = 10
ARGUMENT_COUNT = 3
SMALL_COUNT = 80
SMALL_VALUE = 500
RANDOM_COUNT = 1000
STRUCTURED_COUNT = 200
BOUNDARY_COUNT = 120
EXHAUSTIVE_BOUND = 300
MULTIPLIERS = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 25, 27, 49, 81, 125)
BOUNDARIES = (
    1,
    2,
    3,
    4,
    9,
    25,
    49,
    3137,
    3137 * 3137,
    3137 * 3163,
    3162 * 3162,
    2**23,
    3**14,
    5**10,
    9_999_991,
    MAX_VALUE - 1,
    MAX_VALUE,
)
RESIDUAL_PAIRS = (
    (2**22, 2 * 3**14),
    (2 * 3**14, 2),
    (3**14, 3),
    (5 * 3**13, 5),
    (7 * 3**12, 7),
)
SHARED_PAIRS = (
    (3**14, 5 * 3**13),
    (5 * 3**13, 7 * 3**12),
    (2**23, 3 * 2**21),
    (2**18 * 37, 3**11 * 37),
    (5**10, 3 * 5**9),
)


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL_MODE:
        count = rng.randint(1, SMALL_COUNT)
    elif mode == RANDOM_MODE:
        count = RANDOM_COUNT
    elif mode == STRUCTURED_MODE:
        count = STRUCTURED_COUNT
    elif mode == BOUNDARY_MODE:
        count = BOUNDARY_COUNT
    elif MAX_RANDOM_MODE <= mode <= MAX_COPRIME_MODE:
        count = MAX_QUERIES
    elif mode == EXHAUSTIVE_MODE:
        count = EXHAUSTIVE_BOUND * EXHAUSTIVE_BOUND
    else:
        raise SystemExit("mode must be between 1 and 10")

    sys.stdout.write(str(count) + "\n")
    for index in range(count):
        if mode == SMALL_MODE:
            a = rng.randint(1, SMALL_VALUE)
            b = rng.randint(1, SMALL_VALUE)
        elif mode in (RANDOM_MODE, MAX_RANDOM_MODE):
            a = rng.randint(1, MAX_VALUE)
            b = rng.randint(1, MAX_VALUE)
            if index == 0:
                a = MAX_VALUE
        elif mode == STRUCTURED_MODE:
            left = rng.choice(MULTIPLIERS)
            right = rng.choice(MULTIPLIERS)
            common = rng.randint(1, MAX_VALUE // max(left, right))
            a, b = left * common, right * common
        elif mode == BOUNDARY_MODE:
            a, b = rng.choice(BOUNDARIES), rng.choice(BOUNDARIES)
            if index == 0:
                a, b = MAX_VALUE, MAX_VALUE
        elif mode in (MAX_RESIDUAL_MODE, MAX_SHARED_MODE):
            pairs = RESIDUAL_PAIRS if mode == MAX_RESIDUAL_MODE else SHARED_PAIRS
            a, b = pairs[rng.randrange(len(pairs))]
            if rng.randrange(2):
                a, b = b, a
            if index == 0:
                a, b = MAX_VALUE, MAX_VALUE
        elif mode == MAX_EQUAL_MODE:
            a = b = rng.randint(1, MAX_VALUE)
            if index == 0:
                a = b = MAX_VALUE
        elif mode == MAX_COPRIME_MODE:
            a = rng.randint(1, MAX_VALUE - 1)
            b = a + 1
            if index == 0:
                a, b = MAX_VALUE - 1, MAX_VALUE
        else:
            a = index // EXHAUSTIVE_BOUND + 1
            b = index % EXHAUSTIVE_BOUND + 1
        sys.stdout.write(f"{a} {b}\n")


if __name__ == "__main__":
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    generate(int(sys.argv[1]), int(sys.argv[2]))
