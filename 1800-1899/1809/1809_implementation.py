import sys
from itertools import combinations

SIDE = 20
COUNT = 4
STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def sees(p, a, b):
    """Whether potatoes a and b share a line with nobody between them."""
    (xa, ya), (xb, yb) = p[a], p[b]
    if xa != xb and ya != yb:
        return False
    return not any(
        k != a and k != b and (x, y) != (xa, ya)
        and min(xa, xb) <= x <= max(xa, xb) and min(ya, yb) <= y <= max(ya, yb)
        for k, (x, y) in enumerate(p))


def good(p):
    if len(set(p)) < COUNT or not all(1 <= x <= SIDE and 1 <= y <= SIDE for x, y in p):
        return False
    return all(sum(sees(p, a, b) for b in range(COUNT) if b != a) == 1 for a in range(COUNT))


def main():
    data = list(map(int, sys.stdin.read().split()))
    start = [(data[2 * i], data[2 * i + 1]) for i in range(COUNT)]
    everywhere = [(x, y) for x in range(1, SIDE + 1) for y in range(1, SIDE + 1)]
    answer = None
    if good(start):
        answer = start
    for k in range(COUNT):
        for cell in everywhere:
            if answer is None:
                p = start[:]
                p[k] = cell
                if good(p):
                    answer = p
    if answer is None:
        # two moves always do: next to the two kept potatoes, or as a pair
        # of their own in rows and columns nobody else uses
        for k, l in combinations(range(COUNT), 2):
            kept = [start[i] for i in range(COUNT) if i not in (k, l)]
            near = [(x + dx, y + dy) for x, y in kept for dx, dy in STEPS]
            xs = [x for x in range(1, SIDE + 1) if all(x != kx for kx, _ in kept)]
            ys = [y for y in range(1, SIDE) if all(y != ky and y + 1 != ky for _, ky in kept)]
            pairs = [(a, b) for a in near for b in near] + [((xs[0], ys[0]), (xs[0], ys[0] + 1))]
            for a, b in pairs:
                p = start[:]
                p[k], p[l] = a, b
                if answer is None and good(p):
                    answer = p
    print("\n".join("%d %d" % cell for cell in answer))


main()
