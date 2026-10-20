"""Generate a valid position: python gen.py MODE SEED."""

import random
import sys

MIN_COLUMNS = 3
MAX_COLUMNS = 1_000_000_000
SMALL_COLUMNS = 16
TWO_TAIL_MIN_COLUMNS = 4


def generate(mode, seed):
    rng = random.Random(seed)
    n = rng.randint(MIN_COLUMNS, MAX_COLUMNS)
    r1, r2 = rng.randint(1, 2), rng.randint(1, 2)
    if mode == "small":
        n = rng.randint(MIN_COLUMNS, SMALL_COLUMNS)
    elif mode == "max":
        n = MAX_COLUMNS
    elif mode == "two":
        n = rng.randint(TWO_TAIL_MIN_COLUMNS, MAX_COLUMNS)

    c1, c2 = rng.randint(1, n), rng.randint(1, n)
    if mode == "same-row":
        r2 = r1
        while c1 == c2:
            c2 = rng.randint(1, n)
    elif mode == "same-column":
        c2 = c1
        r2 = 2 if r1 == 1 else 1
    elif mode == "adjacent":
        c1 = rng.randint(1, n - 1)
        c2 = c1 + 1
    elif mode == "balanced":
        tail = rng.randint(0, (n - 1) // 2)
        c1, c2 = tail + 1, n - tail
    elif mode in ("unit", "two"):
        difference = 1 if mode == "unit" else 2
        tail = rng.randint(0, (n - difference - 2) // 2)
        left, right = tail, tail + difference
        if rng.getrandbits(1):
            left, right = right, left
        c1, c2 = left + 1, n - right
        r2 = 2 if r1 == 1 else 1
    elif mode == "edges":
        c1, c2 = rng.choice((1, 2, n - 1, n)), rng.choice((1, 2, n - 1, n))
    elif mode not in ("small", "random", "max"):
        raise ValueError("unknown mode: " + mode)

    if c1 == c2:
        r2 = 2 if r1 == 1 else 1
    if rng.getrandbits(1):
        c1, c2 = n + 1 - c1, n + 1 - c2
    if rng.getrandbits(1):
        r1 = 2 if r1 == 1 else 1
        r2 = 2 if r2 == 1 else 1
    return n, r1, c1, r2, c2


def main():
    mode, seed = sys.argv[1:]
    n, r1, c1, r2, c2 = generate(mode, int(seed))
    print(n)
    print(r1, c1)
    print(r2, c2)


if __name__ == "__main__":
    main()
