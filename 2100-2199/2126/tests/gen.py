"""Generate one input with ``python gen.py MODE SEED``.

Modes: 1 small random, 2 unrestricted random, 3 prime-power boundaries,
4 dense digits, 5 alternating digits, 6 maximum n, 7 largest-prime middle
digits, and 8 a digit with a zero central trinomial coefficient.
"""

import random
import sys

MAX_N = 10**18
MIN_PRIME = 5
PRIME_LIMIT = 10**6
MAX_PRIME = 999983
MAX_SMALL_N = 40
FIRST_ODD_DIVISOR = 3
ARGUMENT_COUNT = 3
SMALL_MODE = 1
RANDOM_MODE = 2
BOUNDARY_MODE = 3
DENSE_MODE = 4
ALTERNATING_MODE = 5
MAXIMUM_MODE = 6
MIDDLE_MODE = 7
ZERO_MODE = 8
SMALL_PRIMES = (5, 7, 11, 13, 17, 19, 31, 97)
BOUNDARY_PRIMES = (5, 7, 17, 97, 997, 65521, 131071, 524287, 999983)
OFFSETS = (-2, -1, 0, 1, 2)
ZERO_DIGITS = ((7, (3,)), (17, (5, 11)), (19, (4, 14)))


def is_prime(value):
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = FIRST_ODD_DIVISOR
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def random_prime(rng):
    while True:
        candidate = rng.randrange(MIN_PRIME, PRIME_LIMIT) | 1
        if is_prime(candidate):
            return candidate


def powers(prime):
    result = [prime]
    while result[-1] <= MAX_N // prime:
        result.append(result[-1] * prime)
    return result


def repeating_digits(prime, pattern, offset):
    value = 0
    power = 1
    position = offset
    while power <= MAX_N:
        digit = pattern[position % len(pattern)]
        candidate = value + digit * power
        if candidate > MAX_N:
            break
        value = candidate
        power *= prime
        position += 1
    return value


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == SMALL_MODE:
        return rng.randint(1, MAX_SMALL_N), rng.choice(SMALL_PRIMES)
    if mode == RANDOM_MODE:
        prime = random_prime(rng)
        return rng.randint(1, MAX_N), prime
    if mode == BOUNDARY_MODE:
        prime = rng.choice(BOUNDARY_PRIMES)
        power = rng.choice(powers(prime))
        candidates = [power + delta for delta in OFFSETS if 1 <= power + delta <= MAX_N]
        return rng.choice(candidates), prime
    if mode == DENSE_MODE:
        prime = rng.choice(BOUNDARY_PRIMES)
        return powers(prime)[-1] - 1, prime
    if mode == ALTERNATING_MODE:
        prime = rng.choice(BOUNDARY_PRIMES)
        pattern = (0, 1, prime // 2, prime - 1)
        return repeating_digits(prime, pattern, rng.randrange(len(pattern))), prime
    if mode == MAXIMUM_MODE:
        return MAX_N, rng.choice(BOUNDARY_PRIMES)
    if mode == MIDDLE_MODE:
        pattern = tuple(MAX_PRIME // 2 + rng.choice(OFFSETS) for _ in OFFSETS)
        return repeating_digits(MAX_PRIME, pattern, 0), MAX_PRIME
    if mode == ZERO_MODE:
        prime, digits = rng.choice(ZERO_DIGITS)
        digit = rng.choice(digits)
        quotient = rng.randrange((MAX_N - digit) // prime + 1)
        return quotient * prime + digit, prime
    raise ValueError("mode must be between 1 and 8")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    n, prime = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(n, prime)


if __name__ == "__main__":
    main()
