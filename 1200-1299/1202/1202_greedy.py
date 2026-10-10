import sys

FIELDS = 4


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    rects = [data[1 + FIELDS * i : 1 + FIELDS * (i + 1)] for i in range(n)]
    # the rectangles form a chain from left to right, so the horizontal
    # part of the path is fixed; only the height at each border varies
    y, vertical = 1, 0
    for (_, low1, _, high1), (_, low2, _, high2) in zip(rects, rects[1:]):
        lo, hi = max(low1, low2) + 1, min(high1, high2) - 1
        if lo > hi:
            print(-1)
            return
        # moving only when forced is optimal: clamp into the crossing
        target = min(max(y, lo), hi)
        vertical += abs(target - y)
        y = target
    _, _, right, top = rects[-1]
    print(right - 2 + vertical + abs(top - 1 - y))


main()
