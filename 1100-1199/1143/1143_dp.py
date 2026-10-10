import sys
from math import hypot


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pts = [(float(data[1 + 2 * k]), float(data[2 + 2 * k])) for k in range(n)]
    dist = [[hypot(px - qx, py - qy) for qx, qy in pts] for px, py in pts]
    # a shortest path never crosses itself, so on a convex polygon the visited
    # camps form an arc and the path ends at one of its ends; at[i] and
    # at_end[i] are the best paths over the arc from camp i, ending at either end
    at = [0.0] * n
    at_end = [0.0] * n
    for length in range(1, n):
        grow = [float("inf")] * n
        grow_end = [float("inf")] * n
        for i in range(n):
            j = (i + length - 1) % n
            before, after = (i - 1) % n, (i + length) % n
            for cost, here in ((at[i], i), (at_end[i], j)):
                grow[before] = min(grow[before], cost + dist[here][before])
                grow_end[i] = min(grow_end[i], cost + dist[here][after])
        at, at_end = grow, grow_end
    print("%.3f" % min(at + at_end))


main()
