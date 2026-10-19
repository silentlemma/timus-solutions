import sys

FAR = 2  # eyes lie closer to PR than twice its length
ARC = 6  # numbers describing an arc


def exact_sort(order, num, den, tie):
    # sort by num/den, ties by tie: stable float sorts put it almost in
    # order, then insertion with exact cross products fixes the neighbours
    # that floats cannot tell apart
    order.sort(key=tie.__getitem__)
    approx = [a / b for a, b in zip(num, den)]
    order.sort(key=approx.__getitem__)
    for j in range(1, len(order)):
        cur = order[j]
        k = j
        while k:
            prev = order[k - 1]
            lhs, rhs = num[cur] * den[prev], num[prev] * den[cur]
            if lhs > rhs or (lhs == rhs and tie[cur] >= tie[prev]):
                break
            order[k] = prev
            k -= 1
        order[k] = cur


def faces(arc, points):
    px, py, qx, qy, rx, ry = arc
    ux, uy = rx - px, ry - py
    side = ux * (qy - py) - uy * (qx - px)
    span = ux * ux + uy * uy
    height, near, far = [], [], []
    for x, y in points:
        cross = ux * (y - py) - uy * (x - px)
        n = ux * (x - px) + uy * (y - py)
        f = -ux * (x - rx) - uy * (y - ry)
        # across PR from Q, both base angles acute, close enough to PR
        if cross * side >= 0 or n <= 0 or f <= 0 or abs(cross) >= FAR * span:
            continue
        height.append(abs(cross))
        near.append(n)
        far.append(f)
    k = len(height)
    # tangents of the angles at P and at R are height/near and height/far,
    # and the angles at R get ranks, equal angles sharing a rank
    zero = [0] * k
    by_r = list(range(k))
    exact_sort(by_r, height, far, zero)
    rank = [0] * k
    r = 0
    for j in range(k):
        cur = by_r[j]
        if j and height[cur] * far[by_r[j - 1]] != height[by_r[j - 1]] * far[cur]:
            r += 1
        rank[cur] = r + 1
    # the line through two eyes misses PR exactly when one eye is seen
    # higher from P and lower from R: count pairs in opposite orders
    by_p = list(range(k))
    exact_sort(by_p, height, near, rank)
    tree = [0] * (r + 2)
    size = r + 1
    pairs = 0
    for seen in range(k):
        rk = rank[by_p[seen]]
        below = 0
        i = rk
        while i:
            below += tree[i]
            i &= i - 1
        pairs += seen - below
        i = rk
        while i <= size:
            tree[i] += 1
            i += i & -i
    return pairs


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n, m = next(data), next(data)
    arcs = [tuple(next(data) for _ in range(ARC)) for _ in range(n)]
    points = [(next(data), next(data)) for _ in range(m)]
    print(sum(faces(arc, points) for arc in arcs))


main()
