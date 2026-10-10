import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    cities = sorted(range(1, n + 1), key=lambda i: (int(data[2 * i - 1]), int(data[2 * i])))
    # neighbours in (x, y) order: each road lies in its own strip of x, and
    # two roads can share only the border line, where they end at different
    # cities because no three cities are on one line
    out = ["%d %d" % (cities[k], cities[k + 1]) for k in range(0, n, 2)]
    print("\n".join(out))


main()
