from math import gcd, isqrt

ROOT = 31623
SMALL = 100
BLOCK = 64


def main():
    sieve = bytearray([1]) * (ROOT + 1)
    sieve[0] = sieve[1] = 0
    for value in range(2, isqrt(ROOT) + 1):
        if sieve[value]:
            sieve[value * value :: value] = bytes(len(sieve[value * value :: value]))
    primes = [value for value in range(2, ROOT + 1) if sieve[value]]
    small = [value for value in primes if value <= SMALL]
    blocks = [primes[first : first + BLOCK] for first in range(len(small), len(primes), BLOCK)]
    del primes, sieve
    leaves = 1
    while leaves < len(blocks):
        leaves *= 2
    products = [1] * (2 * leaves)
    for index, block in enumerate(blocks):
        product = 1
        for prime in block:
            product *= prime
        products[leaves + index] = product
    for index in range(leaves - 1, 0, -1):
        products[index] = products[2 * index] * products[2 * index + 1]

    def factor(n):
        for prime in small:
            if n % prime == 0:
                return prime
        divisor = gcd(n, products[1])
        if divisor < n:
            return divisor
        # Both factors divide this subtree product. Split until separated,
        # or finish by at most BLOCK individual divisions in their leaf.
        index = 1
        while index < leaves:
            index *= 2
            divisor = gcd(n, products[index])
            if divisor == 1:
                index += 1
            elif divisor < n:
                return divisor
        return next(prime for prime in blocks[index - leaves] if n % prime == 0)

    out = []
    for _ in range(int(input())):
        n = int(input())
        p = factor(n)
        q = n // p
        x = q * pow(q, -1, p)
        y = n + 1 - x
        if x > y:
            x, y = y, x
        out.append(f"0 1 {x} {y}")
    print("\n".join(out))


main()
