"""Checker: 2n - 1 non-negative integers of at most 300 digits whose Hankel
matrix has every leading square of determinant 1. The determinants are
checked modulo three large primes by fraction-free elimination: its
pivots are exactly the leading minors."""

import sys

MOST_DIGITS = 300
PRIMES = [(1 << 61) - 1, 1000000007, 998244353]


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    n = int(open(source).read().split()[0])
    words = open(output).read().split()
    if len(words) != 2 * n - 1:
        fail("expected %d numbers, got %d" % (2 * n - 1, len(words)))
    if not all(w.isdigit() and len(w) <= MOST_DIGITS for w in words):
        fail("every number must be a non-negative integer of at most 300 digits")
    alpha = [int(w) for w in words]
    for p in PRIMES:
        a = [[alpha[i + j] % p for j in range(n)] for i in range(n)]
        # Gaussian elimination mod p: the k-th leading minor is the product
        # of the first k pivots, which must all be 1
        for k in range(n):
            if a[k][k] != 1:
                fail("the leading square of size %d does not have determinant 1" % (k + 1))
            for i in range(k + 1, n):
                f = a[i][k]
                if f:
                    a[i] = [(x - f * y) % p for x, y in zip(a[i], a[k])]


main()
