import random
import sys

MAX_N = 100_000
MAX_K = 100
MAX_VALUE = 1_000_000_000
BOUNDED_VALUE = 100_000
SMALL_K = 7
SMALL_N = 12
FULL_BITS = 30
BOUNDED_BITS = 17
SPARSE_WIDTH = 3
LOW_BITS = BOUNDED_BITS - 1
MIN_BOUNDED_K = SMALL_K + 1
ARGUMENT_COUNT = 3

MODES = (
    "small",
    "sparse",
    "dense",
    "bounded",
    "overlap",
    "powers",
    "keep-one",
    "max-zero",
    "max-small",
    "max-bounded",
)


def sparse_value(rng, bits, width):
    value = 0
    for bit in rng.sample(range(bits), rng.randint(1, width)):
        value |= 1 << bit
    return value


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        size = rng.randint(1, SMALL_N)
        removed = rng.randrange(size)
        limit = MAX_VALUE if removed <= SMALL_K else BOUNDED_VALUE
        choices = [0, 1, 2, limit]
        values = [
            rng.choice(choices) if rng.randrange(2) else rng.randint(0, limit) for _ in range(size)
        ]
    elif mode in ("sparse", "dense"):
        removed = rng.randint(0, SMALL_K)
        size = rng.randint(removed + 1, removed + FULL_BITS)
        if mode == "sparse":
            values = [sparse_value(rng, FULL_BITS, SPARSE_WIDTH) for _ in range(size)]
        else:
            values = [rng.randint(0, MAX_VALUE) for _ in range(size)]
    elif mode in ("bounded", "overlap"):
        removed = rng.randint(MIN_BOUNDED_K, MAX_K)
        size = removed + rng.randint(1, BOUNDED_BITS)
        if mode == "bounded":
            values = [rng.randint(0, BOUNDED_VALUE) for _ in range(size)]
        else:
            values = [sparse_value(rng, LOW_BITS, SPARSE_WIDTH) for _ in range(size)]
            for index in rng.sample(range(size), rng.randint(1, min(size, BOUNDED_BITS))):
                values[index] = 1 << LOW_BITS
                values[index] |= 1 << rng.randrange(LOW_BITS)
    elif mode == "powers":
        removed = rng.randint(MIN_BOUNDED_K, MAX_K)
        size = max(BOUNDED_BITS, removed + rng.randint(1, BOUNDED_BITS))
        values = [1 << bit for bit in range(BOUNDED_BITS)]
        values.extend([0] * (size - BOUNDED_BITS))
    elif mode == "keep-one":
        removed = MAX_K
        values = [rng.randint(0, BOUNDED_VALUE) for _ in range(removed + 1)]
    elif mode == "max-zero":
        removed = 0
        values = [rng.randint(0, MAX_VALUE) for _ in range(MAX_N)]
    elif mode == "max-small":
        removed = SMALL_K
        values = [sparse_value(rng, FULL_BITS, SPARSE_WIDTH) for _ in range(MAX_N)]
    elif mode == "max-bounded":
        removed = MAX_K
        values = [rng.randint(0, BOUNDED_VALUE) for _ in range(MAX_N)]
    else:
        raise ValueError("unknown mode: " + mode)
    rng.shuffle(values)
    return values, removed


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    values, removed = generate(sys.argv[1], int(sys.argv[2]))
    print(len(values), removed)
    print(*values)


if __name__ == "__main__":
    main()
