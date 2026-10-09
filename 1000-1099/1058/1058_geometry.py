import math
import sys

# samples per smooth piece and golden-section steps around the best samples
SAMPLES = 64
STEPS = 60
GOLDEN = (math.sqrt(5) - 1) / 2
EPS = 1e-12


def main():
    tok = sys.stdin.read().split()
    n = int(tok[0])
    xs = [float(tok[1 + 2 * i]) for i in range(n)]
    ys = [float(tok[2 + 2 * i]) for i in range(n)]
    # the walk below needs counterclockwise order, whatever order is given
    if sum(xs[i - 1] * ys[i] - xs[i] * ys[i - 1] for i in range(n)) < 0:
        xs.reverse()
        ys.reverse()
    # vertices repeated twice so that a boundary walk never wraps around
    vx, vy = xs * 2 + xs[:1], ys * 2 + ys[:1]
    # pre[k]: twice the signed area swept by the edges 0 .. k-1 from the origin
    pre = [0.0]
    for k in range(2 * n):
        pre.append(pre[-1] + vx[k] * vy[k + 1] - vx[k + 1] * vy[k])
    half = pre[n] / 2

    def point(u):
        i = int(u)
        t = u - i
        return vx[i] + t * (vx[i + 1] - vx[i]), vy[i] + t * (vy[i + 1] - vy[i]), i

    def partner(u):
        """The position w in (u, u + n) of the other end of the halving cut."""
        px, py, i = point(u)

        # twice the area of P, V[i+1], ..., V[j]
        def fan(j):
            return px * vy[i + 1] - vx[i + 1] * py + pre[j] - pre[i + 1] + vx[j] * py - px * vy[j]

        lo, hi = i + 1, i + n
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if fan(mid) <= half:
                lo = mid
            else:
                hi = mid
        j = lo
        # on the edge V[j] -> V[j+1] the area grows linearly with the position
        ex, ey = vx[j + 1] - vx[j], vy[j + 1] - vy[j]
        slope = vx[j] * ey - ex * vy[j] + ex * py - px * ey
        s = (half - fan(j)) / slope if slope > 0 else 0.0
        return j + min(max(s, 0.0), 1.0)

    def length(u):
        px, py, _ = point(u)
        qx, qy, _ = point(partner(u))
        return math.hypot(qx - px, qy - py)

    # the cut length is smooth between the vertices and the partners of the
    # vertices; sample every piece and refine its best samples
    breaks = sorted({float(k) for k in range(n + 1)} | {partner(k) % n for k in range(n)})
    best = min(length(b % n) for b in breaks)
    for a, b in zip(breaks, breaks[1:]):
        if b - a < EPS:
            continue
        us = [a + (b - a) * k / SAMPLES for k in range(SAMPLES + 1)]
        vals = [length(u) for u in us]
        for k in range(SAMPLES + 1):
            # a local minimum among the samples, the piece ends included
            left, right = max(k - 1, 0), min(k + 1, SAMPLES)
            if vals[k] <= vals[left] and vals[k] <= vals[right]:
                lo, hi = us[left], us[right]
                for _ in range(STEPS):
                    m1, m2 = hi - GOLDEN * (hi - lo), lo + GOLDEN * (hi - lo)
                    if length(m1) < length(m2):
                        hi = m2
                    else:
                        lo = m1
                best = min(best, length((lo + hi) / 2))
        best = min(best, min(vals))
    print("%.6f" % best)


main()
