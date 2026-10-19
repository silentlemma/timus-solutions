"""Generate from seed and mode: 1 small random, 2 dense maximal,
3 tight windows, 4 widely separated orders, 5 deadline batches,
6 maximal random, 7 odd total workload, 8 impossible common deadline."""

import random
import sys

MAX_COUNT = 50
MAX_TIME = 1000
MIN_TIME = 2
SMALL_COUNT = 6
SMALL_TIME = 8
SPARSE_STEP = 20
SMALL_MODE = 1
DENSE_MODE = 2
TIGHT_MODE = 3
SPARSE_MODE = 4
BATCH_MODE = 5
RANDOM_MODE = 6
ODD_MODE = 7
IMPOSSIBLE_MODE = 8
BATCH_DEADLINES = (100, 101, 150, 151, 500, MAX_TIME)


def generate(seed, mode):
    rng = random.Random(seed)
    n = rng.randint(1, SMALL_COUNT) if mode == SMALL_MODE else MAX_COUNT
    limit = SMALL_TIME if mode == SMALL_MODE else MAX_TIME
    window = rng.randint(MIN_TIME, limit)
    capacity = rng.randint(1, n)
    deadlines = sorted(rng.randint(MIN_TIME, limit) for _ in range(n))
    if mode == DENSE_MODE:
        window, capacity = MAX_TIME, seed % MAX_COUNT + 1
        deadlines = [MAX_TIME] * n
    elif mode == TIGHT_MODE:
        window = MIN_TIME
    elif mode == SPARSE_MODE:
        window = MIN_TIME
        deadlines = [MIN_TIME + SPARSE_STEP * i for i in range(n)]
    elif mode == BATCH_MODE:
        window = rng.randint(MIN_TIME, MAX_COUNT)
        deadlines = sorted(rng.choice(BATCH_DEADLINES) for _ in range(n))
    elif mode == ODD_MODE:
        window, capacity = MAX_TIME, 2
        deadlines = [MAX_TIME] * (n - 1)
    elif mode == IMPOSSIBLE_MODE:
        window, capacity = MIN_TIME, rng.randint(1, MAX_COUNT - 1)
        deadlines = [MIN_TIME] * n
    return window, capacity, deadlines


def render(window, capacity, deadlines):
    return f"{window} {capacity}\n{len(deadlines)}\n{' '.join(map(str, deadlines))}\n"


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode not in range(SMALL_MODE, IMPOSSIBLE_MODE + 1):
        raise ValueError("mode must be from 1 to 8")
    sys.stdout.write(render(*generate(seed, mode)))


if __name__ == "__main__":
    main()
