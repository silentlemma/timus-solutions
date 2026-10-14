"""Checker: the expected number of trips, each trip listing its coats in
increasing order with each size more than R above the one before, and
every coat in exactly one trip."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n, r = int(data[0]), int(data[1])
    sizes = [int(v) for v in data[2 : 2 + n]]
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if not all(w.isdigit() for w in words) or not words:
        fail("expected numbers only")
    nums = [int(w) for w in words]
    if nums[0] != want:
        fail("%d trips, the least is %d" % (nums[0], want))
    pos, taken = 1, [False] * (n + 1)
    for trip in range(want):
        if pos >= len(nums):
            fail("trip %d is missing" % (trip + 1))
        count = nums[pos]
        coats = nums[pos + 1 : pos + 1 + count]
        pos += 1 + count
        if count < 1 or len(coats) != count:
            fail("trip %d is malformed" % (trip + 1))
        for i, c in enumerate(coats):
            if not 1 <= c <= n or taken[c]:
                fail("coat %d is out of range or taken twice" % c)
            taken[c] = True
            if i and (c <= coats[i - 1] or sizes[c - 1] - sizes[coats[i - 1] - 1] <= r):
                fail("trip %d cannot hold coats %d and %d" % (trip + 1, coats[i - 1], c))
    if pos != len(nums):
        fail("extra numbers after the trips")
    if not all(taken[1:]):
        fail("some coat stays in the shop")


main()
