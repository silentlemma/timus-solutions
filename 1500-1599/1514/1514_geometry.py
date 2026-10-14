import math
import sys

SMALL = 8  # pieces up to this size are checked triple by triple
HALF = 0.5  # a better triangle has every side shorter than half its perimeter


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = [int(v) for v in data[1 : 2 * n + 1 : 2]]
    ys = [int(v) for v in data[2 : 2 * n + 2 : 2]]
    order = sorted(range(n), key=lambda i: (xs[i], ys[i]))
    best = [math.inf, (0, 1, 2)]

    def perimeter(a, b, c):
        return (
            math.hypot(xs[a] - xs[b], ys[a] - ys[b])
            + math.hypot(xs[b] - xs[c], ys[b] - ys[c])
            + math.hypot(xs[c] - xs[a], ys[c] - ys[a])
        )

    def triples(pts, reach):
        """Tries every triple of pts, sorted by y, that fits within reach
        vertically."""
        size = len(pts)
        for i in range(size):
            a = pts[i]
            top = ys[a] + reach
            for j in range(i + 1, size):
                b = pts[j]
                if ys[b] >= top:
                    break
                for k in range(j + 1, size):
                    c = pts[k]
                    if ys[c] >= top:
                        break
                    p = perimeter(a, b, c)
                    if p < best[0]:
                        best[0], best[1] = p, (a, b, c)
                        top = ys[a] + best[0] * HALF

    def solve(lo, hi):
        """Solves the points order[lo:hi]."""
        if hi - lo <= SMALL:
            triples(sorted(order[lo:hi], key=ys.__getitem__), math.inf)
            return
        mid = (lo + hi) // 2
        split = xs[order[mid]]
        solve(lo, mid)
        solve(mid, hi)
        # a better triangle across the split lies in a strip around it
        reach = best[0] * HALF
        strip = [p for p in order[lo:hi] if abs(xs[p] - split) < reach]
        strip.sort(key=ys.__getitem__)
        triples(strip, reach)

    solve(0, n)
    print("%.6f" % best[0])
    print(" ".join(str(i + 1) for i in best[1]))


main()
