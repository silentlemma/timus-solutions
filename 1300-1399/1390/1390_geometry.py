import sys
from bisect import bisect_left, bisect_right
from math import atan2, gcd

DIGITS = 10**9  # the time is printed with nine digits after the point
SHOT = 2
WALL = 4  # numbers that describe a shot and a wall
TREE = 4  # a segment tree over n leaves has under 4 n nodes


def reduced(x, y):
    g = gcd(x, y)
    return x // g, y // g


def main():
    tokens = sys.stdin.buffer.read().split()
    events = []
    pos = 0
    while pos < len(tokens) and tokens[pos] != b"end":
        if tokens[pos] == b"shot":
            count = SHOT
        else:
            count = WALL
        events.append(tuple(int(t) for t in tokens[pos + 1 : pos + 1 + count]))
        pos += 1 + count
    # the leaves: distinct shot directions by angle
    leaves = sorted({reduced(*e) for e in events if len(e) == 2}, key=lambda d: atan2(d[1], d[0]))
    angles = [atan2(y, x) for x, y in leaves]
    lx = [x for x, _ in leaves]
    ly = [y for _, y in leaves]
    size = max(1, len(leaves))
    tree = [-1] * (TREE * size)
    # a wall is the line nx x + ny y = c with c > 0: a shot v hits it at time c / (n . v)
    nx, ny, cs = [], [], []

    def better(w, u, leaf):
        vx, vy = lx[leaf], ly[leaf]
        return (nx[w] * vx + ny[w] * vy) * cs[u] > (nx[u] * vx + ny[u] * vy) * cs[w]

    def push(node, lo, hi, w):
        """Li Chao insertion: two walls swap places at most once on an arc below pi."""
        while True:
            cur = tree[node]
            if cur < 0:
                tree[node] = w
                return
            mid = (lo + hi) // 2
            if better(w, cur, mid):
                tree[node], w = w, cur
                cur = tree[node]
            if lo == hi:
                return
            if better(w, cur, lo):
                node, hi = 2 * node, mid
            elif better(w, cur, hi):
                node, lo = 2 * node + 1, mid + 1
            else:
                return

    def insert(node, lo, hi, left, right, w):
        if right < lo or hi < left:
            return
        if left <= lo and hi <= right:
            push(node, lo, hi, w)
            return
        mid = (lo + hi) // 2
        insert(2 * node, lo, mid, left, right, w)
        insert(2 * node + 1, mid + 1, hi, left, right, w)

    out = []
    for e in events:
        if len(e) == WALL:
            if not leaves:
                continue  # no shots at all
            x1, y1, x2, y2 = e
            if x1 * y2 - y1 * x2 < 0:
                x1, y1, x2, y2 = x2, y2, x1, y1
            a, b = y2 - y1, x1 - x2
            c = a * x1 + b * y1
            nx.append(a)
            ny.append(b)
            cs.append(c)
            w = len(cs) - 1
            # the wall covers the directions from its first end counterclockwise to the second
            first = atan2(*reversed(reduced(x1, y1)))
            last = atan2(*reversed(reduced(x2, y2)))
            lo, hi = bisect_left(angles, first), bisect_right(angles, last) - 1
            if first <= last:
                insert(1, 0, size - 1, lo, hi, w)
            else:
                insert(1, 0, size - 1, lo, size - 1, w)
                insert(1, 0, size - 1, 0, hi, w)
            continue
        vx, vy = e
        leaf = bisect_left(angles, atan2(*reversed(reduced(vx, vy))))
        node, lo, hi, best = 1, 0, size - 1, -1
        while True:
            cur = tree[node]
            if cur >= 0 and (best < 0 or better(cur, best, leaf)):
                best = cur
            if lo == hi:
                break
            mid = (lo + hi) // 2
            if leaf <= mid:
                node, hi = 2 * node, mid
            else:
                node, lo = 2 * node + 1, mid + 1
        if best < 0:
            out.append("Infinite")
        else:
            den = nx[best] * vx + ny[best] * vy
            q = (2 * cs[best] * DIGITS + den) // (2 * den)
            out.append("%d.%09d" % divmod(q, DIGITS))
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
