import os
import sys
from math import isqrt

TARGET = 20
FIRST_ODD = 3
FIRST_WHEEL = 5
WHEEL = 6


def has_target_factors(n):
    twos = (n & -n).bit_length() - 1
    remaining = TARGET - twos
    n >>= twos
    if remaining <= 0:
        return remaining == 0 and n == 1
    while n % FIRST_ODD == 0:
        n //= FIRST_ODD
        remaining -= 1
        if remaining == 0:
            return n == 1
    if remaining <= 2:
        root = isqrt(n)
        if root * root == n:
            # A square has an even prime-factor count. Exactly two means a prime root.
            if remaining != 2 or root < 2:
                return False
            divisor, step = FIRST_WHEEL, 2
            # Factors two and three were already removed from n and its root.
            while divisor * divisor <= root:
                if root % divisor == 0:
                    return False
                divisor += step
                step = WHEEL - step
            return True
    divisor, step = FIRST_WHEEL, 2
    while divisor * divisor <= n:
        # All remaining prime factors are at least this untested wheel value.
        if remaining > 2 and divisor**remaining > n:
            return False
        while n % divisor == 0:
            n //= divisor
            remaining -= 1
            if remaining == 0:
                return n == 1
        divisor += step
        step = WHEEL - step
    return remaining == (1 if n > 1 else 0)


answer = has_target_factors(int(sys.stdin.buffer.read()))
os.write(1, b"Yes\n" if answer else b"No\n")
os._exit(0)
