import math
import sys

SIEVE_LIMIT = 10000
LOWER_MODULUS = 5000
MODULUS_COUNT = 510


def prime_moduli():
    prime = [True] * (SIEVE_LIMIT + 1)
    prime[0] = prime[1] = False
    for value in range(2, math.isqrt(SIEVE_LIMIT) + 1):
        if prime[value]:
            for multiple in range(value * value, SIEVE_LIMIT + 1, value):
                prime[multiple] = False
    return tuple(
        value for value in range(LOWER_MODULUS, SIEVE_LIMIT + 1) if prime[value]
    )[:MODULUS_COUNT]


MODULI = prime_moduli()


def multiply(first, second, modulus):
    a, b = first
    c, d = second
    return (a * c - b * d) % modulus, (a * d + b * c) % modulus


def power(real, imaginary, exponent, modulus):
    base = real % modulus, imaginary % modulus
    result = 1, 0
    while exponent:
        if exponent & 1:
            result = multiply(result, base, modulus)
        base = multiply(base, base, modulus)
        exponent >>= 1
    return result


def count_roots(a, b, n, c, d, m):
    common = math.gcd(n, m)
    first_exponent, second_exponent = m // common, n // common
    for modulus in MODULI:
        if power(a, b, first_exponent, modulus) != power(
            c, d, second_exponent, modulus
        ):
            return 0
    return common


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    print(count_roots(*data))


if __name__ == "__main__":
    main()
