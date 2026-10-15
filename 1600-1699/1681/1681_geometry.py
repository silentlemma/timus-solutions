import sys


def clip(poly, ax, ay, bx, by, sign):
    """The part of a convex polygon on the given side (sign of the cross
    product) of the line through A and B."""
    out = []
    count = len(poly)
    for i in range(count):
        px, py = poly[i]
        qx, qy = poly[(i + 1) % count]
        sp = ((bx - ax) * (py - ay) - (by - ay) * (px - ax)) * sign
        sq = ((bx - ax) * (qy - ay) - (by - ay) * (qx - ax)) * sign
        if sp >= 0:
            out.append((px, py))
        if (sp > 0 > sq) or (sp < 0 < sq):
            t = sp / (sp - sq)
            out.append((px + (qx - px) * t, py + (qy - py) * t))
    return out


def area(poly):
    total = 0.0
    for i in range(len(poly)):
        x1, y1 = poly[i - 1]
        x2, y2 = poly[i]
        total += x1 * y2 - x2 * y1
    return total / 2


def main():
    data = [int(w) for w in sys.stdin.read().split()]
    n, k = data[0], data[1]
    coords = data[2:]
    pts = [(coords[2 * i], coords[2 * i + 1]) for i in range(n)]
    k = min(k, n - k)
    if k == 1:
        # every rope lies along the fence: the rabbit cannot get in at all
        print("%.9f" % 1.0)
        return
    whole = area(pts)
    reachable = 0.0
    for i in range(n):
        # the face next to side i is on the side's side of every rope; only
        # the ropes from vertices i + 1 - k, ..., i pass over that side
        mx = pts[i][0] + pts[(i + 1) % n][0]
        my = pts[i][1] + pts[(i + 1) % n][1]
        face = pts
        for j in (i + 1 - k, i) + tuple(range(i + 2 - k, i)):
            ax, ay = pts[j % n]
            bx, by = pts[(j + k) % n]
            side = (bx - ax) * (my - 2 * ay) - (by - ay) * (mx - 2 * ax)
            face = clip(face, ax, ay, bx, by, 1 if side > 0 else -1)
            if not face:
                break
        reachable += area(face) if face else 0.0
    print("%.9f" % ((whole - reachable) / whole))


main()
