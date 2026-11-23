import os
from sys import stdout

from math import gcd, isqrt
from itertools import cycle

WHEEL_PERIOD = 210
WHEEL_START = 11
SMALL_PRIMES = (2, 3, 5, 7)
RESIDUES = tuple(
    value
    for value in range(WHEEL_START, WHEEL_START + WHEEL_PERIOD)
    if gcd(value, WHEEL_PERIOD) == 1
)
STEPS = tuple(b - a for a, b in zip(RESIDUES, RESIDUES[1:] + (RESIDUES[0] + WHEEL_PERIOD,)))


def cube_root(value):
    if value < 2:
        return value
    root = 1 << ((value.bit_length() + 2) // 3)
    while True:
        following = (2 * root + value // (root * root)) // 3
        if following >= root:
            return root
        root = following


def solve(value):
    if value == 0:
        return 1
    remaining = isqrt(value)
    if remaining * remaining == value:
        return remaining // 2 + 1
    root = 1
    for divisor in SMALL_PRIMES:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        root *= divisor ** (exponent // 2)
    remaining = isqrt(value)
    if remaining * remaining == value:
        return root * remaining // 2 + 1
    divisor = WHEEL_START
    steps = cycle(STEPS)
    limit = cube_root(value)
    # The final residual has at most two prime factors, counted with multiplicity.
    while divisor <= limit:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        if exponent:
            root *= divisor ** (exponent // 2)
            remaining = isqrt(value)
            if remaining * remaining == value:
                return root * remaining // 2 + 1
            limit = cube_root(value)
        divisor += next(steps)
    remaining = isqrt(value)
    if remaining * remaining == value:
        root *= remaining
    return root // 2 + 1


print(solve(int(open(0, "rb", buffering=0).read())))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
