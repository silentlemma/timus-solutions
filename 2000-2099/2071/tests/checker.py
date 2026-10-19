"""Checker: the minimal number of pourings as in the expected output, and an
arrangement of all glasses that needs exactly that many pourings."""

import sys


class Bad(Exception):
    pass


def pourings(cocktails):
    # a juice needs a new pouring where it starts a run of glasses
    count, previous = 0, ""
    for c in cocktails:
        count += sum(1 for j in c if j not in previous)
        previous = c
    return count


def check(source, expected, output):
    words = open(source).read().split()
    n, orders = int(words[0]), words[1:]
    best = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != n + 1 or not all(w.isdigit() for w in got):
        raise Bad("expected a number and %d indices" % n)
    if int(got[0]) != best:
        raise Bad("expected %d pourings, got %s" % (best, got[0]))
    arrangement = [int(w) for w in got[1:]]
    if sorted(arrangement) != list(range(1, n + 1)):
        raise Bad("not a permutation of the glasses")
    real = pourings(orders[i - 1] for i in arrangement)
    if real != best:
        raise Bad("the arrangement needs %d pourings" % real)


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
