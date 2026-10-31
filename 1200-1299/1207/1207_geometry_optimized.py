import sys
from array import array

COORDINATE_LIMIT = 1000000
KEY_SHIFT = 42


def main():
    source = sys.stdin.buffer
    n = int(source.readline())
    # coordinates in [-10^6, 10^6] fit signed 32-bit array elements.
    xs, ys = array("i"), array("i")
    pivot = 0
    for i in range(n):
        x, y = map(int, source.readline().split())
        xs.append(x)
        ys.append(y)
        if (y, x) < (ys[pivot], xs[pivot]):
            pivot = i
    px, py = xs[pivot], ys[pivot]
    horizontal = -(2 * COORDINATE_LIMIT << KEY_SHIFT) - 1

    def angle_key(i):
        # distinct slopes differ by at least 1/(2000000^2); scaling by 2^42
        # separates them by more than one, so integer division preserves their order.
        return -((xs[i] - px) << KEY_SHIFT) // (ys[i] - py) if ys[i] != py else horizontal

    others = sorted((i for i in range(n) if i != pivot), key=angle_key)
    print(pivot + 1, others[(n - 2) // 2] + 1)


main()
