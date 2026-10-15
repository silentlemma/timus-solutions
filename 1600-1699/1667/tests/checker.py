"""Checker: for each test an N x M table of distinct squares of positive
integers, at most 10^17, whose rows and columns all add up to squares."""

import math
import sys

TOP = 10 ** 17


def fail(reason):
    print(reason)
    sys.exit(1)


def square(v):
    return v >= 0 and math.isqrt(v) ** 2 == v


def main():
    source, _, output = sys.argv[1:4]
    data = open(source).read().split()
    t = int(data[0])
    words = open(output).read().split()
    pos = 0
    for k in range(t):
        n, m = int(data[1 + 2 * k]), int(data[2 + 2 * k])
        cells = words[pos:pos + n * m]
        pos += n * m
        if len(cells) < n * m:
            fail("test %d: the table is too short" % (k + 1))
        try:
            nums = [int(w) for w in cells]
        except ValueError:
            fail("test %d: not an integer" % (k + 1))
        if any(not 0 < v <= TOP or not square(v) for v in nums):
            fail("test %d: an entry is not a positive square up to 10^17" % (k + 1))
        if len(set(nums)) != n * m:
            fail("test %d: entries repeat" % (k + 1))
        grid = [nums[i * m:(i + 1) * m] for i in range(n)]
        if not all(square(sum(row)) for row in grid):
            fail("test %d: a row does not add up to a square" % (k + 1))
        if not all(square(sum(row[j] for row in grid)) for j in range(m)):
            fail("test %d: a column does not add up to a square" % (k + 1))
    if pos != len(words):
        fail("extra output")


main()
