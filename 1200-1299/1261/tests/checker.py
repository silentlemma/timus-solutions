"""Checker: the payment minus the tip must be N, the tip positive, the
payment at most 4294967291, and both sums made of distinct powers of 3
(ternary digits 0 and 1 only). A solution always exists, so the answer
0 is wrong."""

import sys

LIMIT = 4294967291


def distinct_powers(v):
    while v:
        if v % 3 == 2:
            return False
        v //= 3
    return True


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    try:
        tokens = [int(t) for t in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if len(tokens) != 2:
        fail("expected the payment and the tip")
    pay, tip = tokens
    if pay - tip != n:
        fail("%d - %d is not %d" % (pay, tip, n))
    if tip < 1:
        fail("no tip")
    if pay > LIMIT:
        fail("payment %d is above the limit" % pay)
    if not distinct_powers(pay) or not distinct_powers(tip):
        fail("a sum repeats a bill")


if __name__ == "__main__":
    main()
