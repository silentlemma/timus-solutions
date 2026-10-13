import sys
from functools import cmp_to_key


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs, ys = data[1 : 1 + 2 * n : 2], data[2 : 2 + 2 * n : 2]
    ox, oy = int(xs[0]), int(ys[0])
    vec = [(int(x) - ox, int(y) - oy) for x, y in zip(xs, ys)]

    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] > 0) else 1

    def cross(a, b):
        return a[0] * b[1] - a[1] * b[0]

    def compare(i, j):
        # by angle around the first pumpkin, nearer first on the same ray
        a, b = vec[i], vec[j]
        if half(a) != half(b):
            return half(a) - half(b)
        c = cross(a, b)
        if c:
            return -c
        return abs(a[0]) + abs(a[1]) - abs(b[0]) - abs(b[1])

    order = sorted(range(1, n), key=cmp_to_key(compare))
    # cut the circle after a turn of at least half a circle, if there is one:
    # then every step turns by less than that and the walk never meets itself
    start = 0
    for k in range(len(order)):
        a, b = vec[order[k - 1]], vec[order[k]]
        c = cross(a, b)
        if c < 0 or (c == 0 and a[0] * b[0] + a[1] * b[1] < 0):
            start = k
    walk = [0] + order[start:] + order[:start]
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(str(i + 1) for i in walk)))


main()
