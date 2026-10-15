import math
import sys

PERCENT = 100


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def triangle(ax, ay, bx, by, cx, cy):
    # signed area, positive for a counterclockwise triangle
    return cross(bx - ax, by - ay, cx - ax, cy - ay) / 2


def main():
    big, small, near, x, y = (int(v) for v in sys.stdin.read().split())
    d = math.hypot(x, y)
    ux, uy = x / d, y / d
    # the outer common tangents touch both buildings at n * radius from
    # each center, n making cos = -k with the direction to the new one
    k = (near - small) / d
    s = math.sqrt(1 - k * k)
    ends = []
    tangents = []
    for side in (-1, 1):
        nx = -k * ux - side * s * uy
        ny = -k * uy + side * s * ux
        tx, ty = x + near * nx, y + near * ny
        # the line runs away from the old building through the tangent
        # point, and leaves the city where |T + t D| = R
        dx, dy = x + (near - small) * nx, y + (near - small) * ny
        a = dx * dx + dy * dy
        b = tx * dx + ty * dy
        c = tx * tx + ty * ty - big * big
        t = (-b + math.sqrt(b * b - a * c)) / a
        tangents.append((tx, ty))
        ends.append((tx + t * dx, ty + t * dy))
    (t1x, t1y), (t2x, t2y) = tangents
    (e1x, e1y), (e2x, e2y) = ends
    # go around the hidden part counterclockwise: the arc of the new
    # building that faces the old one, the first tangent out to the city
    # border, along the border, the second tangent back
    area = math.acos(k) * near * near
    area += triangle(x, y, t1x, t1y, e1x, e1y)
    area += triangle(x, y, e2x, e2y, t2x, t2y)
    turn = math.atan2(cross(e1x, e1y, e2x, e2y), e1x * e2x + e1y * e2y)
    if turn < 0:
        turn += 2 * math.pi
    # the border arc seen from the new center: a triangle plus the piece
    # of the city cut off by the chord
    area += triangle(x, y, e1x, e1y, e2x, e2y)
    area += turn * big * big / 2 - triangle(0, 0, e1x, e1y, e2x, e2y)
    print("%.10f" % (PERCENT * area / (math.pi * big * big)))


main()
