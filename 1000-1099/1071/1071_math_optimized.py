from math import isqrt
import sys


def fits(x, y, base):
    # A subsequence can also be matched from the least significant end.
    wanted = y % base
    while x > y:
        x, digit = divmod(x, base)
        if digit == wanted:
            y //= base
            if y == 0:
                return True
            wanted = y % base
    return x == y


def answer(x, y):
    boundary = isqrt(x) + 1
    for base in range(2, boundary):
        if fits(x, y, base):
            return base

    # In larger bases x has two digits, so y is the quotient or the remainder.
    quotient_base = max(boundary, x // (y + 1) + 1)
    best = quotient_base if quotient_base <= x // y else x + 1

    difference = x - y
    minimum_base = max(boundary, y + 1)
    # A larger divisor of the complement gives a smaller base.
    for divisor in range(difference // minimum_base, 0, -1):
        if difference % divisor == 0:
            best = min(best, difference // divisor)
            break
    return best if best <= x else None


def main():
    x, y = map(int, sys.stdin.buffer.read().split())
    result = answer(x, y)
    print("No solution" if result is None else result)


if __name__ == "__main__":
    main()
