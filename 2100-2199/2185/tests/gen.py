"""Print one deterministic valid input: python gen.py MODE SEED.
Modes 1..3 are small; modes 4..13 cover maximal counts and boundary patterns.
"""

import random
import sys

MAX_COUNT = 1_000_000
MAX_VALUE = 1_000_000
SMALL_COUNT = 40
SMALL_VALUE = 30
DOMAIN_LIMIT = 80
MEDIUM_COUNT = 300

SMALL_MODE = 1
DOMAIN_MODE = 2
BOUNDARY_MODE = 3
LEFT_CHAIN_MODE = 4
RIGHT_CHAIN_MODE = 5
RANDOM_MODE = 6
NEGATIVE_MODE = 7
ZERO_MODE = 8
POSITIVE_MODE = 9
FOLD_MODE = 10
ONE_QUERY_MODE = 11
ONE_STEP_MODE = 12
EXTREME_MODE = 13


def sweep():
    queries = [i if i % 2 == 0 else -i - 1 for i in range(MAX_COUNT)]
    queries[0] = MAX_VALUE
    return queries


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL_MODE:
        count = rng.randint(1, SMALL_COUNT)
        query_count = rng.randint(1, SMALL_COUNT)
        steps = [rng.randint(-SMALL_VALUE, SMALL_VALUE) for _ in range(count)]
        queries = [rng.randint(-SMALL_VALUE, SMALL_VALUE) for _ in range(query_count)]
    elif mode == DOMAIN_MODE:
        bound = rng.randint(1, DOMAIN_LIMIT)
        steps = [rng.randint(-bound, bound) for _ in range(rng.randint(1, SMALL_COUNT))]
        queries = list(range(-bound, bound + 1))
        rng.shuffle(queries)
    elif mode == BOUNDARY_MODE:
        choices = (-MAX_VALUE, -MAX_VALUE + 1, -1, 0, 1, MAX_VALUE - 1, MAX_VALUE)
        steps = [rng.choice(choices) for _ in range(rng.randint(1, MEDIUM_COUNT))]
        queries = list(choices) * rng.randint(1, SMALL_COUNT)
        rng.shuffle(queries)
    elif mode == LEFT_CHAIN_MODE:
        steps, queries = [1] * MAX_COUNT, sweep()
    elif mode == RIGHT_CHAIN_MODE:
        steps, queries = [MAX_VALUE] + [1] * (MAX_COUNT - 1), sweep()
    elif mode == RANDOM_MODE:
        steps = [rng.randint(-MAX_VALUE, MAX_VALUE) for _ in range(MAX_COUNT)]
        queries = [rng.randint(-MAX_VALUE, MAX_VALUE) for _ in range(MAX_COUNT)]
        queries[0] = MAX_VALUE
    elif mode == NEGATIVE_MODE:
        steps, queries = [-MAX_VALUE] * MAX_COUNT, sweep()
    elif mode == ZERO_MODE:
        steps, queries = [0] * MAX_COUNT, sweep()
    elif mode == POSITIVE_MODE:
        steps, queries = [MAX_VALUE] * MAX_COUNT, sweep()
    elif mode == FOLD_MODE:
        steps = [rng.randint(1, MAX_VALUE) for _ in range(MAX_COUNT)]
        queries = sweep()
    elif mode == ONE_QUERY_MODE:
        steps = [rng.randint(-MAX_VALUE, MAX_VALUE) for _ in range(MAX_COUNT)]
        queries = [rng.choice((-MAX_VALUE, -1, 0, MAX_VALUE))]
    elif mode == ONE_STEP_MODE:
        steps = [rng.randint(-MAX_VALUE, MAX_VALUE)]
        queries = sweep()
    elif mode == EXTREME_MODE:
        choices = (-MAX_VALUE, -MAX_VALUE + 1, -1, 0, 1, MAX_VALUE - 1, MAX_VALUE)
        steps = [rng.choice(choices) for _ in range(MAX_COUNT)]
        queries = [rng.choice(choices) for _ in range(MAX_COUNT)]
        queries[0] = MAX_VALUE
    else:
        raise ValueError("mode must be between 1 and 13")
    return steps, queries


def main():
    mode, seed = map(int, sys.argv[1:])
    steps, queries = generate(mode, seed)
    sys.stdout.write(f"{len(steps)} {len(queries)}\n")
    sys.stdout.write(" ".join(map(str, steps)) + "\n")
    sys.stdout.write("\n".join(map(str, queries)) + "\n")


if __name__ == "__main__":
    main()
