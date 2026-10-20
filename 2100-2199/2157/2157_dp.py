import sys
from bisect import bisect_right
from math import isqrt, sqrt

COORDINATE_LIMIT = 10000
GRAVITY = 10
HALF_GRAVITY = GRAVITY // 2
OUTPUT_DIGITS = 9


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count, start_x, start_y = next(data), next(data), next(data)
    points = []
    for _ in range(count):
        x, y, density = next(data), next(data), next(data)
        points.append((y, x + COORDINATE_LIMIT, density))
    points.append((start_y, start_x + COORDINATE_LIMIT, 0))
    points.sort()

    fall_time = [sqrt(height / HALF_GRAVITY) for height in range(start_y + 1)]
    column_count = 2 * COORDINATE_LIMIT + 1
    heights = [[] for _ in range(column_count)]
    durations = [[] for _ in range(column_count)]
    max_radius = isqrt((start_y - 1) // HALF_GRAVITY)
    offsets = [
        [(dx, HALF_GRAVITY * dx * dx) for dx in range(-radius, radius + 1)]
        for radius in range(max_radius + 1)
    ]

    answer = 0.0
    for height, source_column, density in points:
        best = fall_time[height]
        radius = isqrt((height - 1) // HALF_GRAVITY)
        for dx, drop in offsets[radius]:
            column = source_column + dx
            if column < 0 or column >= column_count:
                continue
            levels = heights[column]
            if not levels:
                continue
            index = bisect_right(levels, height - drop) - 1
            if index < 0:
                continue
            # The highest reachable cloud dominates lower clouds in this column.
            candidate = fall_time[height - levels[index]] + durations[column][index]
            if candidate > best:
                best = candidate
        answer = best + density
        heights[source_column].append(height)
        durations[source_column].append(answer)

    print(f"{answer:.{OUTPUT_DIGITS}f}")


if __name__ == "__main__":
    main()
