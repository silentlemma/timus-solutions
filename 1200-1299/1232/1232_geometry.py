import math
import sys

EPS = 1e-9


def solve(h, d, alpha):
    tg, sn, cs = math.tan(alpha / 2), math.sin(alpha / 2), math.cos(alpha / 2)

    def min_drop(t):
        # the smallest drop of one move from a point on the cone wall at
        # depth t: across to the opposite wall, or almost level once the
        # cone there is at least d wide
        w = 2 * t * tg
        if w >= d:
            return 0.0
        return (math.sqrt(d * d * (1 + tg * tg) - w * w) - w * tg) / (1 + tg * tg)

    def path(n, slides):
        # first slides moves down the wall, then crossings at full tilt; as
        # soon as one move can drop exactly the extra height, that move and
        # then straight down
        pts = []
        t, x, side = 0.0, 0.0, 1.0
        for left in range(n, 0, -1):
            extra = h - t - (left - 1) * d
            drop = min_drop(t)
            if extra >= drop - EPS:
                x += side * math.sqrt(max(0.0, d * d - extra * extra))
                t += extra
                pts.append((x, h - t))
                pts.extend((x, (k - 1) * d) for k in range(left - 1, 0, -1))
                pts[-1] = (x, 0.0)
                return pts
            if left == 1:
                return None
            if n - left < slides:
                x -= side * d * sn
                t += d * cs
            else:
                t += drop
                x = side * t * tg
                side = -side
            pts.append((x, h - t))
        return None

    n = math.ceil(h / d - EPS)
    for slides in range(n + 1):
        pts = path(n, slides)
        if pts is not None:
            return [str(n)] + ["%.6f 0 %.6f" % p for p in pts]
    return ["-1"]


def main():
    h, d, alpha = map(float, sys.stdin.read().split())
    sys.stdout.write("\n".join(solve(h, d, alpha)) + "\n")


main()
