import sys


def divisor_sum(n):
    """The sum of all divisors of n by trial division."""
    total, d = 0, 1
    while d * d <= n:
        if n % d == 0:
            total += d if d * d == n else d + n // d
        d += 1
    return total


def main():
    lo, hi = map(int, sys.stdin.read().split())
    if lo == 1:
        # 1 has no proper divisors at all
        print(1)
        return
    # a prime p has the ratio 1/p, and the largest prime in range beats every
    # composite there (it is above hi / 2 by Bertrand's postulate), so only a
    # range without primes, at most 113 numbers here, needs comparing
    for n in range(hi, lo - 1, -1):
        if divisor_sum(n) == n + 1:
            print(n)
            return
    best = lo
    for n in range(lo + 1, hi + 1):
        # sigma(n) / n < sigma(best) / best, the smaller number winning a tie
        if divisor_sum(n) * best < divisor_sum(best) * n:
            best = n
    print(best)


main()
