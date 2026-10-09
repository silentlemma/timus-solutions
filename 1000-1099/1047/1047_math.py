import sys
from fractions import Fraction

CENTS = 100


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    first, last, *rest = (Fraction(x) for x in data[1:])
    c = rest[:n]
    # with d[i] = a[i] - a[i-1] the relation reads d[i+1] = d[i] + 2 c[i], so
    # a[N+1] - a[0] = (N + 1) d[1] + 2 sum (N + 1 - i) c[i]
    weighted = sum((n - i) * ci for i, ci in enumerate(c))
    a1 = (n * first + last - 2 * weighted) / (n + 1)
    # the answer has two decimals; rounding only guards against bad input
    q = round(abs(a1) * CENTS)
    sign = "-" if a1 < 0 and q > 0 else ""
    print("%s%d.%02d" % (sign, q // CENTS, q % CENTS))


main()
