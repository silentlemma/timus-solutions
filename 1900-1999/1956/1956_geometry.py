from collections import Counter
from operator import itemgetter
import math
import sys


def minimum_distance(points):
    counted = list(Counter(points).items())
    best = math.inf
    for index, ((px, py), _) in enumerate(counted[:-1]):
        directions = []
        total_x = total_y = 0.0
        for other, ((qx, qy), weight) in enumerate(counted):
            if other == index:
                continue
            dx, dy = float(qx - px), float(qy - py)
            if dy < 0 or dy == 0 and dx < 0:
                dx, dy = -dx, -dy
            wx, wy = dx * weight, dy * weight
            directions.append((-dx / (abs(dx) + dy), dx, dy, wx + wx, wy + wy, other))
            total_x += wx
            total_y += wy
        directions.sort(key=itemgetter(0))
        for _, dx, dy, twice_x, twice_y, other in directions:
            if other > index:
                numerator = dx * total_y - dy * total_x
                if numerator == 0:
                    return 0.0
                value = numerator / math.sqrt(dx * dx + dy * dy)
                if value < best:
                    best = value
            total_x -= twice_x
            total_y -= twice_y
    return 0.0 if len(counted) < 2 else best


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    count = data[0]
    points = list(zip(data[1::2], data[2::2]))
    print(f"{minimum_distance(points[:count]):.12f}")


if __name__ == "__main__":
    main()
