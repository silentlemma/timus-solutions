"""Checker: the restored strings must keep every known character and put
0 or 1 in place of every "?", their distance must be the printed number,
and that number must be the least possible, as in the expected output."""

import sys


class Bad(Exception):
    pass


def distance(s, p):
    n, m = len(s), len(p)
    return sum(p[i] != s[j] for i in range(m) for j in range(i, i + n - m + 1))


def restored(original, got, name):
    if len(got) != len(original):
        raise Bad("%s has the wrong length" % name)
    for a, b in zip(original, got):
        if b not in "01" or (a != "?" and a != b):
            raise Bad("%s does not restore the input" % name)


def check(source, expected, output):
    s, p = open(source).read().split()[:2]
    best = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != 3 or not got[0].isdigit():
        raise Bad("expected a number and two strings")
    restored(s, got[1], "the string")
    restored(p, got[2], "the pattern")
    if distance(got[1], got[2]) != int(got[0]):
        raise Bad("the printed distance does not match the strings")
    if int(got[0]) != best:
        raise Bad("distance %s, but %d is possible" % (got[0], best))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
