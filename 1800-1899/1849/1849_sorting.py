import sys
from array import array
from bisect import bisect_left
from math import gcd

SPAN = 10000  # coordinates lie in [-SPAN, SPAN]
REACH = 10  # direction parts lie in [-REACH, REACH]


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rabbits = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    pos = 1 + 2 * n
    q = int(data[pos])
    rest = map(int, data[pos + 1:])
    x, y, vx, vy = next(rest), next(rest), next(rest), next(rest)
    ax, bx, ay, by, avx, bvx, avy, bvy = rest
    width, turn = 2 * SPAN + 1, 2 * REACH + 1
    # every direction (vx, vy) is filed under its primitive vector
    primitive, kind = [], {}
    for dx in range(-REACH, REACH + 1):
        for dy in range(-REACH, REACH + 1):
            g = gcd(dx, dy)
            if g:
                key = (dx // g, dy // g)
                if key not in kind:
                    kind[key] = len(primitive)
                    primitive.append(key)
    code = [kind[(dx // gcd(dx, dy), dy // gcd(dx, dy))] if dx or dy else 0
            for dx in range(-REACH, REACH + 1) for dy in range(-REACH, REACH + 1)]
    xs, ys, kinds = array("i", [0]) * q, array("i", [0]) * q, array("i", [0]) * q
    for i in range(q):
        xs[i], ys[i] = x, y
        kinds[i] = code[(vx + REACH) * turn + vy + REACH]
        x = (ax * (x + SPAN) + bx) % width - SPAN
        y = (ay * (y + SPAN) + by) % width - SPAN
        vx = (avx * (vx + REACH) + bvx) % turn - REACH
        vy = (avy * (vy + REACH) + bvy) % turn - REACH
    # the shots in order of their direction, by counting
    start = [0] * (len(primitive) + 1)
    for k in kinds:
        start[k + 1] += 1
    for k in range(len(primitive)):
        start[k + 1] += start[k]
    shots = array("i", [0]) * q
    fill = start[:]
    for i in range(q):
        shots[fill[kinds[i]]] = i
        fill[kinds[i]] += 1
    best, best_count = 0, -1
    for k, (dx, dy) in enumerate(primitive):
        if start[k] == start[k + 1]:
            continue
        # rabbits on each line along (dx, dy), by their place along it
        lines = {}
        for rx, ry in rabbits:
            lines.setdefault(rx * dy - ry * dx, []).append(rx * dx + ry * dy)
        for places in lines.values():
            places.sort()
        for j in range(start[k], start[k + 1]):
            i = shots[j]
            places = lines.get(xs[i] * dy - ys[i] * dx)
            if places is None:
                continue
            got = len(places) - bisect_left(places, xs[i] * dx + ys[i] * dy)
            # a later shot wins a tie
            if got > best_count or (got == best_count and i > best):
                best, best_count = i, got
    if best_count <= 0:
        best_count, best = 0, q - 1
    print(best + 1, best_count)


main()
