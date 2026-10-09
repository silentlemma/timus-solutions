"""Checker: YES and a numbering of the flights by 1..M, each number used
once, such that the numbers of the flights at every airport with two or
more flights have greatest common divisor 1. A connected graph always has
such a numbering, so NO is never accepted."""

import sys
from math import gcd


def main():
    inp, _, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n, m = data[0], data[1]
    edges = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(m)]
    tokens = open(output).read().split()
    if not tokens or tokens[0] != "YES":
        print("expected YES")
        sys.exit(1)
    try:
        numbers = [int(x) for x in tokens[1:]]
    except ValueError:
        print("non-integer token")
        sys.exit(1)
    if sorted(numbers) != list(range(1, m + 1)):
        print("the numbers are not a permutation of 1..%d" % m)
        sys.exit(1)
    at = [0] * (n + 1)
    count = [0] * (n + 1)
    for (a, b), k in zip(edges, numbers):
        for v in (a, b):
            at[v] = gcd(at[v], k)
            count[v] += 1
    for v in range(1, n + 1):
        if count[v] >= 2 and at[v] != 1:
            print("airport %d: the greatest common divisor is %d" % (v, at[v]))
            sys.exit(1)


main()
