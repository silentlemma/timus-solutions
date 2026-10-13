"""Checker: two counts that cost at most N and spend as much as the best
choice does."""

import sys


def best(a, b, n):
    if a < b:
        a, b = b, a
    return max(x * a + (n - x * a) // b * b for x in range(min(n // a, b - 1) + 1))


def main():
    inp, _, output = sys.argv[1:4]
    a, b, n = map(int, open(inp).read().split())
    got = open(output).read().split()
    if len(got) != 2:
        print("expected two numbers")
        sys.exit(1)
    x, y = map(int, got)
    spent = x * a + y * b
    if x < 0 or y < 0 or spent > n:
        print("the purchase is impossible")
        sys.exit(1)
    if spent != best(a, b, n):
        print("spends %d, but %d is possible" % (spent, best(a, b, n)))
        sys.exit(1)


main()
