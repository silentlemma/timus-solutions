"""Checker: "Impossible" exactly when the reference says so; otherwise a
count k and k different weekdays whose training days between September 2
and the eve of the match number from A to B."""

import sys

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = {"September": 0, "October": 30, "November": 61, "December": 91}


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    first, month, day, a, b = open(inp).read().split()
    a, b = int(a), int(b)
    start = DAYS.index(first)
    match = MONTHS[month] + int(day) - 1
    count = [0] * len(DAYS)
    for i in range(1, match):
        count[(start + i) % len(DAYS)] += 1
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got:
        fail("empty output")
    if want == ["Impossible"]:
        if got != ["Impossible"]:
            fail("expected Impossible")
        return
    if got == ["Impossible"]:
        fail("a schedule exists")
    k = int(got[0])
    chosen = got[1:]
    if len(chosen) != k:
        fail("expected %d days" % k)
    if len(set(chosen)) != k or any(d not in DAYS for d in chosen):
        fail("days must be different weekday names")
    total = sum(count[DAYS.index(d)] for d in chosen)
    if not a <= total <= b:
        fail("%d trainings, expected from %d to %d" % (total, a, b))


main()
