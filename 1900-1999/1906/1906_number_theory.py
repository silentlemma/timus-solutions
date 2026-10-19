from math import gcd
import sys

MAX_VALUE = 1_000_000_000


def extended_gcd(a, b):
    old_r, r = a, b
    old_x, x, old_y, y = 1, 0, 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
    return old_r, old_x, old_y


def largest_modulus(d, e, constraint):
    if e % gcd(d, constraint) == 0:
        return constraint
    common = gcd(constraint, e)
    remaining = constraint // common
    forbidden = d // gcd(d, e)
    while True:
        divisor = gcd(remaining, forbidden)
        if divisor == 1:
            return common * remaining
        remaining //= divisor


def witness(d, e, constraint):
    modulus = largest_modulus(d, e, constraint) if constraint else d * MAX_VALUE + 1
    common = gcd(d, modulus)
    reduced = modulus // common
    multiplier = (
        0 if reduced == 1 else e // common * pow(d // common, -1, reduced) % reduced
    )
    return modulus, multiplier


def solve(values):
    n = len(values)
    if values[0] == 0:
        length = 0
        while length < n and values[length] == 0:
            length += 1
        return length, 1, 0
    if n == 1:
        return 1, values[0] + 1, 0
    d, e, constraint = values[0], values[1], 0
    largest = max(values[:2])
    length = 2
    for index in range(1, n - 1):
        a, b = values[index : index + 2]
        if a == 0:
            if b:
                break
            length = index + 2
            continue
        divisor = gcd(d, a)
        if divisor == d:
            following_e = e
        else:
            _, x, y = extended_gcd(d, a)
            following_e = x * e + y * b
        determinant = d // divisor * b - a // divisor * e
        following_constraint = gcd(constraint, determinant)
        if following_constraint:
            following_e %= following_constraint
        following_largest = max(largest, b)
        if following_constraint:
            candidate = largest_modulus(divisor, following_e, following_constraint)
            if candidate <= following_largest:
                break
        d, e, constraint = divisor, following_e, following_constraint
        largest = following_largest
        length = index + 2
    modulus, multiplier = witness(d, e, constraint)
    return length, modulus, multiplier


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(tokens)
    print(*solve([next(tokens) for _ in range(count)]))


if __name__ == "__main__":
    main()
