"""Checker: the output is an order of all members 1..N in which every member
comes before each of its children (and so before all descendants)."""

import sys


def main():
    inp, _, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n, pos, children = data[0], 1, []
    for _ in range(n):
        end = data.index(0, pos)
        children.append(data[pos:end])
        pos = end + 1
    try:
        order = [int(x) for x in open(output).read().split()]
    except ValueError:
        print("non-integer token")
        sys.exit(1)
    if sorted(order) != list(range(1, n + 1)):
        print("not an order of all members 1..%d" % n)
        sys.exit(1)
    place = {v: i for i, v in enumerate(order)}
    for parent, kids in enumerate(children, 1):
        for child in kids:
            if place[parent] > place[child]:
                print("%d speaks after its child %d" % (parent, child))
                sys.exit(1)


main()
