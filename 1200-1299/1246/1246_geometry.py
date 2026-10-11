import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    xs, ys = data[1 : 1 + 2 * n : 2], data[2 : 2 + 2 * n : 2]
    # twice the signed area by the shoelace formula: positive when the
    # runner goes counterclockwise, and the rope winds the same way
    twice = sum(map(int.__mul__, xs, ys[1:] + ys[:1])) - sum(map(int.__mul__, xs[1:] + xs[:1], ys))
    print("ccw" if twice > 0 else "cw")


main()
