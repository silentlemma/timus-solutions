"""Checker: the speech must be as long as the expected one and occur in
both given speeches; when nothing is common the speech is empty."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    _, a, b = open(source).read().split()
    want = open(expected).read().strip()
    got = open(output).read().strip()
    if len(got) != len(want):
        fail("length %d, expected %d" % (len(got), len(want)))
    if got not in a or got not in b:
        fail("the speech is not part of both speeches")


main()
