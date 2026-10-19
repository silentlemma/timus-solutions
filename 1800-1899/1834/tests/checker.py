"""Checker: the least number k of passes from the expected answer, then
k orders, each obtained from the one before by one pass (some cars
kept in order, the rest appended reversed), the last one sorted."""

import sys


class Bad(Exception):
    pass


def one_pass(before, after):
    # after must be cars rising in their old positions, then cars falling
    where = {v: i for i, v in enumerate(before)}
    places = [where[v] for v in after]
    rise = 1
    while rise < len(places) and places[rise] > places[rise - 1]:
        rise += 1
    fall = len(places) - 1
    while fall > 0 and places[fall - 1] > places[fall]:
        fall -= 1
    return fall <= rise


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n, cars = data[0], data[1:1 + data[0]]
    want = int(open(expected).read().split()[0])
    try:
        got = list(map(int, open(output).read().split()))
    except ValueError:
        raise Bad("expected whole numbers")
    if not got or got[0] != want:
        raise Bad("expected %d passes" % want)
    if len(got) != 1 + want * n:
        raise Bad("expected %d orders of %d cars" % (want, n))
    for p in range(want):
        after = got[1 + p * n:1 + (p + 1) * n]
        if sorted(after) != list(range(1, n + 1)):
            raise Bad("order %d is not a permutation" % (p + 1))
        if not one_pass(cars, after):
            raise Bad("order %d does not follow by one pass" % (p + 1))
        cars = after
    if cars != list(range(1, n + 1)):
        raise Bad("the train ends unsorted")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
