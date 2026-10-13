import sys
from bisect import bisect_right


def main():
    data = [int(v) for v in sys.stdin.read().split()]
    n = data[0]
    xs, ys = data[1 : 2 * n + 1 : 2], data[2 : 2 * n + 2 : 2]

    def segment(x):
        """The segment of f that holds x, or the one to its right."""
        return min(bisect_right(xs, x) - 1, n - 2)

    def value(x):
        j = segment(x)
        return ys[j] + (ys[j + 1] - ys[j]) * (x - xs[j]) / (xs[j + 1] - xs[j])

    def slope(left):
        """The slope of f to the right of x = left, as (rise, run)."""
        j = segment(left)
        return ys[j + 1] - ys[j], xs[j + 1] - xs[j]

    # f(x) = E(x) + O(x) with E(x) = (f(x) + f(-x)) / 2 and
    # O(x) = (f(x) - f(-x)) / 2; both are linear between the points of f
    # and their mirror images
    points = sorted(set(xs) | {-x for x in xs})
    parts = []
    for sign in (1, -1):  # the even part, then the odd one
        # the slope of a part between two neighbouring points, as a fraction:
        # (a/b -+ c/d) / 2 with the slope a/b of f at x and c/d of f at -x
        slopes = []
        for left, right in zip(points, points[1:]):
            a, b = slope(left)
            c, d = slope(-right)
            slopes.append((a * d - sign * c * b, 2 * b * d))
        keep = [points[0]]
        for k in range(1, len(points) - 1):
            (p, q), (r, s) = slopes[k - 1], slopes[k]
            if p * s != r * q:  # only real bends stay
                keep.append(points[k])
        keep.append(points[-1])
        parts.append([(x, (value(x) + sign * value(-x)) / 2) for x in keep])
    out = ["Yes"]
    for part in parts:
        out += ["%.6f %.6f" % p for p in part]
    print("\n".join(out))


main()
