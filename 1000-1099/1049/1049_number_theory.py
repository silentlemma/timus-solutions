import sys
from collections import Counter

BASE = 10


def main():
    # the exponents of the primes in the product of all the numbers
    exponent = Counter()
    for x in map(int, sys.stdin.read().split()):
        p = 2
        while p * p <= x:
            while x % p == 0:
                exponent[p] += 1
                x //= p
            p += 1
        if x > 1:
            exponent[x] += 1
    # a divisor picks each prime from 0 to its exponent times
    last = 1
    for e in exponent.values():
        last = last * (e + 1) % BASE
    print(last)


main()
