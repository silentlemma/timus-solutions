import sys
from math import gcd, isqrt


def main():
    r1, r2, n, i = map(int, sys.stdin.read().split())
    pos = i - 1
    if pos == 0:
        print("%d/1" % r1)
        return
    if pos == 1 << n:
        print("%d/1" % r2)
        return
    # between touching neighbours 1/sqrt(r) adds up, so circle pos has
    # 1/sqrt(r) = a/sqrt(r1) + b/sqrt(r2), with a and b from Stern's sequence
    # found as alpha f(x) + beta f(x + 1) while x is halved level by level
    alpha, beta, x = 1, 0, pos
    for _ in range(n):
        if x % 2 == 0:
            alpha, beta = alpha + beta, beta
        else:
            alpha, beta = alpha, alpha + beta
        x //= 2
    a, b = alpha, beta
    # with both a and b positive the radius is rational exactly when
    # r1 = g p^2 and r2 = g q^2 for g = gcd(r1, r2)
    g = gcd(r1, r2)
    p, q = isqrt(r1 // g), isqrt(r2 // g)
    if p * p * g != r1 or q * q * g != r2:
        print("Irrational")
        return
    # r = 1 / ((a q + b p) / (p q sqrt(g)))^2
    num, den = g * p * p * q * q, (a * q + b * p) ** 2
    common = gcd(num, den)
    print("%d/%d" % (num // common, den // common))


main()
