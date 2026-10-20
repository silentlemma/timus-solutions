import random
import sys

MAX_N = 100_000
MAX_HEIGHT = 1_000_000_000
SMALL_N = 20
PLATEAU_WIDTH = 17
SAW_PERIOD = 31

SMALL = 1
RANDOM = 2
EQUAL = 3
ALTERNATING = 4
INCREASING = 5
DECREASING = 6
PLATEAUS = 7
LOW = 8
SAW = 9
NEAR_LIMIT = 10
ENDPOINTS = 11
MIXED_SIZE = 12


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL:
        n = rng.randint(2, SMALL_N)
        return [rng.randint(1, 10) for _ in range(n)]
    if mode == MIXED_SIZE:
        n = rng.randint(2, MAX_N)
        return [rng.randint(1, MAX_HEIGHT) for _ in range(n)]
    n = MAX_N
    if mode == RANDOM:
        return [rng.randint(1, MAX_HEIGHT) for _ in range(n)]
    if mode == EQUAL:
        n -= seed % 2
        return [MAX_HEIGHT] * n
    if mode == ALTERNATING:
        return [MAX_HEIGHT if (i + seed) % 2 else 1 for i in range(n)]
    if mode in (INCREASING, DECREASING):
        values = [1 + i * (MAX_HEIGHT - 1) // (n - 1) for i in range(n)]
        return values if mode == INCREASING else values[::-1]
    if mode == PLATEAUS:
        values = []
        while len(values) < n:
            width = rng.randint(1, PLATEAU_WIDTH)
            values.extend([rng.randint(1, MAX_HEIGHT)] * width)
        return values[:n]
    if mode == LOW:
        return [rng.randint(1, 2) for _ in range(n)]
    if mode == SAW:
        return [
            1 + ((i + seed) % SAW_PERIOD) * (MAX_HEIGHT - 1) // (SAW_PERIOD - 1) for i in range(n)
        ]
    if mode == NEAR_LIMIT:
        return [MAX_HEIGHT - rng.randint(0, 1) for _ in range(n)]
    if mode == ENDPOINTS:
        return [MAX_HEIGHT] + [1] * (n - 2) + [MAX_HEIGHT]
    raise ValueError("unknown mode")


def main():
    mode, seed = map(int, sys.argv[1:])
    values = generate(mode, seed)
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
