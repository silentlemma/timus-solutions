import sys
from collections import Counter
from math import gcd


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pts = list(zip(data[1 : 2 * n + 1 : 2], data[2 : 2 * n + 1 : 2]))
    best = min(n, 2)
    for i, (xi, yi) in enumerate(pts):
        # the points on one line through point i have the same reduced direction
        count = Counter()
        for xj, yj in pts[i + 1 :]:
            dx, dy = xj - xi, yj - yi
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            # opposite directions are the same line
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            count[dx, dy] += 1
        if count:
            best = max(best, max(count.values()) + 1)
    print(best)


main()
