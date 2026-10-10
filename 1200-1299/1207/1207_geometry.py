import sys
from functools import cmp_to_key


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = list(map(int, data[1 : 2 * n + 1 : 2]))
    ys = list(map(int, data[2 : 2 * n + 2 : 2]))
    # the lowest point (the leftmost of the lowest) sees all others within
    # half a turn, so they can be sorted by angle with cross products
    pivot = min(range(n), key=lambda i: (ys[i], xs[i]))
    px, py = xs[pivot], ys[pivot]

    def turn(i, j):
        cross = (xs[i] - px) * (ys[j] - py) - (ys[i] - py) * (xs[j] - px)
        return (cross < 0) - (cross > 0)

    others = sorted((i for i in range(n) if i != pivot), key=cmp_to_key(turn))
    # the middle one leaves (n - 2) / 2 points on each side of the line
    print(pivot + 1, others[(n - 2) // 2] + 1)


main()
