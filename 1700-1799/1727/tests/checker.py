"""Checker: distinct positive numbers below 10^5 whose digits add up to
n; a set always exists, so -1 is never right."""

import sys

LIMIT = 10 ** 5


class Bad(Exception):
    pass


def check(source, output):
    n = int(open(source).read().split()[0])
    try:
        got = [int(w) for w in open(output).read().split()]
    except ValueError:
        raise Bad("expected integers")
    if not got or got[0] < 1:
        raise Bad("a set exists, but none was printed")
    count, numbers = got[0], got[1:]
    if len(numbers) != count:
        raise Bad("expected %d numbers, found %d" % (count, len(numbers)))
    if any(not 0 < x < LIMIT for x in numbers):
        raise Bad("a number is not between 1 and 99999")
    if len(set(numbers)) != count:
        raise Bad("the numbers are not distinct")
    total = sum(sum(map(int, str(x))) for x in numbers)
    if total != n:
        raise Bad("the digits add up to %d, not %d" % (total, n))


def main():
    try:
        check(sys.argv[1], sys.argv[3])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
