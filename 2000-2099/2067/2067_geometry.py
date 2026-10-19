import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = list(map(int, data[1:2 * n + 1:2]))
    r = list(map(int, data[2:2 * n + 2:2]))
    # v, u are best friends exactly when every other point lies on the
    # segment vu: all points collinear, v and u the two extreme ones
    ds, dr = s[1] - s[0], r[1] - r[0]
    if any(ds * (r[i] - r[0]) != (s[i] - s[0]) * dr for i in range(2, n)):
        print(0)
        return
    points = sorted(range(n), key=lambda i: (s[i], r[i]))
    print(1)
    print(points[0] + 1, points[-1] + 1)


main()
