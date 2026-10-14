"""Checker: the same hieroglyphs as expected, in any order."""

import sys


def main():
    _, expected, output = sys.argv[1:4]
    want = sorted(open(expected).read().split())
    got = sorted(open(output).read().split())
    if want != got:
        print("expected %s, got %s" % (want[:10], got[:10]))
        sys.exit(1)


main()
