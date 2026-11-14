from math import isqrt
import sys


FIRST_ODD_PRIME = 3


def odd_factors(limit):
    factors = bytearray((limit + 1) // 2)
    for prime in range(isqrt(limit - 1) | 1, 2, -2):
        if any(prime % divisor == 0 for divisor in range(FIRST_ODD_PRIME, isqrt(prime) + 1, 2)):
            continue
        start = prime * prime // 2
        size = (len(factors) - start + prime - 1) // prime
        if size > 0:
            factors[start::prime] = bytes((prime,)) * size
    return factors


def largest_root(prime, factors):
    order = prime - 1
    half = order >> 1
    remaining = order // (order & -order)
    powers = []
    while remaining > 1:
        factor = factors[remaining >> 1] or remaining
        powers.append(order // factor)
        while remaining % factor == 0:
            remaining //= factor

    for candidate in range(order, 1, -1):
        # The quadratic-residue test rejects non-generators first.
        if pow(candidate, half, prime) != 1:
            for exponent in powers:
                if pow(candidate, exponent, prime) == 1:
                    break
            else:
                return candidate
    raise ValueError("expected a prime modulus")


def main():
    _, *primes = map(int, sys.stdin.buffer.read().split())
    if primes:
        factors = odd_factors(max(primes))
        answers = {prime: str(largest_root(prime, factors)) for prime in set(primes)}
        sys.stdout.write("\n".join(map(answers.__getitem__, primes)) + "\n")


if __name__ == "__main__":
    main()
