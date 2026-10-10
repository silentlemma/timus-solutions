import math
import sys
from math import gcd


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data)
    rects = [[next(data) for _ in "xyxyc"] for _ in range(n)]
    c0, length = next(data), next(data)
    # walking at angle t, a vertical line x = a is crossed after a/cos t and a
    # horizontal one y = b after b/sin t; a rectangle adds (c - c0) times
    # (exit - entry), a sum of such terms, each valid between two corners
    events = {}

    def term(start, end, dp, dq):
        for (y, x), sign in ((start, 1), (end, -1)):
            g = gcd(y, x)
            key = (y // g, x // g)
            p, q = events.get(key, (0, 0))
            events[key] = (p + sign * dp, q + sign * dq)

    for x1, y1, x2, y2, c in rects:
        w = c - c0
        # out through the right side or the top, in through the left or the bottom
        term((y1, x2), (y2, x2), w * x2, 0)
        term((y2, x2), (y2, x1), 0, w * y2)
        term((y1, x1), (y2, x1), -w * x1, 0)
        term((y1, x2), (y1, x1), 0, -w * y1)
    order = sorted(events, key=lambda k: math.atan2(k[0], k[1]))
    # below the lowest corner no rectangle is met at all
    low = math.atan2(order[0][0], order[0][1])
    best = (c0 * length, low / 2)
    # between corners the time is c0*L + p/cos t + q/sin t: with p, q > 0 it
    # is above c0*L, otherwise monotone or concave, so corners are enough
    p = q = 0
    for y, x in order:
        t = math.atan2(y, x)
        cost = c0 * length + p / math.cos(t) + q / math.sin(t)
        if cost < best[0]:
            best = (cost, t)
        dp, dq = events[(y, x)]
        p, q = p + dp, q + dq
    cost, t = best
    print("%.6f\n%.6f %.6f" % (cost, length * math.cos(t), length * math.sin(t)))


main()
