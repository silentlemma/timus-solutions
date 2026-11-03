import sys


def index(n, m, r, c):
    layer = min(r, c, n - 1 - r, m - 1 - c)
    height, width = n - 2 * layer, m - 2 * layer
    r, c = r - layer, c - layer
    # Outer layers contain exactly the cells outside this remaining rectangle.
    before = n * m - height * width
    if height == 1:
        offset = c
    elif width == 1:
        offset = r
    elif r == 0:
        offset = c
    elif c == width - 1:
        offset = width - 1 + r
    elif r == height - 1:
        offset = width - 1 + height - 1 + width - 1 - c
    else:
        offset = 2 * (height + width - 2) - r
    return before + offset


def main():
    n, m, r1, c1, r2, c2 = map(int, sys.stdin.read().split())
    print(abs(index(n, m, r1 - 1, c1 - 1) - index(n, m, r2 - 1, c2 - 1)))


main()
