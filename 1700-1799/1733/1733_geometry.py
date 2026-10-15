import heapq
import math
import sys

EPS = 1e-9
SIDES = 4


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


class Book:
    def __init__(self, corners):
        self.corners = corners

    def edge(self, i):
        (ax, ay), (bx, by) = self.corners[i], self.corners[(i + 1) % SIDES]
        return ax, ay, bx - ax, by - ay

    def side(self, i, x, y):
        # positive inside the book (the corners go counterclockwise)
        ax, ay, ex, ey = self.edge(i)
        return cross(ex, ey, x - ax, y - ay)

    def outside(self, x, y):
        return any(self.side(i, x, y) < -EPS for i in range(SIDES))

    def blocks(self, ax, ay, bx, by):
        # whether the segment passes through the inside of the book
        lo, hi = 0.0, 1.0
        for i in range(SIDES):
            f0, f1 = self.side(i, ax, ay), self.side(i, bx, by)
            if f0 <= EPS and f1 <= EPS:
                return False
            if f0 < f1:
                lo = max(lo, (EPS - f0) / (f1 - f0)) if f0 <= EPS else lo
            elif f1 < f0:
                hi = min(hi, (f0 - EPS) / (f0 - f1)) if f1 <= EPS else hi
        return hi - lo > EPS


def chord(book, i, cx, cy, r):
    # the part of side i inside the disk, as a parameter range on the side
    ax, ay, ex, ey = book.edge(i)
    a = ex * ex + ey * ey
    b = (ax - cx) * ex + (ay - cy) * ey
    c = (ax - cx) ** 2 + (ay - cy) ** 2 - r * r
    disc = b * b - a * c
    if disc <= 0:
        return None
    root = math.sqrt(disc)
    lo, hi = max(0.0, (-b - root) / a), min(1.0, (-b + root) / a)
    if (hi - lo) * math.sqrt(a) <= EPS:
        return None
    return lo, hi


def nearest(book, sx, sy, cx, cy, r):
    # the closest point of the disk outside the book that sx, sy sees
    best = math.inf
    d = math.hypot(sx - cx, sy - cy)
    if d > EPS:
        qx, qy = cx + (sx - cx) * r / d, cy + (sy - cy) * r / d
        if book.outside(qx, qy) and not book.blocks(sx, sy, qx, qy):
            best = max(0.0, d - r)
    for i in range(SIDES):
        part = chord(book, i, cx, cy, r)
        if part is None or book.side(i, sx, sy) > EPS:
            continue
        ax, ay, ex, ey = book.edge(i)
        t = ((sx - ax) * ex + (sy - ay) * ey) / (ex * ex + ey * ey)
        t = min(max(t, part[0]), part[1])
        best = min(best, math.hypot(ax + t * ex - sx, ay + t * ey - sy))
    return best


def main():
    v = [int(w) for w in sys.stdin.read().split()]
    corners = [(v[2 * i], v[2 * i + 1]) for i in range(SIDES)]
    cx, cy, r, mx, my = v[2 * SIDES:]
    book = Book(corners)
    # the mouse goes straight or around corners of the book; Dijkstra over
    # the mouse and the corners gives each its shortest way from the start
    points = [(mx, my)] + corners
    dist = [math.inf] * len(points)
    dist[0] = 0.0
    heap = [(0.0, 0)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for w in range(1, len(points)):
            if w == u:
                continue
            (ux, uy), (wx, wy) = points[u], points[w]
            if u > 0 and (u - w) % SIDES not in (1, SIDES - 1):
                continue
            if u == 0 and book.blocks(ux, uy, wx, wy):
                continue
            nd = d + math.hypot(wx - ux, wy - uy)
            if nd < dist[w]:
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    answer = min(dist[k] + nearest(book, x, y, cx, cy, r) for k, (x, y) in enumerate(points))
    print("%.5f" % answer)


main()
