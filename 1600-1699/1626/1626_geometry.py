import gc
import math
import sys

# PyPy frees the short-lived bit masks only when it collects, and the rows
# here make a lot of them; collecting now and then keeps the peak low.
COLLECT_EVERY = 64


def cross(ox, oy, ax, ay, bx, by):
    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = [int(v) for v in data[1 : 2 * n + 1 : 2]]
    ys = [int(v) for v in data[2 : 2 * n + 2 : 2]]
    sx1, sy1, sx2, sy2 = (int(v) for v in data[2 * n + 1 :])
    orig = list(range(n))
    if sum(xs[i] * ys[i - n + 1] - xs[i - n + 1] * ys[i] for i in range(n)) < 0:
        xs.reverse()
        ys.reverse()
        orig.reverse()  # counterclockwise from now on
    edge_left = [0] * n  # bit k: the vertex is strictly left of edge k -> k + 1
    for v in range(n):
        if v % COLLECT_EVERY == 0:
            gc.collect()
        bits = 0
        for k in range(n):
            kn = (k + 1) % n
            if cross(xs[k], ys[k], xs[kn], ys[kn], xs[v], ys[v]) > 0:
                bits |= 1 << k
        edge_left[v] = bits

    def in_cone(i, j):
        """j lies strictly inside the interior angle of the polygon at i"""
        prv, nxt = (i - 1) % n, (i + 1) % n
        base = cross(xs[i], ys[i], xs[nxt], ys[nxt], xs[prv], ys[prv])
        to_next = cross(xs[i], ys[i], xs[nxt], ys[nxt], xs[j], ys[j])
        to_prev = cross(xs[i], ys[i], xs[prv], ys[prv], xs[j], ys[j])
        if base >= 0:
            return to_next > 0 and to_prev < 0
        return to_next > 0 or to_prev < 0

    # vis[a]: the vertices joined to a by an edge or a diagonal
    vis = [0] * n
    for i in range(n):
        vis[i] |= 1 << (i + 1) % n | 1 << (i - 1) % n
    for a in range(n):
        if a % COLLECT_EVERY == 0:
            gc.collect()
        # row[b]: the vertices strictly left of the line a -> b, and clear:
        # the b with no vertex on the open segment ab. Around a the others
        # sorted by angle make every left set a circular range.
        clear = 0
        ax, ay = xs[a], ys[a]
        others = (k for k in range(n) if k != a)
        order = sorted(others, key=lambda k: math.atan2(ys[k] - ay, xs[k] - ax))
        m = len(order)
        prefix = [0] * (m + 1)  # bits of the first t points of the order
        for t in range(m):
            prefix[t + 1] = prefix[t] | (1 << order[t])
        row = [0] * n
        end = 0
        t = 0
        while t < m:
            b = order[t]
            dx, dy = xs[b] - ax, ys[b] - ay
            # the points in exactly the direction of b, nearest first
            group = t + 1
            while group < m:
                q = order[group]
                along = (xs[q] - ax) * dx + (ys[q] - ay) * dy
                if cross(ax, ay, xs[b], ys[b], xs[q], ys[q]) or along < 0:
                    break
                group += 1
            same = sorted(order[t:group], key=lambda k: abs(xs[k] - ax) + abs(ys[k] - ay))
            clear |= 1 << same[0]
            end = max(end, group)
            while end < t + m:
                q = order[end % m]
                if cross(ax, ay, xs[b], ys[b], xs[q], ys[q]) <= 0:
                    break
                end += 1
            if end <= m:
                bits = prefix[end] ^ prefix[group]
            else:  # the range wraps past the end of the order
                bits = (prefix[m] ^ prefix[group]) | prefix[end - m]
            for k in same:
                row[k] = bits
            t = group
        i = a
        for j in range(i + 2, n):
            if (j + 1) % n == i or not clear >> j & 1:
                continue
            if not in_cone(i, j) or not in_cone(j, i):
                continue
            line = row[j]
            shifted = (line >> 1) | ((line & 1) << (n - 1))
            # edges whose ends lie on different sides of the line, and whose
            # line separates i from j; those touching i or j cannot cross
            hits = (line ^ shifted) & (edge_left[i] ^ edge_left[j])
            for k in ((i - 1) % n, i, (j - 1) % n, j):
                hits &= ~(1 << k)
            crossing = False
            while hits:
                k = (hits & -hits).bit_length() - 1
                hits &= hits - 1
                kn = (k + 1) % n
                d1 = cross(xs[i], ys[i], xs[j], ys[j], xs[k], ys[k])
                d2 = cross(xs[i], ys[i], xs[j], ys[j], xs[kn], ys[kn])
                if (d1 > 0 > d2) or (d1 < 0 < d2):
                    crossing = True
                    break
            if not crossing:
                vis[i] |= 1 << j
                vis[j] |= 1 << i

    def opens_inward(v, u, w):
        """no polygon edge at v points into the corner u, v, w (counterclockwise)"""
        for e in ((v - 1) % n, (v + 1) % n):
            if e != u and e != w and cross(xs[v], ys[v], xs[u], ys[u], xs[e], ys[e]) > 0:
                if cross(xs[v], ys[v], xs[w], ys[w], xs[e], ys[e]) < 0:
                    return False
        return True

    left1 = [0] * n  # bit k: k strictly left of the line a -> s1
    left2 = [0] * n
    for a in range(n):
        if a % COLLECT_EVERY == 0:
            gc.collect()
        for k in range(n):
            if cross(xs[a], ys[a], sx1, sy1, xs[k], ys[k]) > 0:
                left1[a] |= 1 << k
            if cross(xs[a], ys[a], sx2, sy2, xs[k], ys[k]) > 0:
                left2[a] |= 1 << k
    # a triangle a, b, k counterclockwise whose sides are edges or diagonals,
    # with both ends of S strictly inside; it holds no vertex when no polygon
    # edge enters it at a corner, as the boundary cannot cross its sides
    for b in range(n):
        if b % COLLECT_EVERY == 0:
            gc.collect()
        right1 = right2 = 0
        for k in range(n):
            if cross(xs[b], ys[b], sx1, sy1, xs[k], ys[k]) < 0:
                right1 |= 1 << k
            if cross(xs[b], ys[b], sx2, sy2, xs[k], ys[k]) < 0:
                right2 |= 1 << k
        for a in range(n):
            if a == b or not (vis[a] >> b & 1):
                continue
            if cross(xs[a], ys[a], xs[b], ys[b], sx1, sy1) <= 0:
                continue
            if cross(xs[a], ys[a], xs[b], ys[b], sx2, sy2) <= 0:
                continue
            cand = vis[a] & vis[b] & left1[a] & left2[a] & right1 & right2
            cand &= ~(1 << a | 1 << b)
            while cand:
                k = (cand & -cand).bit_length() - 1
                cand &= cand - 1
                if opens_inward(a, b, k) and opens_inward(b, k, a) and opens_inward(k, a, b):
                    print(orig[a] + 1, orig[b] + 1, orig[k] + 1)
                    return
    print("Impossible")


main()
