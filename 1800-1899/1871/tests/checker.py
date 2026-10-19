"""Checker: the number of users who learn about the earthquake and their
names in any order, each once."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or not got[0].isdigit() or int(got[0]) != len(got) - 1:
        raise Bad("the count does not match the names")
    if got[0] != want[0]:
        raise Bad("expected %s users, got %s" % (want[0], got[0]))
    if len(set(got[1:])) != len(got) - 1:
        raise Bad("a name is repeated")
    if set(got[1:]) != set(want[1:]):
        raise Bad("wrong users")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
