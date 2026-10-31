import math
import sys

COORDINATES = 6


def main():
    tokens = sys.stdin.read().split()
    ax, ay, bx, by, cx, cy = map(int, tokens[:COORDINATES])
    # an unbounded rope may become infinity; then both extensions are zero.
    rope = float(tokens[COORDINATES])
    dx, dy = bx - ax, by - ay
    # the nearest point of the bed: C projected onto AB, kept inside it
    length = dx * dx + dy * dy
    t = 0.0 if length == 0 else max(0.0, min(1.0, ((cx - ax) * dx + (cy - ay) * dy) / length))
    nearest = math.hypot(ax + t * dx - cx, ay + t * dy - cy)
    farthest = max(math.hypot(ax - cx, ay - cy), math.hypot(bx - cx, by - cy))
    print("%.2f" % max(0.0, nearest - rope))
    print("%.2f" % max(0.0, farthest - rope))


main()
