"""Checker: the expected least number of bottles, then that many
distinct city numbers whose drops destroy every city."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, r = data[0], data[1]
    cities = list(zip(data[2:2 + 2 * n:2], data[3:3 + 2 * n:2]))
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not all(w.isdigit() for w in got):
        raise Bad("expected whole numbers")
    if int(got[0]) != want:
        raise Bad("%s bottles, the least is %d" % (got[0], want))
    drops = [int(w) for w in got[1:]]
    if len(drops) != want or len(set(drops)) != want:
        raise Bad("expected %d distinct cities" % want)
    if not all(1 <= d <= n for d in drops):
        raise Bad("a city number is out of range")
    for x, y in cities:
        if not any((x - cities[d - 1][0]) ** 2 + (y - cities[d - 1][1]) ** 2 <= r * r for d in drops):
            raise Bad("the city at %d %d survives" % (x, y))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
