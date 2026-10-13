import sys
from collections import deque

SIDES = ((1, 0), (-1, 0), (0, 1), (0, -1))


def main():
    n, m, limit, x1, y1, x2, y2 = (int(v) for v in sys.stdin.read().split())

    def inside(x, y):
        return 1 <= x <= n and 1 <= y <= m and (x, y) != (x2, y2)

    # the fewest steps from the knight to every cell, around the demon
    dist = {(x1, y1): 0}
    queue = deque([(x1, y1)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in SIDES:
            nx, ny = x + dx, y + dy
            if inside(nx, ny) and (nx, ny) not in dist:
                dist[(nx, ny)] = dist[(x, y)] + 1
                queue.append((nx, ny))

    # the strike comes from a cell next to the demon after a straight run of
    # k steps; its start must be reachable with the steps that are left
    best = 0
    for ax, ay in ((x2 + dx, y2 + dy) for dx, dy in SIDES):
        if not inside(ax, ay):
            continue
        for dx, dy in SIDES:
            k = 0
            while True:
                sx, sy = ax - k * dx, ay - k * dy
                if not inside(sx, sy):
                    break
                if (sx, sy) in dist and dist[(sx, sy)] + k <= limit:
                    best = max(best, k + 1)
                k += 1
    print(best)


main()
