import sys
from math import isqrt

ROOT = 10 ** 6  # the cube root of the largest n
FIRST_ODD_PRIME = 3  # n is odd


def main():
    n = int(sys.stdin.read())
    # the gods number a square divisor of n: a number has an odd count of
    # divisors exactly when it is a square
    sieve = bytearray([1]) * (ROOT + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, isqrt(ROOT) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytearray(len(range(p * p, ROOT + 1, p)))
    best = 1
    for p in range(FIRST_ODD_PRIME, ROOT + 1, 2):
        if p * p * p > n:
            break
        if sieve[p] and n % p == 0:
            power = 0
            while n % p == 0:
                n //= p
                power += 1
            best *= p ** (power - power % 2)
    # what is left has no prime factor up to its cube root, so at most two
    # prime factors: it is a square only as the square of one prime
    if isqrt(n) ** 2 == n:
        best *= n
    print(best)


main()
