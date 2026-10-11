import sys

SIDE = 100
SPOT = 3


def area(lo, hi, lo2, hi2):
    """The smallest picture holding the box, at least 100 by 100."""
    return max(hi - lo, SIDE) * max(hi2 - lo2, SIDE)


def best(spots):
    # sorted by their low edge on the first axis, a prefix and the rest can
    # hang apart exactly when the prefix ends no later than the rest begins
    spots.sort()
    n = len(spots)
    suffix = [None] * n
    lo, hi, lo2, hi2 = spots[-1]
    for i in range(n - 1, -1, -1):
        a, b, c, d = spots[i]
        lo, hi, lo2, hi2 = min(lo, a), max(hi, b), min(lo2, c), max(hi2, d)
        suffix[i] = area(lo, hi, lo2, hi2)
    result = suffix[0]
    lo, hi, lo2, hi2 = spots[0]
    for k in range(1, n):
        a, b, c, d = spots[k]
        if hi <= a:
            result = min(result, area(lo, hi, lo2, hi2) + suffix[k])
        lo, hi, lo2, hi2 = min(lo, a), max(hi, b), min(lo2, c), max(hi2, d)
    return result


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    # a picture must hold each spot whole, so it must hold its bounding square
    rs, xs, ys = (data[1 + t :: SPOT][:n] for t in range(SPOT))
    across = [(x - r, x + r, y - r, y + r) for r, x, y in zip(rs, xs, ys)]
    down = [(y - r, y + r, x - r, x + r) for r, x, y in zip(rs, xs, ys)]
    # two pictures that do not overlap are split by a vertical or a
    # horizontal line, and each can grow to 100 mm away from that line
    print(min(best(across), best(down)))


main()
