"""Checker: the number of pairs as in the expected output, and the same
pairs, each written in any order."""

import sys


class Bad(Exception):
    pass


def pairs(path):
    words = open(path).read().split()
    if not words or not all(w.isdigit() for w in words):
        raise Bad("not a list of numbers")
    count = int(words[0])
    if len(words) != 1 + 2 * count:
        raise Bad("expected %d pairs" % count)
    return {frozenset(map(int, words[1 + 2 * i:3 + 2 * i])) for i in range(count)}, count


def check(source, expected, output):
    want, k = pairs(expected)
    got, m = pairs(output)
    if m != k:
        raise Bad("expected %d pairs, got %d" % (k, m))
    if got != want:
        raise Bad("wrong pairs")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
