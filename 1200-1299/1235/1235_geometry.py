import sys

HEADER = 3


def main():
    data = list(map(int, sys.stdin.read().split()))
    w, h = data[1], data[2]
    trees = list(zip(data[HEADER::2], data[HEADER + 1 :: 2]))
    # a largest square slides left and down until its sides meet a tree or
    # the park border, so its corner has x = 0 or a tree x and y = 0 or a tree y
    best = (0, 0, 0)
    for p in {0, *(x for x, _ in trees)}:
        right = [(x - p, y) for x, y in trees if x > p]
        for q in {0, *(y for _, y in trees)}:
            # a tree up and to the right of the corner is inside unless the
            # side stops at its larger distance
            side = min(w - p, h - q)
            for dx, y in right:
                if y > q:
                    side = min(side, max(dx, y - q))
            if side > best[2]:
                best = (p, q, side)
    print(*best)


main()
