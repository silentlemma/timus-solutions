from math import gcd


def main():
    n = int(input())
    # the chance that the row ends with two cards: (n^2 + 3n - 2) / (2n (2n - 1))
    num = n * (n + 2) + n - 2
    den = 2 * n * (2 * n - 1)
    g = gcd(num, den)
    print("%d/%d" % (num // g, den // g))


main()
