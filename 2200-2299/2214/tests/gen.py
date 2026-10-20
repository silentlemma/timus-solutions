"""Generate one valid input: python gen.py MODE SEED."""

import random
import sys

MAX_N = 5000
MAX_DAYS = 100
MAX_GAIN = 10**9
SMALL_N = 12
SMALL_DAYS = 8
MEDIUM_N = 80
MEDIUM_DAYS = 20
QUARTER = 4
SPARSE_RATE = 10


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        n = rng.randint(1, SMALL_N)
        days = rng.randint(1, SMALL_DAYS)
    elif mode == "medium":
        n = rng.randint(SMALL_N, MEDIUM_N)
        days = rng.randint(SMALL_DAYS, MEDIUM_DAYS)
    else:
        n, days = MAX_N, MAX_DAYS
    length = rng.randint(1, n)
    moves = rng.randint(0, days)
    if mode not in ("small", "medium"):
        moves = days // 2
    if mode == "unit":
        length = 1
    elif mode == "quarter":
        length = n // QUARTER
    elif mode == "half":
        length = n // 2
    elif mode == "long":
        length = n - 1
    elif mode in ("full", "limit"):
        length = n
    elif mode == "static":
        moves = 0
    elif mode == "daily":
        moves = days

    print(n, days, length, moves)
    for _ in range(days):
        if mode == "zero":
            row = [0] * n
        elif mode == "limit":
            row = [MAX_GAIN] * n
        elif mode == "sparse":
            row = [
                rng.randint(0, MAX_GAIN) if rng.randrange(SPARSE_RATE) == 0 else 0 for _ in range(n)
            ]
        elif mode == "small":
            row = [rng.randint(0, 10) for _ in range(n)]
        else:
            row = [rng.randint(0, MAX_GAIN) for _ in range(n)]
        print(*row)


def main():
    modes = {
        "small",
        "medium",
        "max",
        "unit",
        "quarter",
        "half",
        "long",
        "full",
        "static",
        "daily",
        "zero",
        "limit",
        "sparse",
    }
    if len(sys.argv) != 1 + 2 or sys.argv[1] not in modes:
        raise SystemExit("usage: gen.py MODE SEED; modes: " + ", ".join(sorted(modes)))
    generate(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()
