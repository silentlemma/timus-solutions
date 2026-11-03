import math
import sys

STRIPS = 4096
PERCENT = 100
FIELDS = 3  # x, y and the radius of a bomb
MIDDLE = 0.5  # where in its strip the line is taken


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    values = [float(v) for v in data[1 : 1 + FIELDS * n]]
    bombs = [
        (values[FIELDS * i], values[FIELDS * i + 1], values[FIELDS * i + 2] ** 2) for i in range(n)
    ]
    # Midpoint error<=2*sum(r)/STRIPS, below0.005 for at most10 discs.
    # Compute each squared radius once; keep the same clipped interval union.
    covered = 0.0
    for k in range(STRIPS):
        x = (k + MIDDLE) / STRIPS
        pieces = []
        for cx, cy, rr in bombs:
            dx = x - cx
            square = rr - dx * dx
            if square > 0:
                half = math.sqrt(square)
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
