"""Checker: the order costs the printed sum, feeds everyone, names each
dish of the menu at most once with a positive count, and matches the
expected order in cost and in the number of different dishes."""

import sys

SCALE = 1000


def thousandths(text):
    whole, _, part = text.partition(".")
    return int(whole) * SCALE + int((part + "000")[:3])


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    words = open(source).read().split()
    n, m = int(words[0]), int(words[1])
    menu = {}
    for i in range(n):
        name, price, fill = words[2 + 3 * i : 5 + 3 * i]
        menu[name] = (int(price), thousandths(fill))
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or not got[0].isdigit() or len(got) % 2 == 0:
        fail("expected a sum and pairs of a dish and a count")
    pairs = [(got[i], got[i + 1]) for i in range(1, len(got), 2)]
    names = [name for name, _ in pairs]
    if len(set(names)) != len(names):
        fail("a dish is listed twice")
    cost = fill = 0
    for name, count in pairs:
        if name not in menu:
            fail("%s is not on the menu" % name)
        if not count.isdigit() or int(count) < 1:
            fail("the count of %s is not positive" % name)
        cost += menu[name][0] * int(count)
        fill += menu[name][1] * int(count)
    if cost != int(got[0]):
        fail("the order costs %d, not %s" % (cost, got[0]))
    if fill < m * SCALE:
        fail("the order does not feed everyone")
    if cost != int(want[0]):
        fail("the order costs %d, the best costs %s" % (cost, want[0]))
    if len(pairs) != (len(want) - 1) // 2:
        fail("%d different dishes, the best has %d" % (len(pairs), (len(want) - 1) // 2))


main()
