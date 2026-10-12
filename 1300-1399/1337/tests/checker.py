"""Checker: No Solution exactly when the expected answer says so;
otherwise the least number of days and an order of documents that, each
fetched on its official's first day it can be, ends on that day with all
wanted documents in hand. Any such order is accepted."""

import sys

NO = ["No", "Solution"]


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    words = iter(int(x) for x in open(source).read().split())
    n, week = next(words), next(words)
    day_of = [0] + [next(words) for _ in range(n)]

    def listed():
        items = []
        for value in words:
            if value == 0:
                return items
            items.append(value)
        return items

    needs = [[]] + [listed() for _ in range(n)]
    today = next(words)
    held = set(listed())
    wanted = listed()
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == NO or got == NO:
        if got != want:
            fail("expected %s" % " ".join(want[:1]))
        return
    if not all(w.isdigit() for w in got) or not got:
        fail("expected numbers")
    days, order = int(got[0]), [int(w) for w in got[1:]]
    if days != int(want[0]):
        fail("%d days instead of %s" % (days, want[0]))
    t, last = 0, 0  # day 0 is today
    for doc in order:
        if not 1 <= doc <= n or doc in held:
            fail("document %d cannot be fetched" % doc)
        if not all(p in held for p in needs[doc]):
            fail("document %d is fetched before its papers" % doc)
        t += (day_of[doc] - today - t) % week
        held.add(doc)
        last, t = t, t + 1
    if not all(d in held for d in wanted):
        fail("not every wanted document is in hand")
    if last != days:
        fail("the order takes %d days, not %d" % (last, days))


main()
