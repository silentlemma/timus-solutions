import math
import sys

CORNERS = 3
WIDE = 2 * math.pi / 3  # 120 degrees


def main():
    v = [float(x) for x in sys.stdin.read().split()]
    p = list(zip(v[0::2], v[1::2]))
    angle, side = [], []
    for i in range(CORNERS):
        a, b, c = p[i], p[(i + 1) % CORNERS], p[(i + 2) % CORNERS]
        ux, uy, wx, wy = b[0] - a[0], b[1] - a[1], c[0] - a[0], c[1] - a[1]
        angle.append(math.atan2(abs(ux * wy - uy * wx), ux * wx + uy * wy))
        side.append(math.hypot(c[0] - b[0], c[1] - b[1]))
    for i in range(CORNERS):
        if angle[i] >= WIDE:
            # a corner of at least 120 degrees is the best place itself
            print("%.8f %.8f" % p[i])
            return
    # otherwise the Fermat point: every side is seen at 120 degrees, and its
    # barycentric weights are a / sin(A + 60 degrees) and so on
    w = [side[i] / math.sin(angle[i] + math.pi / CORNERS) for i in range(CORNERS)]
    total = sum(w)
    x = sum(w[i] * p[i][0] for i in range(CORNERS)) / total
    y = sum(w[i] * p[i][1] for i in range(CORNERS)) / total
    print("%.8f %.8f" % (x, y))


main()
