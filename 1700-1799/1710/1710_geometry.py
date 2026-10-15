import sys


def main():
    ax, ay, bx, by, cx, cy = (int(w) for w in sys.stdin.read().split())
    # C' on the ray AC with |BC'| = |BC| is the other root t of
    # t^2 - 2 t (AB . u) + |AB|^2 - |BC|^2 = 0, u the unit vector along AC:
    # t' = 2 (AB . AC) / |AC| - |AC|, so C' = A + (C - A) (2 dot - |AC|^2) / |AC|^2
    dot = (bx - ax) * (cx - ax) + (by - ay) * (cy - ay)
    side = (cx - ax) ** 2 + (cy - ay) ** 2
    if 2 * dot <= side or dot == side:
        print("YES")
        return
    k = (2 * dot - side) / side
    print("NO")
    print("%.10f %.10f" % (ax, ay))
    print("%.10f %.10f" % (bx, by))
    print("%.10f %.10f" % (ax + (cx - ax) * k, ay + (cy - ay) * k))


main()
