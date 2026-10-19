import sys
from math import isqrt

PERSISTENT_COUNT = 3


def solve(values):
    limit = isqrt(max(values))
    sieve = bytearray(b"\1") * (limit + 1)
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\0" * (
                (limit - prime * prime) // prime + 1
            )
    primes = [prime for prime in range(2, limit + 1) if sieve[prime]]
    counts = {}
    best = 0
    for value in values:
        for prime in primes:
            if prime * prime > value:
                break
            if value % prime:
                continue
            count = counts.get(prime, 0) + 1
            counts[prime] = count
            if count == PERSISTENT_COUNT:
                return "infinity"
            best = max(best, count)
            while value % prime == 0:
                value //= prime
        if value > 1:
            count = counts.get(value, 0) + 1
            counts[value] = count
            if count == PERSISTENT_COUNT:
                return "infinity"
            best = max(best, count)
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    size = next(tokens)
    print(solve([next(tokens) for _ in range(size)]))
