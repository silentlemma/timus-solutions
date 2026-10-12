import math
import sys

HALF_TURN = 180.0


def main():
    w, h, n, ax, ay, bx, by = map(int, sys.stdin.read().split())

    def images(bounces):
        """The mirror images of B that a straight line from A reaches
        after the given number of bounces: i walls across, j walls up."""
        for i in range(-bounces, bounces + 1):
            rest = bounces - abs(i)
            for j in sorted({rest, -rest}):
                x = i * w + (bx if i % 2 == 0 else w - bx)
                y = j * h + (by if j % 2 == 0 else h - by)
                yield x, y

    best = None
    for x, y in images(n):
        dx, dy = x - ax, y - ay
        length = dx * dx + dy * dy
        angle = math.atan2(dy, dx) * HALF_TURN / math.pi
        if angle < 0:
            angle += 2 * HALF_TURN
        if best is None or (length, angle) < best:
            best = (length, angle)
    print("%.2f" % best[1])


main()
