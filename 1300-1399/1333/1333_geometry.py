import math
import sys

STRIPS = 20000
PERCENT = 100
FIELDS = 3  # x, y and the radius of a bomb
MIDDLE = 0.5  # where in its strip the line is taken


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    values = [float(v) for v in data[1 : 1 + FIELDS * n]]
    bombs = [values[FIELDS * i : FIELDS * (i + 1)] for i in range(n)]
    # the area is the sum over thin vertical strips of the covered part of
    # the line through the middle of each strip
    covered = 0.0
    for k in range(STRIPS):
        x = (k + MIDDLE) / STRIPS
        pieces = []
        for cx, cy, r in bombs:
            if abs(x - cx) < r:
                half = math.sqrt(r * r - (x - cx) ** 2)
                low, high = max(0.0, cy - half), min(1.0, cy + half)
                if low < high:
                    pieces.append((low, high))
        pieces.sort()
        end = 0.0
        for low, high in pieces:
            if high > end:
                covered += high - max(low, end)
                end = high
    print("%.6f" % (covered / STRIPS * PERCENT))


main()
