"""Checker: a tour of all towns that starts at town 1 and costs no more
than the expected tour."""

import sys

TOLL = 1000


def cost(people, tour):
    n = len(tour)
    return sum(people[tour[(i + 1) % n]] * (TOLL // people[tour[i]]) for i in range(n))


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    people = [int(w) for w in data[1:1 + n]]
    want = [int(w) - 1 for w in open(expected).read().split()]
    try:
        got = [int(w) - 1 for w in open(output).read().split()]
    except ValueError:
        print("not an integer")
        sys.exit(1)
    if sorted(got) != list(range(n)):
        print("not a tour of all towns")
        sys.exit(1)
    if got[0] != 0:
        print("the tour must start at town 1")
        sys.exit(1)
    if cost(people, got) != cost(people, want):
        print("cost %d, expected %d" % (cost(people, got), cost(people, want)))
        sys.exit(1)


main()
