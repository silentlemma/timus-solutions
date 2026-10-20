"""Print one valid input for MODE SEED.

Modes 1..12: small random, maximal random, all maximal, sparse maximal,
planted split, large prime split, prime-factor chain, distant split,
divisible values, consecutive Fibonacci values, mirrored powers, and two large chests.
"""

import random
import sys

MAX_COUNT = 100_000
MAX_VALUE = 1_000_000_000_000
SMALL_COUNT = 12
SMALL_VALUE = 30
MEDIUM_COUNT = 2_000
MAX_MULTIPLIER = 100
LARGE_PRIME = 999_999_999_989
CHAIN_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
FIBONACCI_PAIR = (591_286_729_879, 956_722_026_041)
MAX_POWER = 39

SMALL_MODE = 1
RANDOM_MODE = 2
MAXIMAL_MODE = 3
SPARSE_MODE = 4
SPLIT_MODE = 5
PRIME_MODE = 6
CHAIN_MODE = 7
DISTANT_MODE = 8
DIVISIBLE_MODE = 9
FIBONACCI_MODE = 10
POWERS_MODE = 11
TWO_CHESTS_MODE = 12


def plant_split(rng, count, divisor):
    limit = min(MAX_MULTIPLIER, MAX_VALUE // divisor - 1)
    values = [rng.randint(0, limit) * divisor for _ in range(count)]
    left, right = rng.sample(range(count), 2)
    remainder = rng.randint(1, divisor - 1)
    values[left] += remainder
    values[right] += divisor - remainder
    return values


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL_MODE:
        count = rng.randint(2, SMALL_COUNT)
        values = [rng.randint(0, SMALL_VALUE) for _ in range(count)]
    elif mode == RANDOM_MODE:
        values = [rng.randint(0, MAX_VALUE) for _ in range(MAX_COUNT)]
    elif mode == MAXIMAL_MODE:
        values = [MAX_VALUE] * MAX_COUNT
    elif mode == SPARSE_MODE:
        values = [0] * MAX_COUNT
        for index in rng.sample(range(MAX_COUNT), rng.randint(1, 2)):
            values[index] = rng.randint(1, MAX_VALUE)
    elif mode == SPLIT_MODE:
        count = rng.randint(2, MEDIUM_COUNT)
        divisor = rng.randint(2, MAX_VALUE // MAX_MULTIPLIER)
        values = plant_split(rng, count, divisor)
    elif mode == PRIME_MODE:
        values = [LARGE_PRIME] * MAX_COUNT
        left, right = rng.sample(range(MAX_COUNT), 2)
        remainder = rng.randint(1, LARGE_PRIME - 1)
        values[left] = remainder
        values[right] = LARGE_PRIME - remainder
    elif mode == CHAIN_MODE:
        product = 1
        for prime in CHAIN_PRIMES:
            product *= prime
        values = []
        for prime in CHAIN_PRIMES:
            part = product // prime
            values.extend((part, product - part))
        values.extend([0] * rng.randint(0, MEDIUM_COUNT))
        rng.shuffle(values)
    elif mode == DISTANT_MODE:
        divisor = rng.randint(2, MAX_VALUE // MAX_MULTIPLIER)
        values = [rng.randint(1, MAX_MULTIPLIER) * divisor for _ in range(MAX_COUNT)]
        remainder = rng.randint(1, divisor - 1)
        values[0] = remainder
        values[-1] = divisor - remainder
    elif mode == DIVISIBLE_MODE:
        count = rng.randint(2, MEDIUM_COUNT)
        divisor = rng.randint(1, MAX_VALUE // MAX_MULTIPLIER)
        values = [rng.randint(1, MAX_MULTIPLIER) * divisor for _ in range(count)]
    elif mode == FIBONACCI_MODE:
        count = rng.randint(2, MEDIUM_COUNT)
        values = [FIBONACCI_PAIR[index % 2] for index in range(count)]
        rng.shuffle(values)
    elif mode == POWERS_MODE:
        descending = [2**power for power in range(MAX_POWER, -1, -1)]
        values = descending + [0] * (MAX_COUNT - 2 * len(descending)) + descending[::-1]
        # Balance the total to preserve both long gcd chains.
        values[MAX_COUNT // 2] = (-sum(values)) % (2**MAX_POWER)
    elif mode == TWO_CHESTS_MODE:
        values = [rng.randint(MAX_VALUE // 2 + 1, MAX_VALUE) for _ in range(2)]
    else:
        raise ValueError("mode must be between 1 and 12")
    if not any(values):
        values[0] = 1
    return values


def main():
    mode, seed = map(int, sys.argv[1:])
    values = generate(mode, seed)
    print(len(values))
    print(*values)


if __name__ == "__main__":
    main()
