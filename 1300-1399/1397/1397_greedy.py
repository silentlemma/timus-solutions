import sys
from math import sqrt


def main():
    data = sys.stdin.buffer.read().split()
    pos, out = 0, []
    while pos < len(data):
        m = 2 * int(data[pos])
        coords = [float(v) for v in data[pos + 1 : pos + 1 + 2 * m]]
        xs, ys = coords[::2], coords[1::2]
        pos += 1 + 2 * m
        # total[i]: the sum of distances from point i to all the others
        total = [0.0] * m
        for i, (x, y) in enumerate(zip(xs, ys)):
            row = [sqrt((x - u) ** 2 + (y - v) ** 2) for u, v in zip(xs[i + 1 :], ys[i + 1 :])]
            total[i] += sum(row)
            for k, d in enumerate(row, i + 1):
                total[k] += d
        # a player's score is half the totals of the own points minus the
        # distances to the other colour, which both sides share: take the
        # largest total left, in turns
        total.sort(reverse=True)
        out.append("%.3f" % abs((sum(total[::2]) - sum(total[1::2])) / 2))
    print("\n".join(out))


main()
