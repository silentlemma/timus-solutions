"""Checker: the order is free, so the output must hold exactly the
expected names, each once."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    _, expected, output = sys.argv[1:4]
    want = open(expected).read().split()
    got = open(output).read().split()
    if len(set(got)) != len(got):
        fail("a name is printed twice")
    if set(got) != set(want):
        fail("expected %d names, got a different set" % len(want))


main()
