"""Checker: a nonempty choice of the given numbers (each used at most as
often as it is given) whose sum is a multiple of N; such a choice always
exists, so 0 is never accepted."""

import sys
from collections import Counter


def main():
    inp, _, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n, given = data[0], Counter(data[1 : 1 + data[0]])
    try:
        out = [int(x) for x in open(output).read().split()]
    except ValueError:
        print("non-integer token")
        sys.exit(1)
    if not out or out[0] < 1 or len(out) != 1 + out[0]:
        print("expected a positive count and that many numbers")
        sys.exit(1)
    chosen = out[1:]
    if Counter(chosen) - given:
        print("a number is used more often than it is given")
        sys.exit(1)
    if sum(chosen) % n:
        print("the sum %d is not a multiple of %d" % (sum(chosen), n))
        sys.exit(1)


main()
