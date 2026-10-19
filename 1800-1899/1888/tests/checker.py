"""Checker: the largest possible spread as in the expected output, and
experiences from 1 to 50 with the two pilots of every flight exactly one
year apart and with that spread; or -1 when the expected output says
so."""

import sys

LOW, HIGH = 1, 50


class Bad(Exception):
    pass


def check(source, expected, output):
    v = list(map(int, open(source).read().split()))
    n, p = v[0], v[1]
    flights = [(v[2 + 2 * k], v[3 + 2 * k]) for k in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or not all(t.lstrip("-").isdigit() for t in got):
        raise Bad("not a list of integers")
    if got[0] != want[0]:
        raise Bad("expected %s, got %s" % (want[0], got[0]))
    if want[0] == "-1":
        if len(got) != 1:
            raise Bad("extra output after -1")
        return
    if len(got) != p + 1:
        raise Bad("expected %d experiences" % p)
    years = [0] + [int(t) for t in got[1:]]
    if any(not LOW <= y <= HIGH for y in years[1:]):
        raise Bad("an experience is out of range")
    for a, b in flights:
        if abs(years[a] - years[b]) != 1:
            raise Bad("pilots %d and %d are not one year apart" % (a, b))
    if max(years[1:]) - min(years[1:]) != int(got[0]):
        raise Bad("the experiences do not have the stated spread")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
