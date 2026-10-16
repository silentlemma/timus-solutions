import sys


def main():
    a, b, d, r1, top1, r2, top2, h = map(int, sys.stdin.read().split())
    # the widest part of a plate inside the borders, at height min(d, h),
    # scaled by h to stay in integers
    low = min(d, h)
    w1 = r1 * h + (top1 - r1) * low
    w2 = r2 * h + (top2 - r2) * low
    fits = 2 * max(w1, w2) <= min(a, b) * h
    # the centres can be this far apart along each side, and the plates
    # must be at least top1 + top2 apart, where they are widest
    dx = a * h - w1 - w2
    dy = b * h - w1 - w2
    apart = dx * dx + dy * dy >= ((top1 + top2) * h) ** 2
    print("YES" if fits and apart else "NO")


main()
