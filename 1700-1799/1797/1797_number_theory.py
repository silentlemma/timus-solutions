import sys
from math import gcd


def floor_sum(n, m, a, b):
    """Sum of (a * i + b) // m over i = 0 .. n - 1."""
    total = 0
    while True:
        if a >= m:
            total += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            total += n * (b // m)
            b %= m
        top = a * n + b
        if top < m:
            return total
        n, b = divmod(top, m)
        m, a = a, m


def count_up_to(limit, x, y):
    """How many numbers from 1 to limit are a * x + b * y with a, b >= 0."""
    g = gcd(x, y)
    limit, x, y = limit // g, x // g, y // g
    # with x and y coprime every such number has exactly one form with
    # b < x; for each b the values of a run from 0 to (limit - b*y) // x
    last = min(limit // y, x - 1)
    forms = floor_sum(last + 1, x, y, limit - y * last) + last + 1
    return forms - 1  # zero is not a volume size


def main():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data[1:])
    out = [count_up_to(hi, x, y) - count_up_to(lo - 1, x, y)
           for _, (x, y, lo, hi) in zip(range(data[0]), zip(it, it, it, it))]
    print("\n".join(map(str, out)))


main()
