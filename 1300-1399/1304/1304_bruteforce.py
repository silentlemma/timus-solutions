import sys

SCALE = 100  # coordinates have at most two decimals
DIGITS = 2
DIMS = 3
VOLUME_CENT = SCALE**2  # a hundredth of a volume unit, counted in 1 / SCALE^3


def scaled(token):
    whole, _, frac = token.partition(".")
    return int(whole or "0") * SCALE + int((frac + "0" * DIGITS)[:DIGITS])


def main():
    words = iter(sys.stdin.read().split())
    u, v, w = (scaled(next(words)) for _ in range(DIMS))
    n = int(next(words))
    points = [tuple(scaled(next(words)) for _ in range(DIMS)) for _ in range(n)]
    # a point outside A can never be inside G
    points = [p for p in points if p[0] <= u and p[1] <= v and p[2] <= w]
    best = 0
    xs = sorted({0, u} | {p[0] for p in points})
    for i, x1 in enumerate(xs):
        for x2 in reversed(xs[i + 1 :]):
            width = x2 - x1
            if width * v * w <= best:
                break  # the remaining x2 are closer still
            inside = sorted((p[1], p[2]) for p in points if x1 < p[0] < x2)
            # the lower y face lies on the floor or on a point; the upper
            # face sweeps down from the top, and every point it passes
            # leaves the slab, so neighbouring z gaps merge into one
            for k in range(-1, len(inside)):
                y1 = 0 if k < 0 else inside[k][0]
                if width * (v - y1) * w <= best:
                    break
                above = inside[k + 1 :]
                # a point on the floor or the ceiling never splits a gap
                zs = sorted([0, w] + [z for _, z in above if 0 < z < w])
                prev = {zs[j]: zs[j - 1] for j in range(1, len(zs))}
                nxt = {zs[j]: zs[j + 1] for j in range(len(zs) - 1)}
                gap = max(b - a for a, b in zip(zs, zs[1:]))
                y2 = v
                for y, z in reversed(above):
                    best = max(best, width * (y2 - y1) * gap)
                    if 0 < z < w:
                        lo, hi = prev[z], nxt[z]
                        nxt[lo], prev[hi] = hi, lo
                        gap = max(gap, hi - lo)
                    y2 = y
                best = max(best, width * (y2 - y1) * gap)
    cents = (best + VOLUME_CENT // 2) // VOLUME_CENT
    print("%d.%02d" % (cents // SCALE, cents % SCALE))


main()
