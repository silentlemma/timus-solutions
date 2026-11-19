import os
from sys import stdout

from math import isqrt

FIRST_ODD_PRIME = 3
FIRST_WHEEL_PRIME = 5
WHEEL_PERIOD = 6


def solve(value):
    if value == 0:
        return 1
    root, divisor, step = 1, 2, 2
    # The final residual has at most two prime factors, counted with multiplicity.
    while divisor * divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        root *= divisor ** (exponent // 2)
        if divisor == 2:
            divisor = FIRST_ODD_PRIME
        elif divisor == FIRST_ODD_PRIME:
            divisor = FIRST_WHEEL_PRIME
        else:
            divisor += step
            step = WHEEL_PERIOD - step
    remaining = isqrt(value)
    if remaining * remaining == value:
        root *= remaining
    return root // 2 + 1


print(solve(int(open(0, "rb", buffering=0).read())))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
