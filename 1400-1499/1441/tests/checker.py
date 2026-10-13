"""Checker: the same number of trails as the reference, and the listed
trails walk along tunnels only, using every tunnel exactly once."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    ends = [int(x) for x in data[2:]]
    left = {}
    for a, b in zip(ends[::2], ends[1::2]):
        key = (min(a, b), max(a, b))
        left[key] = left.get(key, 0) + 1
    want = int(open(expected).read().split()[0])
    lines = open(output).read().strip().split("\n")
    if not lines or not lines[0].strip():
        fail("empty output")
    if int(lines[0]) != want:
        fail("%s trails, expected %d" % (lines[0].strip(), want))
    if len(lines) != want + 1:
        fail("expected %d trail lines" % want)
    for line in lines[1:]:
        path = [int(x) for x in line.split()]
        if len(path) < 2:
            fail("a trail needs at least one tunnel")
        for a, b in zip(path, path[1:]):
            key = (min(a, b), max(a, b))
            if not left.get(key):
                fail("tunnel %d-%d is missing or used twice" % (a, b))
            left[key] -= 1
    if any(left.values()):
        fail("some tunnels are not dug")


main()
