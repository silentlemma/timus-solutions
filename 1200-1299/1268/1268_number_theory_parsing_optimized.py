import os
from array import array
from math import isqrt
import sys

INPUT_BUFFER_BYTES = 4096


FIRST_ODD_PRIME = 3


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > 32 else b""
        yield from parts
    if pending:
        yield pending


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
    values = map(int, words())
    count = next(values)
    primes = array("H", (next(values) for _ in range(count)))
    if primes:
        factors = odd_factors(max(primes))
        answers = {}
        out = []
        for prime in primes:
            answer = answers.get(prime)
            if answer is None:
                answer = str(largest_root(prime, factors))
                answers[prime] = answer
            out.append(answer)
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
