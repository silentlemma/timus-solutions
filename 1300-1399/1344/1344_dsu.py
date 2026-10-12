import sys

CEILING, TURNIP, FREE = 0, -1, -2
ONE, MASS = 0, 1  # the turnip's weight of 1 and the unknown mass
FIELDS = 4


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    blocks = [data[1 + FIELDS * i : 1 + FIELDS * (i + 1)] for i in range(n)]

    def rope(i):
        return 2 * i + 2  # tension in the rope over block i

    def axle(i):
        return rope(i) + 1  # tension in the rope at the axle of block i

    # every tension is a power of two times the tension at the root of its
    # group: value(x) = 2 ** shift[x] * value(root)
    parent = list(range(2 * n + 2))
    shift = [0] * (2 * n + 2)
    zero = [False] * (2 * n + 2)  # the whole group must have no tension

    def find(x):
        if parent[x] == x:
            return x
        root = find(parent[x])
        shift[x] += shift[parent[x]]
        parent[x] = root
        return root

    def tie(x, y, k):
        """value(x) = 2 ** k * value(y)"""
        rx, ry = find(x), find(y)
        if rx == ry:
            if shift[x] != k + shift[y]:
                zero[rx] = True
            return
        parent[rx] = ry
        shift[rx] = k + shift[y] - shift[x]
        zero[ry] = zero[ry] or zero[rx]

    # ports of a block: the two rope ends and the axle, with the way they
    # leave it; a first-type block hangs its rope ends down
    def ports(i):
        kind, x1, x2, y = blocks[i]
        down = kind == 1
        return [(rope(i), x1, down), (rope(i), x2, down), (axle(i), y, not down)]

    for i in range(n):
        tie(axle(i), rope(i), 1)  # the axle holds both ends of the rope
        for node, target, down in ports(i):
            if target == TURNIP:
                tie(node, ONE, 0)
            elif target == FREE:
                tie(node, MASS, 0)
            elif target != CEILING:
                # the other end leaves block target the opposite way
                for other, back, other_down in ports(target - 1):
                    if back == i + 1 and other_down != down:
                        tie(node, other, 0)
                        break
    one, mass = find(ONE), find(MASS)
    if zero[one]:
        print("No solution")
    elif one == mass:
        print("%.4f" % 2.0 ** (shift[MASS] - shift[ONE]))
    elif zero[mass]:
        print("%.4f" % 0.0)
    else:
        print("Any")


main()
