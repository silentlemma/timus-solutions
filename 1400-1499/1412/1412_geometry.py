import math
import sys


def cut(ax, ay, bx, by):
    """Signed area of the unit disk at the origin inside the triangle (origin, a, b)."""
    dx, dy = bx - ax, by - ay
    qa, qb, qc = dx * dx + dy * dy, ax * dx + ay * dy, ax * ax + ay * ay - 1
    marks = [0.0, 1.0]
    disc = qb * qb - qa * qc
    if disc > 0:
        root = math.sqrt(disc)
        marks += [t for t in ((-qb - root) / qa, (-qb + root) / qa) if 0 < t < 1]
    marks.sort()
    area = 0.0
    for s, t in zip(marks, marks[1:]):
        px, py, qx, qy = ax + dx * s, ay + dy * s, ax + dx * t, ay + dy * t
        mx, my = (px + qx) / 2, (py + qy) / 2
        cross = px * qy - py * qx
        # a piece inside the disk adds its triangle, one outside adds its sector
        area += cross / 2 if mx * mx + my * my < 1 else math.atan2(cross, px * qx + py * qy) / 2
    return area


def change(x, y, width, length):
    """Water that one umbrella moves off or onto the field."""
    corners = [(-x, -y), (length - x, -y), (length - x, width - y), (-x, width - y)]
    covered = sum(cut(*corners[i - 1], *corners[i]) for i in range(len(corners)))
    # the rim splits into arcs at the field's border lines
    turn = 2 * math.pi
    angles = [0.0, turn]
    for d in (-x, length - x):
        if abs(d) <= 1:
            angles += [math.acos(d), turn - math.acos(d)]
    for d in (-y, width - y):
        if abs(d) <= 1:
            angles += [math.asin(d) % turn, math.pi - math.asin(d)]
    angles.sort()
    inside = 0.0
    for s, t in zip(angles, angles[1:]):
        m = (s + t) / 2
        if 0 <= x + math.cos(m) <= length and 0 <= y + math.sin(m) <= width:
            inside += t - s
    # rain caught over the whole disk leaves from the rim evenly by angle
    return math.pi * inside / turn - covered


def main():
    width, length, n, *rest = sys.stdin.read().split()
    width, length = int(width), int(length)
    coords = iter(map(float, rest[: 2 * int(n)]))
    total = float(width * length)
    for x, y in zip(coords, coords):
        total += change(x, y, width, length)
    print("%.3f" % total)


main()
