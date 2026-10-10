import sys
from math import isqrt

ROOT = 31623


def main():
    sieve = bytearray([1]) * (ROOT + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(ROOT) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    primes = [i for i in range(ROOT + 1) if sieve[i]]
    data = sys.stdin.read().split()
    out = []
    for n in map(int, data[1 : 1 + int(data[0])]):
        p = next(d for d in primes if n % d == 0)
        q = n // p
        # x = 1 (mod p) and x = 0 (mod q); the other root is n + 1 - x
        x = q * pow(q, -1, p) % n
        lo, hi = sorted((x, n + 1 - x))
        out.append("0 1 %d %d" % (lo, hi))
    print("\n".join(out))


main()
