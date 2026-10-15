"""Checker: as many problems as in the expected answer, each prepared by a
person who can write statements and a person who can prepare tests whose
ranks differ by exactly 2, with nobody taking part twice."""

import sys

GAP = 2
FIELDS = 3


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    people = {}
    for i in range(n):
        k = 1 + FIELDS * i
        name, kind, rank = words[k:k + FIELDS]
        people[name] = (kind, int(rank))
    best = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not got[0].isdigit():
        raise Bad("expected the number of problems first")
    count = int(got[0])
    if count != best:
        raise Bad("%d problems, the best is %d" % (count, best))
    if len(got) != 1 + 2 * count:
        raise Bad("expected two names for each of %d problems" % count)
    used = set()
    for i in range(count):
        writer, tester = got[1 + 2 * i], got[2 + 2 * i]
        for name in (writer, tester):
            if name not in people:
                raise Bad("unknown name %s" % name)
            if name in used:
                raise Bad("%s takes part twice" % name)
            used.add(name)
        if people[writer][0] == "testdata":
            raise Bad("%s cannot write statements" % writer)
        if people[tester][0] == "statements":
            raise Bad("%s cannot prepare tests" % tester)
        if abs(people[writer][1] - people[tester][1]) != GAP:
            raise Bad("the ranks of %s and %s do not differ by 2" % (writer, tester))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
