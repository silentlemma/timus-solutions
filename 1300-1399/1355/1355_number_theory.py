import sys

FIRST_ODD = 3  # the smallest odd prime


def prime_factors(n):
    """How many primes multiply to n, counted with repetition."""
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    d = FIRST_ODD
    while d * d <= n:  # odd divisors only, which halves the loop
        while n % d == 0:
            n //= d
            count += 1
        d += 2
    return count + (n > 1)


def main():
    data = list(map(int, sys.stdin.read().split()))
    out = []
    for i in range(data[0] if data else 0):
        a, b = data[1 + 2 * i], data[2 + 2 * i]
        # every step multiplies the number by at least one prime
        out.append(str(1 + prime_factors(b // a) if b % a == 0 else 0))
    print("\n".join(out))


main()
