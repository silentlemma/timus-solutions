import math
import sys


def angle(px, ax, ay, bx, by):
    ux, uy, vx, vy = ax - px, ay, bx - px, by
    return math.atan2(abs(ux * vy - uy * vx), ux * vx + uy * vy)


def main():
    x1, y1, x2, y2 = map(int, sys.stdin.read().split())
    if y1 * y2 < 0 or (y1 * y2 == 0 and x1 != x2):
        best = math.pi  # stand on the billboard itself
    elif y1 * y2 == 0:
        best = math.pi / 2  # a vertical billboard standing on the road
    else:
        y1, y2 = abs(y1), abs(y2)
        if y1 == y2:
            spots = [(x1 + x2) / 2]
        else:
            # the best spot is where a circle through both ends touches the road:
            # its distance from where the billboard's line meets the road is sqrt(QA * QB)
            qx = x1 - y1 * (x2 - x1) / (y2 - y1)
            reach = math.sqrt(math.hypot(x1 - qx, y1) * math.hypot(x2 - qx, y2))
            spots = [qx - reach, qx + reach]
        best = max(angle(p, x1, y1, x2, y2) for p in spots)
    print("%.6f" % best)


main()
