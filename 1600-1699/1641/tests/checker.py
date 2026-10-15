"""Checker: n rooms from 1 to k with every room taken, then m distinct
pairs of students from different rooms that together include everyone."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    n, k, m = map(int, open(source).read().split())
    got = open(output).read().split()
    if len(got) != n + 2 * m or not all(w.isdigit() for w in got):
        fail("expected %d rooms and %d pairs" % (n, m))
    nums = [int(w) for w in got]
    room = nums[:n]
    if not all(1 <= r <= k for r in room):
        fail("a room number is out of range")
    if len(set(room)) != k:
        fail("some room has no student")
    seen = set()
    duty = [False] * n
    for d in range(m):
        a, b = nums[n + 2 * d], nums[n + 2 * d + 1]
        if not (1 <= a <= n and 1 <= b <= n) or a == b:
            fail("day %d: bad pair %d %d" % (d + 1, a, b))
        if room[a - 1] == room[b - 1]:
            fail("day %d: both students keep room %d" % (d + 1, room[a - 1]))
        key = (min(a, b), max(a, b))
        if key in seen:
            fail("the pair %d %d is on duty twice" % key)
        seen.add(key)
        duty[a - 1] = duty[b - 1] = True
    if not all(duty):
        fail("student %d is never on duty" % (duty.index(False) + 1))


main()
