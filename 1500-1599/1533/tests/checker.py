"""Checker: the size must equal the expected one, and the listed hobbits
must be distinct and pairwise incomparable, also through chains of
weighings."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    heavier = [0] * n
    for i in range(n):
        for j in range(n):
            if data[1 + i * n + j] == "1":
                heavier[i] |= 1 << j
    for k in range(n):
        for i in range(n):
            if heavier[i] >> k & 1:
                heavier[i] |= heavier[k]
    want = int(open(expected).read().split()[0])
    try:
        values = [int(v) for v in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if not values or values[0] != want:
        fail("size %s, expected %d" % (values[:1], want))
    chosen = values[1:]
    if len(chosen) != want:
        fail("%d hobbits listed, expected %d" % (len(chosen), want))
    if len(set(chosen)) != want or not all(1 <= v <= n for v in chosen):
        fail("hobbits repeat or are out of range")
    for a in chosen:
        for b in chosen:
            if heavier[a - 1] >> (b - 1) & 1:
                fail("hobbit %d is heavier than hobbit %d" % (a, b))


main()
