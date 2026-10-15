"""Checker: for every command, a substring of it that is in no other
command and is as short as the expected one."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n = int(data[0])
    words = data[1:1 + n]
    want = open(expected).read().split()
    got = open(output).read().split()
    if len(got) != n:
        raise Bad("expected %d lines" % n)
    for i, key in enumerate(got):
        if len(key) != len(want[i]):
            raise Bad("command %d: length %d, the least is %d" % (i + 1, len(key), len(want[i])))
        if key not in words[i]:
            raise Bad("command %d: %s is not its substring" % (i + 1, key))
        for j, w in enumerate(words):
            if j != i and key in w:
                raise Bad("command %d: %s is also in command %d" % (i + 1, key, j + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
