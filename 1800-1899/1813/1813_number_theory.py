import sys

LIMIT = 31623  # above the square root of 10^9
FOUR = 4


def main():
    sieve = bytearray([1]) * LIMIT
    primes = []
    for p in range(2, LIMIT):
        if sieve[p]:
            primes.append(p)
            sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
    out = []
    for m in map(int, sys.stdin.read().split()):
        # by the Hull-Dobell theorem the full cycles come from a - 1
        # divisible by every prime of m, and by 4 when 4 divides m, with
        # any b coprime to m; so a runs over 1, 1 + c, ..., below m
        c, rest = 1, m
        for p in primes:
            if p * p > rest:
                break
            if rest % p == 0:
                c *= p
                while rest % p == 0:
                    rest //= p
        if rest > 1:
            c *= rest
        if m % FOUR == 0:
            c *= 2
        out.append((m - c + 2) // 2)
    print("\n".join(map(str, out)))


main()
