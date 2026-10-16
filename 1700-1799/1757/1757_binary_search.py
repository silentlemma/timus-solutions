import sys
from bisect import bisect_right

STEPS = 100
HEADER = 3


def main():
    v = [int(w) for w in sys.stdin.read().split()]
    n, need, fineness = v[0], v[1], v[2]
    mass, purity = v[HEADER::2], v[HEADER + 1::2]
    order = sorted(range(n), key=lambda i: purity[i])
    # the bars laid out from the poorest to the richest: where each starts,
    # and the gold, in grams times a thousand, before it
    starts, golds = [0], [0]
    for i in order:
        starts.append(starts[-1] + mass[i])
        golds.append(golds[-1] + mass[i] * purity[i])
    total = starts[-1]
    target = need * fineness

    def gold_before(t):
        k = min(bisect_right(starts, t), n) - 1
        return golds[k] + (t - starts[k]) * purity[order[k]]

    def window(s):
        return gold_before(s + need) - gold_before(s)

    # a window of the needed weight sliding from the poorest end to the
    # richest gains gold steadily, so it hits the target if anything does
    if total < need or not window(0) <= target <= window(total - need):
        print("NO")
        return
    low, high = 0.0, float(total - need)
    for _ in range(STEPS):
        mid = (low + high) / 2
        if window(mid) < target:
            low = mid
        else:
            high = mid
    start = (low + high) / 2
    take = [0.0] * n
    for k, i in enumerate(order):
        take[i] = max(0.0, min(starts[k + 1], start + need) - max(starts[k], start))
    print("YES")
    print("\n".join("%.10f" % x for x in take))


main()
