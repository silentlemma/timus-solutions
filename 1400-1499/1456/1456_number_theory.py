import sys
from math import gcd


def primes_of(n):
    found, p = [], 2
    while p * p <= n:
        if n % p == 0:
            found.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        found.append(n)
    return found


def main():
    a, n = (int(x) for x in sys.stdin.read().split())
    if gcd(a, n) != 1:
        print(0)  # the remainders keep a common factor with N and never reach 1
        return
    # the order divides phi(N): strip prime factors while a power stays 1
    phi = n
    for p in primes_of(n):
        phi = phi // p * (p - 1)
    order = phi
    for p in primes_of(phi):
        while order % p == 0 and pow(a, order // p, n) == 1:
            order //= p
    print(order)


main()
