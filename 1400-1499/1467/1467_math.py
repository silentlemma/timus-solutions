import sys
from fractions import Fraction
from math import comb


def main():
    k = int(sys.stdin.read())
    # Bernoulli numbers with B1 = +1/2: the sum of C(m + 1, j) B_j over
    # j <= m equals m + 1, which gives B_m from the earlier ones
    bern = []
    for m in range(k + 1):
        rest = sum(comb(m + 1, j) * bern[j] for j in range(m))
        bern.append((m + 1 - rest) / Fraction(m + 1))
    # Faulhaber: the coefficient of N^(k + 1 - j) is C(k + 1, j) B_j / (k + 1)
    coef = [comb(k + 1, j) * bern[j] / (k + 1) for j in range(k + 1)] + [Fraction(0)]
    print(" ".join("%d/%d" % (c.numerator, c.denominator) for c in coef))


main()
