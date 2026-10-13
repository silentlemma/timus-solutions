"""Checker: two numbers x and y from 0 to p - 1 with x^2 + y^2 = k (mod p).
For a prime p such a pair always exists, so NO SOLUTION is wrong."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    k, p = map(int, open(inp).read().split())
    got = open(output).read().split()
    if len(got) != 2 or not all(w.isdigit() for w in got):
        fail("expected two numbers")
    x, y = map(int, got)
    if not (x < p and y < p):
        fail("a number is out of range")
    if (x * x + y * y) % p != k:
        fail("%d^2 + %d^2 is not %d modulo %d" % (x, y, k, p))


if __name__ == "__main__":
    main()
