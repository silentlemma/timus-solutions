import sys
from math import hypot, pi

SHORTEST = 1.0  # the allowed rope lengths
LONGEST = 50.0
EPS = 1e-9


def best_pair(top_a, top_b, d):
    """The largest a^2 + b^2 with 1 <= a <= top_a, 1 <= b <= top_b, a + b <= d."""
    if top_a < SHORTEST - EPS or top_b < SHORTEST - EPS or d < 2 * SHORTEST - EPS:
        return -1.0
    # the square of a convex function is largest at a corner of the region
    corners = [
        (top_a, top_b),
        (top_a, SHORTEST),
        (SHORTEST, top_b),
        (top_a, d - top_a),
        (d - top_b, top_b),
        (d - SHORTEST, SHORTEST),
        (SHORTEST, d - SHORTEST),
    ]
    best = -1.0
    for a, b in corners:
        if (
            SHORTEST - EPS <= a <= top_a + EPS
            and SHORTEST - EPS <= b <= top_b + EPS
            and a + b <= d + EPS
        ):
            best = max(best, a * a + b * b)
    return best


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    xs = [float(v) for v in data[1 : 1 + 2 * n : 2]]
    ys = [float(v) for v in data[2 : 2 + 2 * n : 2]]
    # the longest rope at each tree: up to the nearest other tree and 50 meters
    top = []
    for i in range(n):
        x, y = xs[i], ys[i]
        near = min(hypot(x - u, y - v) for k, (u, v) in enumerate(zip(xs, ys)) if k != i)
        top.append(min(LONGEST, near))
    # trees by their longest rope: a pair cannot beat the best once even both
    # longest ropes together cannot
    order = sorted(range(n), key=lambda i: -top[i])
    best = 0.0
    for a, i in enumerate(order):
        for j in order[a + 1 :]:
            if top[i] ** 2 + top[j] ** 2 <= best:
                break
            d = hypot(xs[i] - xs[j], ys[i] - ys[j])
            best = max(best, best_pair(top[i], top[j], d))
    print("%.4f" % (pi * best))


main()
