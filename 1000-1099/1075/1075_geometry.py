import math
import sys


def main():
    ax, ay, az, bx, by, bz, cx, cy, cz, r = map(int, sys.stdin.read().split())
    u = (ax - cx, ay - cy, az - cz)
    v = (bx - cx, by - cy, bz - cz)
    dot = u[0] * v[0] + u[1] * v[1] + u[2] * v[2]
    cross = math.hypot(
        u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]
    )
    angle = math.atan2(cross, dot)
    da, db = math.hypot(*u), math.hypot(*v)
    # seen from C, the tangents from A and B cover these angles; when the angle
    # ACB fits in them, the segment AB misses the ball
    reach = math.acos(r / da) + math.acos(r / db)
    if angle <= reach:
        length = math.hypot(ax - bx, ay - by, az - bz)
    else:
        length = math.sqrt(da * da - r * r) + math.sqrt(db * db - r * r) + r * (angle - reach)
    print("%.2f" % length)


main()
