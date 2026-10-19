import sys
from math import asinh, hypot, sqrt


def stretch(ax, ay, bx, by, uax, uay, ubx, uby, span):
    # the length of the trace while the source a and the receiver b move
    # along the directions ua and ub for the time span
    dx, dy = bx - ax, by - ay
    vx, vy = ubx - uax, uby - uay
    a = vx * vx + vy * vy
    m = dx * vy - dy * vx  # constant cross product of d(t) = b - a and v
    if a == 0 or m <= 0:
        return 0.0
    # the trace point is a + lam(t) d(t), lam linear; its speed is
    # |r(t)| / sqrt(q(t)) for q(t) = |d(t)|^2 and a quadratic r(t)
    lam0 = (uax * dy - uay * dx) / m
    lam1 = (uax * vy - uay * vx) / m
    h = dx * vx + dy * vy
    c = dx * dx + dy * dy
    b = 2 * h
    r2 = 2 * lam1 * a
    r1 = uax * vx + uay * vy + lam1 * (b + h) + lam0 * a
    r0 = uax * dx + uay * dy + lam1 * c + lam0 * h
    # r = alpha q + beta q' + gamma, integrated term by term
    alpha = 2 * lam1
    beta = (r1 - alpha * b) / (2 * a)
    gamma = r0 - alpha * c - beta * b
    root_a = sqrt(a)
    tail = alpha * m * m / (2 * a) + gamma

    def primitive(t):
        q = max(a * t * t + b * t + c, 0.0)
        slope = 2 * a * t + b
        return ((lam1 * slope / (2 * a) + 2 * beta) * sqrt(q)
                + tail * asinh(slope / (2 * m)) / root_a)

    # the speed changes sign at the roots of r: the trace has a cusp there
    cuts = [0.0]
    if r2:
        half = r1 / 2
        disc = half * half - r2 * r0
        if disc > 0:
            s = sqrt(disc)
            cuts += sorted(((-half - s) / r2, (-half + s) / r2))
    elif r1:
        cuts.append(-r0 / r1)
    cuts = [0.0] + [t for t in cuts[1:] if 0 < t < span] + [span]
    total = 0.0
    for lo, hi in zip(cuts, cuts[1:]):
        mid = (lo + hi) / 2
        part = primitive(hi) - primitive(lo)
        total += part if r2 * mid * mid + r1 * mid + r0 >= 0 else -part
    return total


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    xs = [float(v) for v in data[1:2 * n + 1:2]]
    ys = [float(v) for v in data[2:2 * n + 2:2]]
    d = float(data[2 * n + 1])
    size = [hypot(xs[(i + 1) % n] - xs[i], ys[(i + 1) % n] - ys[i]) for i in range(n)]
    ux = [(xs[(i + 1) % n] - xs[i]) / size[i] for i in range(n)]
    uy = [(ys[(i + 1) % n] - ys[i]) / size[i] for i in range(n)]
    # the source starts at vertex 0; the receiver d further along the border
    j, left = 0, d
    while left >= size[j]:
        left -= size[j]
        j += 1
    bx, by = xs[j] + ux[j] * left, ys[j] + uy[j] * left
    ahead = size[j] - left  # what is left of the receiver's edge
    i, ax, ay, behind = 0, xs[0], ys[0], size[0]
    total = 0.0
    # walk from one corner event to the next, one of the two at a vertex
    while i < n:
        span = min(behind, ahead)
        total += stretch(ax, ay, bx, by, ux[i], uy[i], ux[j], uy[j], span)
        if behind <= ahead:
            ahead -= behind
            bx, by = bx + ux[j] * behind, by + uy[j] * behind
            i += 1
            if i < n:
                ax, ay, behind = xs[i], ys[i], size[i]
            if ahead <= 0:
                j = (j + 1) % n
                bx, by, ahead = xs[j], ys[j], size[j]
        else:
            behind -= ahead
            ax, ay = ax + ux[i] * ahead, ay + uy[i] * ahead
            j = (j + 1) % n
            bx, by, ahead = xs[j], ys[j], size[j]
    print("%.10f" % total)


main()
