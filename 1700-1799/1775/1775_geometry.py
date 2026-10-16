import math
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    pins = [int(v) for v in data[2:2 + 2 * n]]
    xs, ys = pins[0::2], pins[1::2]
    # a ball of diameter D hits the pins whose centres lie in a strip of width
    # D + 1 along its path, so the narrowest strip holding k centres decides, and
    # one side of that strip runs along two centres, so only those directions
    best = math.inf if k > 1 else 0.0
    for i in range(n):
        for j in range(i + 1, n):
            dx, dy = xs[j] - xs[i], ys[j] - ys[i]
            across = sorted(dx * y - dy * x for x, y in zip(xs, ys))
            gap = min(across[t + k - 1] - across[t] for t in range(n - k + 1))
            best = min(best, gap / math.hypot(dx, dy))
    # a ball of any size will do when the strip is no wider than a pin
    print("%.10f" % (best - 1) if best > 1 else "0.000000")


main()
