import math
import sys

# the 15000th prime is 163841
LIMIT = 163842


def main():
    sieve = bytearray([1]) * LIMIT
    sieve[0] = sieve[1] = 0
    for p in range(2, math.isqrt(LIMIT) + 1):
        if sieve[p]:
            sieve[p * p :: p] = bytes(len(range(p * p, LIMIT, p)))
    primes = [p for p in range(LIMIT) if sieve[p]]
    tok = list(map(int, sys.stdin.read().split()))
    print("\n".join(str(primes[n - 1]) for n in tok[1 : tok[0] + 1]))


main()
