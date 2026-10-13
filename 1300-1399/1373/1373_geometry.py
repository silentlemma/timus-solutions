import sys

STROKE = 4  # numbers per stroke


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    xs, ys = [], []
    for i in range(0, len(data) - STROKE + 1, STROKE):
        ax, ay, bx, by = data[i : i + STROKE]
        dx, dy = bx - ax, by - ay
        # go (p, q), then turn clockwise and go (q, -p): p + q = dx and
        # q - p = dy give the corner a + ((dx - dy) / 2, (dx + dy) / 2), and
        # doubled coordinates keep the halves whole
        xs += [2 * ax, 2 * bx, 2 * ax + dx - dy]
        ys += [2 * ay, 2 * by, 2 * ay + dx + dy]
    width = (max(xs) - min(xs)) / 2 if xs else 0
    height = (max(ys) - min(ys)) / 2 if ys else 0
    print("%.4f %.4f" % (width, height))


main()
