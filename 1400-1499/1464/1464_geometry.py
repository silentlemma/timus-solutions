import math
import sys

DIGITS = 4  # coordinates are given to four decimals
SCALE = 10**DIGITS


def exact(text):
    # a coordinate times 10^4, read exactly
    sign = -1 if text.startswith("-") else 1
    whole, _, frac = text.lstrip("+-").partition(".")
    return sign * (int(whole or "0") * SCALE + int((frac + "0" * DIGITS)[:DIGITS]))


def main():
    words = iter(sys.stdin.read().split())
    px, py = exact(next(words)), exact(next(words))
    n = int(next(words))
    xs, ys = [0] * n, [0] * n
    for i in range(n):
        xs[i], ys[i] = exact(next(words)) - px, exact(next(words)) - py
    # the directions of the corners seen from the lamp, equal ones merged
    order = sorted(range(n), key=lambda i: math.atan2(ys[i], xs[i]))
    group = [0] * n
    dirs = []
    for i in order:
        if (
            dirs
            and xs[i] * dirs[-1][1] == ys[i] * dirs[-1][0]
            and xs[i] * dirs[-1][0] + ys[i] * dirs[-1][1] > 0
        ):
            group[i] = len(dirs) - 1
        else:
            dirs.append((xs[i], ys[i]))
            group[i] = len(dirs) - 1
    m = len(dirs)
    # every gap between neighbouring directions is below half a turn; its middle
    middle = []
    for k in range(m):
        (ax, ay), (bx, by) = dirs[k], dirs[(k + 1) % m]
        la, lb = math.hypot(ax, ay), math.hypot(bx, by)
        middle.append((ax / la + bx / lb, ay / la + by / lb))
    size = 1
    while size < m:
        size *= 2
    first = list(range(2 * size))  # the leftmost gap under each tree node
    for x in range(2 * size - 1, 0, -1):
        first[x] = x - size if x >= size else first[2 * x]
    num, ex, ey = [], [], []  # an edge AB: cross(A, B - A) and B - A

    def distance(e, k):
        # how far along the middle ray of gap k the line of edge e lies
        u, v = middle[k]
        return num[e] / (u * ey[e] - v * ex[e])

    best = [-1] * (2 * size)

    def offer(x, e):
        # each node keeps the nearest edge among those covering all its gaps,
        # and edges never cross, so one gap decides for the whole node
        if best[x] < 0 or distance(e, first[x]) < distance(best[x], first[x]):
            best[x] = e

    def cover(lo, hi, e):
        lo += size
        hi += size
        while lo < hi:
            if lo & 1:
                offer(lo, e)
                lo += 1
            if hi & 1:
                hi -= 1
                offer(hi, e)
            lo //= 2
            hi //= 2

    for i in range(n):
        j = (i + 1) % n
        c = xs[i] * ys[j] - ys[i] * xs[j]
        if c == 0:
            continue  # seen edge-on, it hides nothing
        a, b = (i, j) if c > 0 else (j, i)
        e = len(num)
        num.append(float(xs[a] * (ys[b] - ys[a]) - ys[a] * (xs[b] - xs[a])))
        ex.append(float(xs[b] - xs[a]))
        ey.append(float(ys[b] - ys[a]))
        ga, gb = group[a], group[b]
        if ga < gb:
            cover(ga, gb, e)
        else:
            cover(ga, m, e)
            cover(0, gb, e)
    area = 0.0
    for k in range(m):
        x, near = k + size, -1
        while x:
            if best[x] >= 0 and (near < 0 or distance(best[x], k) < distance(near, k)):
                near = best[x]
            x //= 2
        (ax, ay), (bx, by) = dirs[k], dirs[(k + 1) % m]
        ta = num[near] / (ax * ey[near] - ay * ex[near])
        tb = num[near] / (bx * ey[near] - by * ex[near])
        area += ta * tb * (ax * by - ay * bx) / 2
    print("%.4f" % (area / SCALE / SCALE))


main()
