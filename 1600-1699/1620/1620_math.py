import sys
from math import gcd


def main():
    sys.set_int_max_str_digits(0)  # the answer can have about 9000 digits
    n, m, k = map(int, input().split())
    # each flip moves the expectation to E (1 - 2/n) + 1, so after k flips
    # E = n/2 + (m - n/2) ((n - 2)/n)^k = (n^(k+1) + (2m - n)(n - 2)^k) / (2 n^k)
    num = n ** (k + 1) + (2 * m - n) * (n - 2) ** k
    den = 2 * n**k
    g = gcd(num, den)
    print("%d/%d" % (num // g, den // g))


main()
