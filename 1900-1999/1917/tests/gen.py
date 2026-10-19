"""seed mode:1 small,2 shuffled unique,3 equal safe,4 equal unsafe,
5 grouped random,6 many spells,7 first barrier,8 prefix barrier,
9 exact billion,10 below billion,11 large groups,12 exact batch,
13 below batch,14 random max,15 descending,16 duplicate budget one.
All modes except1 contain1000coins.
"""

import random
import sys

MAX_COUNT = 1000
MAX_THRESHOLD = 1000000
MAX_BUDGET = 1000000000
SHUFFLED = 2
EQUAL_SAFE = 3
EQUAL_UNSAFE = 4
GROUPED = 5
MANY = 6
FIRST_BARRIER = 7
PREFIX_BARRIER = 8
EXACT_BILLION = 9
BELOW_BILLION = 10
LARGE_GROUPS = 11
EXACT_BATCH = 12
BELOW_BATCH = 13
RANDOM_MAX = 14
DESCENDING = 15
BUDGET_ONE = 16


def make_case(seed, mode):
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(1, 30) for _ in range(rng.randint(1, 9))]
        return values, rng.randint(1, 200)
    if mode in (SHUFFLED, MANY, DESCENDING):
        values = list(range(1, MAX_COUNT + 1))
        budget = (
            rng.randint(MAX_COUNT, MAX_COUNT * MAX_COUNT)
            if mode == SHUFFLED
            else MAX_COUNT
        )
        if mode == DESCENDING:
            values.reverse()
            return values, budget
    elif mode in (EQUAL_SAFE, EQUAL_UNSAFE):
        values = [MAX_THRESHOLD] * MAX_COUNT
        budget = MAX_BUDGET - int(mode == EQUAL_UNSAFE)
    elif mode == GROUPED:
        palette = [rng.randint(1, MAX_THRESHOLD) for _ in range(20)]
        values = [rng.choice(palette) for _ in range(MAX_COUNT)]
        budget = rng.randint(1, MAX_BUDGET)
    elif mode == FIRST_BARRIER:
        values = [rng.randint(2, MAX_THRESHOLD) for _ in range(MAX_COUNT)]
        budget = 1
    elif mode == PREFIX_BARRIER:
        values = [1] * 100 + [100] * (MAX_COUNT - 100)
        budget = 100
    elif mode in (EXACT_BILLION, BELOW_BILLION):
        values = list(range(MAX_THRESHOLD - MAX_COUNT + 1, MAX_THRESHOLD + 1))
        budget = MAX_BUDGET - int(mode == BELOW_BILLION)
    elif mode == LARGE_GROUPS:
        values = [
            MAX_THRESHOLD // 10 * group for group in range(1, 11) for _ in range(100)
        ]
        budget = 10000000
    elif mode in (EXACT_BATCH, BELOW_BATCH):
        values = [1] * (MAX_COUNT // 2) + [2] * (MAX_COUNT // 2)
        budget = 2 * MAX_COUNT - int(mode == BELOW_BATCH)
    elif mode == RANDOM_MAX:
        values = [rng.randint(1, MAX_THRESHOLD) for _ in range(MAX_COUNT)]
        budget = rng.randint(1, MAX_BUDGET)
    elif mode == BUDGET_ONE:
        values, budget = [1] * MAX_COUNT, 1
    else:
        raise ValueError("unknown generator mode")
    rng.shuffle(values)
    return values, budget


def main():
    values, budget = make_case(int(sys.argv[1]), int(sys.argv[2]))
    print(len(values), budget)
    print(*values)


if __name__ == "__main__":
    main()
