"""Checker: every answer must use exactly the digits of its number, have
no leading zero and be divisible by 7. Such a rearrangement always exists,
so 0 is never accepted."""

import sys

DIVISOR = 7


def main():
    inp, _, output = sys.argv[1:4]
    tok = open(inp).read().split()
    numbers = tok[1 : 1 + int(tok[0])]
    got = open(output).read().split()
    if len(got) != len(numbers):
        print("expected %d answers, got %d" % (len(numbers), len(got)))
        sys.exit(1)
    for i, (x, y) in enumerate(zip(numbers, got), 1):
        if sorted(x) != sorted(y) or y[0] == "0" or int(y) % DIVISOR:
            print("answer %d: %s is not a rearrangement of %s divisible by 7" % (i, y, x))
            sys.exit(1)


main()
