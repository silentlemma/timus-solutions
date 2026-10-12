import math
import sys

EPS = 1e-7


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    cities = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]
    reach = data[1 + 2 * n] - data[2 + 2 * n]  # how far a center may be
    if reach < 0:
        print(0)
        return
    # a best circle can be moved until it passes through two centers or
    # stands on one, so only such places need to be tried
    places = [(float(x), float(y)) for x, y in cities]
    for i in range(n):
        for j in range(i):
            (ax, ay), (bx, by) = cities[i], cities[j]
            dx, dy = bx - ax, by - ay
            half = math.hypot(dx, dy) / 2
            if 0 < half <= reach:
                rise = math.sqrt(max(0.0, reach * reach - half * half)) / (2 * half)
                mx, my = (ax + bx) / 2, (ay + by) / 2
                places.append((mx - dy * rise, my + dx * rise))
                places.append((mx + dy * rise, my - dx * rise))
    limit = (reach + EPS) ** 2
    best = 0
    for px, py in places:
        inside = sum((x - px) ** 2 + (y - py) ** 2 <= limit for x, y in cities)
        if inside > best:
            best = inside
    print(best)


main()
