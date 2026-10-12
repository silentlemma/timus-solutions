import math
import sys

MAX_ROPE = 30000


def main():
    tokens = sys.stdin.read().split()
    ax, ay, bx, by, cx, cy = map(int, tokens[:6])
    rope = 0
    for digit in tokens[6]:
        if digit < '0' or digit > '9':
            continue
        rope = min(MAX_ROPE, rope * 10 + ord(digit) - ord('0'))
        if rope == MAX_ROPE:
            break
    dx, dy = bx - ax, by - ay
    # the nearest point of the bed: C projected onto AB, kept inside it
    length = dx * dx + dy * dy
    t = 0.0 if length == 0 else max(0.0, min(1.0, ((cx - ax) * dx + (cy - ay) * dy) / length))
    nearest = math.hypot(ax + t * dx - cx, ay + t * dy - cy)
    farthest = max(math.hypot(ax - cx, ay - cy), math.hypot(bx - cx, by - cy))
    print("%.2f" % max(0.0, nearest - rope))
    print("%.2f" % max(0.0, farthest - rope))


main()
