import math
import random

# bases that make Miller-Rabin exact far beyond 10^15
BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
FOUR = 4
SEVEN = 7
EIGHT = 8
SMALL = 1000  # trial division below this before Pollard's rho
RESIDUE = 3  # the primes 4k + 3
THREE_SQUARES = 3
FOUR_SQUARES = 4


def is_prime(n):
    if n < 2:
        return False
    for p in BASES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def rho(n):
    """A nontrivial factor of the composite odd n."""
    while True:
        c = random.randrange(1, n)
        x = y = random.randrange(n)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d


def primes_of(n, out):
    """Adds the prime factors of n > 1 to out, with repeats."""
    if is_prime(n):
        out.append(n)
        return
    d = rho(n)
    primes_of(d, out)
    primes_of(n // d, out)


def two_squares(n):
    """Fermat: every prime 4k + 3 must appear an even number of times."""
    factors = []
    for p in range(2, SMALL):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        primes_of(n, factors)
    return all(factors.count(p) % 2 == 0 for p in set(factors) if p % FOUR == RESIDUE)


def main():
    n = int(input())
    root = math.isqrt(n)
    m = n
    while m % FOUR == 0:
        m //= FOUR
    if root * root == n:
        print(1)
    elif two_squares(n):
        print(2)
    elif m % EIGHT == SEVEN:
        # Legendre: exactly the numbers 4^a (8b + 7) need four squares
        print(FOUR_SQUARES)
    else:
        print(THREE_SQUARES)


main()
