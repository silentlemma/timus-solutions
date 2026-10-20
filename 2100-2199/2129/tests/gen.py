"""Generate one deterministic batch from a mode and a seed.

Modes: small random, full bounds, representable sums, binary boundaries,
large bases, and maximum-size binary stress, in that order.
"""

import random
import sys

MAX_VALUE = 10**18
MAX_CASES = 100
MAX_COINS = 100
SMALL_AMOUNT = 512
SMALL_BASE = 20
TERNARY_BASE = 3
QUINARY_BASE = 5
SQUARE_ROOT_LIMIT = 10**9
SPARSE_BITS = 10
ARGUMENT_COUNT = 3
MAX_EXPONENT = MAX_VALUE.bit_length() - 1
MIN_STRESS_EXPONENT = MAX_EXPONENT - 10

SMALL_MODE = 1
BOUNDS_MODE = 2
CONSTRUCTED_MODE = 3
BINARY_MODE = 4
LARGE_BASE_MODE = 5
STRESS_MODE = 6


def small_case(rng):
    return (
        rng.randint(1, SMALL_AMOUNT),
        rng.randint(2, SMALL_BASE),
        rng.randint(1, MAX_COINS),
    )


def bounds_case(rng):
    base = rng.choice(
        [
            rng.randint(2, MAX_VALUE),
            rng.randint(2, MAX_COINS + 1),
            MAX_VALUE - 1,
            MAX_VALUE,
        ]
    )
    count = rng.choice([1, MAX_COINS, rng.randint(1, MAX_COINS)])
    return rng.randint(1, MAX_VALUE), base, count


def constructed_case(rng):
    base = rng.choice([2, TERNARY_BASE, QUINARY_BASE, 10, rng.randint(2, MAX_VALUE)])
    count = rng.randint(1, MAX_COINS)
    largest_coin = MAX_VALUE // count
    powers = [1]
    while powers[-1] <= largest_coin // base:
        powers.append(powers[-1] * base)
    amount = sum(rng.choice(powers) for _ in range(count))
    return amount, base, count


def binary_case(rng):
    exponent = rng.randint(0, MAX_EXPONENT)
    amount = (1 << exponent) + rng.randint(-MAX_COINS, MAX_COINS)
    amount = max(1, min(MAX_VALUE, amount))
    count = rng.choice([1, amount.bit_count(), MAX_COINS, rng.randint(1, MAX_COINS)])
    return amount, 2, count


def large_base_case(rng):
    base = rng.choice(
        [
            MAX_COINS,
            MAX_COINS + 1,
            SQUARE_ROOT_LIMIT,
            SQUARE_ROOT_LIMIT + 1,
            MAX_VALUE - 1,
            MAX_VALUE,
            rng.randint(MAX_COINS + 1, MAX_VALUE),
        ]
    )
    count = rng.randint(1, MAX_COINS)
    high_coins = rng.randint(0, count)
    constructed = high_coins * base + count - high_coins
    amount = rng.choice(
        [
            rng.randint(1, MAX_VALUE),
            base + rng.randint(0, MAX_COINS),
            base * base + rng.randint(-MAX_COINS, MAX_COINS),
            constructed,
        ]
    )
    return max(1, min(MAX_VALUE, amount)), base, count


def stress_case(rng):
    exponent = rng.randint(MIN_STRESS_EXPONENT, MAX_EXPONENT)
    amount = 1 << exponent
    for _ in range(rng.randint(0, SPARSE_BITS)):
        candidate = amount | (1 << rng.randrange(exponent))
        if candidate <= MAX_VALUE:
            amount = candidate
    return amount, 2, MAX_COINS


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = map(int, sys.argv[1:])
    generators = {
        SMALL_MODE: small_case,
        BOUNDS_MODE: bounds_case,
        CONSTRUCTED_MODE: constructed_case,
        BINARY_MODE: binary_case,
        LARGE_BASE_MODE: large_base_case,
        STRESS_MODE: stress_case,
    }
    if mode not in generators:
        raise SystemExit("unknown mode")
    rng = random.Random(seed)
    cases = [generators[mode](rng) for _ in range(MAX_CASES)]
    if mode in (BOUNDS_MODE, LARGE_BASE_MODE):
        cases[0] = MAX_VALUE, MAX_VALUE, MAX_COINS
    if mode == STRESS_MODE:
        cases[0] = MAX_VALUE, 2, MAX_COINS
    print(len(cases))
    for case in cases:
        print(*case)


if __name__ == "__main__":
    main()
