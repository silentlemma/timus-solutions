import sys
from math import acos, atan2, sqrt, tau

ANGLE_EPS = 1e-12


def most_cities(points, reach):
    if reach < 0:
        return 0
    if reach == 0:
        return min(1, len(points))
    diameter = 2 * reach
    diameter_squared = diameter * diameter
    best = 1
    for x, y in points:
        events = []
        active = 1
        for a, b in points:
            dx, dy = a - x, b - y
            distance_squared = dx * dx + dy * dy
            if distance_squared == 0 or distance_squared > diameter_squared:
                continue
            direction = atan2(dy, dx)
            half_width = acos(sqrt(distance_squared) / diameter)
            # Expand closed intervals slightly to include shared endpoints.
            start = (direction - half_width - ANGLE_EPS) % tau
            end = (direction + half_width + ANGLE_EPS) % tau
            active += start > end
            events.append((start, -1))
            events.append((end, 1))
        events.sort()
        best = max(best, active)
        for _, change in events:
            active -= change
            if active > best:
                best = active
        if best == len(points):
            break
    return best


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(data)
    points = [(next(data), next(data)) for _ in range(count)]
    reach = next(data) - next(data)
    print(most_cities(points, reach))


if __name__ == "__main__":
    main()
