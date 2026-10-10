"""Checker: N/2 roads that pair up all cities, no two of which cross; only
roads whose x-ranges overlap are compared, so ordinary plans check fast."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def turn(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (v > 0) - (v < 0)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    pts = [None] + [(int(data[2 * i - 1]), int(data[2 * i])) for i in range(1, n + 1)]
    try:
        nums = [int(t) for t in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(nums) != n or sorted(nums) != list(range(1, n + 1)):
        fail("the roads do not pair up every city once")
    roads = [(pts[nums[k]], pts[nums[k + 1]]) for k in range(0, n, 2)]
    roads.sort(key=lambda r: min(r[0][0], r[1][0]))
    for i, (a, b) in enumerate(roads):
        right = max(a[0], b[0])
        for c, d in roads[i + 1 :]:
            if min(c[0], d[0]) > right:
                break
            # no three cities are collinear, so the turns are never zero
            if turn(a, b, c) != turn(a, b, d) and turn(c, d, a) != turn(c, d, b):
                fail("two roads cross")


if __name__ == "__main__":
    main()
