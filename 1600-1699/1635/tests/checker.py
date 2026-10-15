"""Checker: the count equals the expected minimum, and the listed pieces
are that many palindromes that spell the name in order."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    name = open(source).read().split()[0]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not got[0].isdigit():
        fail("expected the count first")
    if int(got[0]) != want:
        fail("count %s, expected %d" % (got[0], want))
    parts = got[1:]
    if len(parts) != want:
        fail("%d pieces listed, the count says %d" % (len(parts), want))
    for part in parts:
        if part != part[::-1]:
            fail("%s is not a palindrome" % part)
    if "".join(parts) != name:
        fail("the pieces do not spell the name")


main()
