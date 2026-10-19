"""Sum refill detours using the shorter of columns and a symmetric residue prefix."""

from math import gcd
import sys

MOD = 1000000007


def columns(n, m, k):
    end = n * m - 1
    total = 0
    for c in range(n):
        lower = c * m
        upper = lower + m
        first = lower // k + 1
        last = min(upper, end) // k
        count = last - first + 1
        if count <= 0:
            continue
        if c % 2 == 0:
            a, b = first * k - lower, last * k - lower
        else:
            a, b = upper - first * k, upper - last * k
            if b == 0:
                total += 1
        pair = a + b
        if count % 2 == 0:
            count //= 2
        else:
            pair //= 2
        total += (count % MOD) * (pair % MOD) % MOD
        if total >= MOD:
            total -= MOD
    return total


def residues(n, m, k):
    period = 2 * m
    g = gcd(k, period)
    length = period // g
    refills = (n * m - 1) // k
    cycles, remainder = divmod(refills, length)
    reverse = length - remainder - 1
    work = min(remainder, reverse)
    half = length // 2
    cycle = g * half * (length - half) + 1
    at = 0
    step = k % period
    prefix = 0
    for _ in range(work):
        at += step
        if at >= period:
            at -= period
        prefix += at if at <= m else period - at
    if reverse < remainder:
        prefix = cycle - 1 - prefix
    return cycles * cycle + prefix


def column_cycle(n, m, k):
    period = 2 * (k // gcd(m, k))
    cycles, remainder = divmod(n, period)
    cycle = (columns(period, m, k) + 1) % MOD
    prefix = 0
    if remainder:
        prefix = columns(remainder, m, k)
        if remainder * m % k == 0:
            prefix += m if remainder % 2 else 1
    total = ((cycles % MOD) * cycle + prefix) % MOD
    if n * m % k == 0:
        total -= m if n % 2 else 1
    return total % MOD


def solve(n, m, k):
    base = n * m - 1
    if k > base:
        return base % MOD
    length = 2 * m // gcd(k, 2 * m)
    remainder = base // k % length
    work = min(remainder, length - remainder - 1)
    column_period = 2 * (k // gcd(m, k))
    if 2 * column_period < min(n, work):
        extra = column_cycle(n, m, k)
    else:
        extra = columns(n, m, k) if n < work else residues(n, m, k)
    return (base + 2 * extra) % MOD


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    answers = [str(solve(next(tokens), next(tokens), next(tokens))) for _ in range(next(tokens))]
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
