"""Checker: one whole number per day, none negative, adding up to the
work m * d1, with the busiest day using no more diggers than the
rounded-up average."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    m, d1, d2 = (int(w) for w in open(source).read().split())
    work = m * d1
    fewest = -(-work // d2)
    got = open(output).read().split()
    if len(got) != d2:
        raise Bad("expected %d numbers, got %d" % (d2, len(got)))
    if not all(w.isdigit() for w in got):
        raise Bad("every day needs a whole number of diggers")
    days = [int(w) for w in got]
    if sum(days) != work:
        raise Bad("the diggers do %d digger-days instead of %d" % (sum(days), work))
    if max(days) > fewest:
        raise Bad("%d diggers are hired, %d are enough" % (max(days), fewest))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
