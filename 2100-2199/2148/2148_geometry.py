import math
import sys


def main():
    cx, cy, r, ax, ay, bx, by = map(int, sys.stdin.read().split())
    # The players are equally far from the centre, so the mirror point lies on
    # the bisector of the angle between them, in the direction w = A + B - 2C.
    wx, wy = ax + bx - 2 * cx, ay + by - 2 * cy
    # Both shots stay outside the tank exactly when each player is strictly
    # beyond the tangent line at that point: (A - C) . w > r |w|.
    dot = (ax - cx) * wx + (ay - cy) * wy
    norm = wx * wx + wy * wy
    if dot <= 0 or dot * dot <= r * r * norm:
        print("No way")
        return
    scale = r / math.sqrt(norm)
    print("%.9f %.9f" % (cx + wx * scale, cy + wy * scale))


main()
