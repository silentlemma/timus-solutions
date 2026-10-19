"""Usage: gen.py SEED MODE; ones,distinct,paired,late,squares,powers,limit,random.

All modes use 10000 values. Large primes are certified by a segmented sieve.
"""

from math import isqrt
import random
import sys

SIZE = 10000
LIMIT = 10000000
SEGMENT_START = 9800000


def small_primes(limit):
    composite = bytearray(limit + 1)
    for prime in range(2, isqrt(limit) + 1):
        if not composite[prime]:
            composite[prime * prime : limit + 1 : prime] = b"\1" * (
                (limit - prime * prime) // prime + 1
            )
    return [prime for prime in range(2, limit + 1) if not composite[prime]]


def large_primes():
    composite = bytearray(LIMIT - SEGMENT_START + 1)
    for prime in small_primes(isqrt(LIMIT)):
        start = max(prime * prime, (SEGMENT_START + prime - 1) // prime * prime)
        composite[start - SEGMENT_START :: prime] = b"\1" * ((LIMIT - start) // prime + 1)
    return [
        value
        for value in range(LIMIT, SEGMENT_START - 1, -1)
        if not composite[value - SEGMENT_START]
    ][:SIZE]


def generate(seed, mode):
    if mode == "ones":
        return [1] * SIZE
    if mode == "distinct":
        values = large_primes()
        assert len(values) == SIZE
        return values
    if mode == "paired":
        return [p for p in large_primes()[: SIZE // 2] for _ in range(2)]
    if mode == "late":
        primes = large_primes()
        return primes[: SIZE - 2] + [primes[0], primes[0]]
    if mode == "squares":
        values = [p * p for p in small_primes(isqrt(LIMIT)) for _ in range(2)]
        return values + [1] * (SIZE - len(values))
    if mode == "powers":
        return [1] * (SIZE - 2) + [2**23, 2**22]
    if mode == "limit":
        return [LIMIT] * SIZE
    if mode == "random":
        rng = random.Random(seed)
        return [rng.randint(1, LIMIT) for _ in range(SIZE)]
    raise ValueError("unknown mode")


if __name__ == "__main__":
    values = generate(int(sys.argv[1]), sys.argv[2])
    print(len(values))
    print("\n".join(map(str, values)))
