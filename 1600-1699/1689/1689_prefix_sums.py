import sys
from itertools import accumulate

HEADER = 5  # g, w, b, p, n


def main():
    data = [int(w) for w in sys.stdin.buffer.read().split()]
    g, w, b, p, n = data[:HEADER]
    last = g - b  # the barbell starts at s = 0 .. g - b
    diff = [0] * (last + 2)

    def add(lo, hi, value):
        lo, hi = max(lo, 0), min(hi, last)
        if lo <= hi:
            diff[lo] += value
            diff[hi + 1] -= value

    for x in data[HEADER:HEADER + n]:
        # a plate [a, a + p] hurts the worm [x, x + w] when they overlap by a
        # positive length, that is for whole a from x - p + 1 to x + w - 1.
        # The left plate starts at s, the right one at s + b - p
        lo1, hi1 = x - p + 1, x + w - 1
        lo2, hi2 = x - b + 1, x + w - 1 - b + p
        add(lo1, hi1, 1)
        add(lo2, hi2, 1)
        # a worm under both plates is hurt once
        add(max(lo1, lo2), min(hi1, hi2), -1)
    hurt = list(accumulate(diff[:last + 1]))
    print(hurt.index(min(hurt)))


main()
