"""Checker: n lowercase letters such that every two artists d apart
around the circle, for every proper divisor d of n, differ. Such a
colouring always exists, so "Impossible" is wrong."""

import sys
from operator import eq


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read())
    got = open(output).read().split()
    if len(got) != 1 or len(got[0]) != n:
        raise Bad("expected one word of %d letters" % n)
    word = got[0]
    if not all("a" <= c <= "z" for c in word):
        raise Bad("only lowercase letters are allowed")
    for d in range(1, n):
        if n % d == 0 and any(map(eq, word, word[d:] + word[:d])):
            raise Bad("two artists %d apart share a colour" % d)


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
