"""Print one pair of positive binary integers: python gen.py MODE SEED."""

import random
import sys

MAX_BITS = 1_000_000
SMALL_BITS = 64
MAX_BLOCK = 1024
SPARSE_ONES = 64
SMALL = 1
RANDOM = 2
MAX_RANDOM = 3
LONG_CHAIN = 4
EQUAL = 5
DISJOINT = 6
BLOCKS = 7
STOPPED_CHAIN = 8
SPARSE = 9
BOUNDARY = 10
DENSE = 11


def positive_bits(rng, size):
    if size == 1:
        return "1"
    return "1" + format(rng.getrandbits(size - 1), "b").zfill(size - 1)


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == SMALL:
        x = positive_bits(rng, rng.randint(1, SMALL_BITS))
        y = positive_bits(rng, rng.randint(1, SMALL_BITS))
    elif mode == RANDOM:
        x = positive_bits(rng, rng.randint(1, MAX_BITS))
        y = positive_bits(rng, rng.randint(1, MAX_BITS))
    elif mode == MAX_RANDOM:
        x = positive_bits(rng, MAX_BITS)
        y = positive_bits(rng, MAX_BITS)
    elif mode == LONG_CHAIN:
        x, y = "1" * MAX_BITS, "1"
        if seed % 2:
            x, y = y, x
    elif mode == EQUAL:
        x = y = positive_bits(rng, MAX_BITS)
    elif mode == DISJOINT:
        x = positive_bits(rng, MAX_BITS - 1) + "0"
        y = "".join("1" if bit == "0" else "0" for bit in x).lstrip("0")
    elif mode == BLOCKS:
        block = "1" + "0" * rng.randint(0, MAX_BLOCK - 1)
        x = "1" * MAX_BITS
        y = (block * (MAX_BITS // len(block) + 1))[:MAX_BITS]
    elif mode == STOPPED_CHAIN:
        x, y = "10" + "1" * (MAX_BITS - 2), "1"
    elif mode == SPARSE:
        x = ["0"] * MAX_BITS
        y = ["0"] * MAX_BITS
        x[0] = y[0] = "1"
        for _ in range(SPARSE_ONES):
            x[rng.randrange(MAX_BITS)] = "1"
            y[rng.randrange(MAX_BITS)] = "1"
        x, y = "".join(x), "".join(y)
    elif mode == BOUNDARY:
        power = 1 << rng.randrange(MAX_BITS.bit_length())
        size = min(MAX_BITS, max(1, power + rng.randint(-1, 1)))
        x = positive_bits(rng, size)
        y = positive_bits(rng, rng.randint(1, size))
    elif mode == DENSE:
        x = y = "1" * MAX_BITS
    else:
        raise SystemExit("unknown mode")
    print(x)
    print(y)


if __name__ == "__main__":
    main()
