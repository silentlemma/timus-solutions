import math
import sys

NUMBERS = 6  # W, D and the two points


def unfolded(start, end, size, low, hits):
    """The distance along one axis once the room is mirrored at each hit."""
    if not hits:
        return abs(end - start)
    first = start if hits[0] == low else size - start
    last = end if hits[-1] == low else size - end
    return first + (len(hits) - 1) * size + last


def main():
    data = sys.stdin.read().split()
    w, d, x0, y0, x1, y1 = (int(t) for t in data[:NUMBERS])
    walls = "".join(data[NUMBERS:])
    dx = unfolded(x0, x1, w, "L", [c for c in walls if c in "LR"])
    dy = unfolded(y0, y1, d, "F", [c for c in walls if c in "FB"])
    print("%.4f" % math.sqrt(dx * dx + dy * dy))


main()
