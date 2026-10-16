import sys
from math import isqrt

MOD = 10 ** 9 + 7


def mul(x, y):
    """Product of 2 x 2 matrices given as (a, b, c, d) rows first."""
    a, b, c, d = x
    e, f, g, h = y
    return ((a * e + b * g) % MOD, (a * f + b * h) % MOD,
            (c * e + d * g) % MOD, (c * f + d * h) % MOD)


def term(a):
    # [p_k p_(k-1); q_k q_(k-1)] grows by the factor [a 1; 1 0]
    return (a % MOD, 1, 1, 0)


def main():
    x, k = map(int, sys.stdin.read().split())
    a0 = isqrt(x)
    # the partial quotients of sqrt(x) repeat with a period that ends at
    # the first term equal to 2 a0
    period = []
    m, d, a = 0, 1, a0
    while a != 2 * a0:
        m = d * a - m
        d = (x - m * m) // d
        a = (a0 + m) // d
        period.append(a)
    cycle = (1, 0, 0, 1)
    for a in period:
        cycle = mul(cycle, term(a))
    result = term(a0)
    full, rest = divmod(k, len(period))
    power = cycle
    while full:
        if full & 1:
            result = mul(result, power)
        power = mul(power, power)
        full >>= 1
    for a in period[:rest]:
        result = mul(result, term(a))
    # convergents are always in lowest terms
    p, _, q, _ = result
    print("%d/%d" % (p, q))


main()
