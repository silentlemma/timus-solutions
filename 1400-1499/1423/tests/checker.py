"""Checker: -1 exactly when the reference prints -1; otherwise any X with
0 <= X < N such that X shifts of the last character to the front turn S
into T."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    n, s, t = open(inp, "rb").read().split()[:3]
    n = int(n)
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != 1:
        fail("expected one number")
    x = int(got[0])
    if want == -1:
        if x != -1:
            fail("T is not a rotation of S")
        return
    if not 0 <= x < n:
        fail("X out of range")
    if s[n - x :] + s[: n - x] != t:
        fail("%d shifts do not give T" % x)


main()
