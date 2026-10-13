import math
import sys

STOP = b"0"
HALF = math.sqrt(0.5)  # each axis of a diagonal jump
# the numeric keypad: the jump of each key in steps east and north
DX = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
DY = [0, -1, -1, -1, 0, 0, 0, 1, 1, 1]


def main():
    keys = sys.stdin.buffer.read().split(STOP, 1)[0]
    # straight jumps add whole metres, diagonal ones 1/sqrt(2) on each axis
    straight = [0, 0]
    diagonal = [0, 0]
    for key in range(len(DX)):
        times = keys.count(str(key).encode())
        part = diagonal if DX[key] and DY[key] else straight
        part[0] += DX[key] * times
        part[1] += DY[key] * times
    x = straight[0] + diagonal[0] * HALF
    y = straight[1] + diagonal[1] * HALF
    print("%.10f %.10f" % (x, y))


main()
