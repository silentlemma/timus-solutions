import math
import sys

EPS = 1e-9


def main():
    words = iter(sys.stdin.read().split())
    n, h = int(next(words)), float(next(words))
    poly = [(float(next(words)), float(next(words))) for _ in range(n)]
    d, lx, ly = float(next(words)), float(next(words)), float(next(words))
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(poly, poly[1:] + poly[:1]))
    if area < 0:
        poly.reverse()
    # each side as an outward normal (nx, ny) and an offset: inside the lot
    # every side has nx x + ny y <= c
    sides = []
    for (ax, ay), (bx, by) in zip(poly, poly[1:] + poly[:1]):
        nx, ny = by - ay, ax - bx
        sides.append((nx, ny, nx * ax + ny * ay))
    shot = 0
    for _ in range(int(next(words))):
        px, py = float(next(words)), float(next(words))
        scale = math.hypot(px - lx, py - ly) + 1
        if all(nx * px + ny * py <= c + EPS * math.hypot(nx, ny) * scale for nx, ny, c in sides):
            shot += 1  # over the lot the laser always reaches it in time
            continue
        # the beam leaves the lot at horizontal distance a and must clear
        # the fence there, so it meets the stone no lower than h r / a
        r = math.hypot(px - lx, py - ly)
        ux, uy = (px - lx) / r, (py - ly) / r
        a = min(
            (c - nx * lx - ny * ly) / (nx * ux + ny * uy)
            for nx, ny, c in sides
            if nx * ux + ny * uy > 0
        )
        if r * r * (a * a + h * h) <= d * d * a * a * (1 + EPS):
            shot += 1
    print(shot)


main()
