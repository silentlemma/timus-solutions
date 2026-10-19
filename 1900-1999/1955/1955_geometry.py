import math
import sys


def line_span(points, edges, px, py, dx, dy, require_visible=False):
    offset = dx * py - dy * px
    hits = []
    boundary = []
    previous = dx * points[-1][1] - dy * points[-1][0] - offset
    squared = dx * dx + dy * dy
    for index, (ex, ey, constant) in enumerate(edges):
        denominator = dx * ey - dy * ex
        height = previous + denominator
        if (previous > 0) != (height > 0):
            numerator = constant - px * ey + py * ex
            if require_visible and previous != 0 and height != 0:
                if 0 < numerator < denominator or denominator < numerator < 0:
                    return 0.0, False
            hits.append(numerator / denominator)
        elif height == 0 and previous == 0:
            ax, ay = points[index - 1]
            bx, by = points[index]
            first = ((ax - px) * dx + (ay - py) * dy) / squared
            second = ((bx - px) * dx + (by - py) * dy) / squared
            boundary.append((min(first, second), max(first, second)))
        previous = height
    hits.sort()
    intervals = boundary + list(zip(hits[::2], hits[1::2]))
    if not intervals:
        return 0.0, False
    intervals.sort()
    left, right = intervals[0]
    best = 0.0
    visible = False
    for start, end in intervals[1:]:
        if start <= right:
            right = max(right, end)
        else:
            best = max(best, right - left)
            visible = visible or left <= 0 and right >= 1
            left, right = start, end
    return max(best, right - left), visible or left <= 0 and right >= 1


def longest_segment(points):
    edges = []
    lower = 0
    for index, (bx, by) in enumerate(points):
        ax, ay = points[index - 1]
        edges.append((bx - ax, by - ay, ax * by - ay * bx))
        lower = max(lower, (bx - ax) ** 2 + (by - ay) ** 2)
    diameter = 0
    endpoints = None
    for index, (px, py) in enumerate(points):
        for qx, qy in points[:index]:
            squared = (qx - px) ** 2 + (qy - py) ** 2
            if squared > diameter:
                diameter = squared
                endpoints = px, py, qx - px, qy - py
    span, visible = line_span(points, edges, *endpoints)
    if visible:
        return math.sqrt(diameter)
    best_squared = max(float(lower), span * span * diameter)
    width = max(x for x, y in points) - min(x for x, y in points)
    height = max(y for x, y in points) - min(y for x, y in points)
    width_squared, height_squared = width * width, height * height
    seen = set()
    for index, (px, py) in enumerate(points):
        for qx, qy in points[:index]:
            dx, dy = qx - px, qy - py
            squared = dx * dx + dy * dy
            if (
                width_squared * squared < lower * dx * dx
                or height_squared * squared < lower * dy * dy
            ):
                continue
            divisor = math.gcd(dx, dy)
            nx, ny = dx // divisor, dy // divisor
            if nx < 0 or nx == 0 and ny < 0:
                nx, ny = -nx, -ny
            key = nx, ny, nx * py - ny * px
            if key in seen:
                continue
            span, visible = line_span(points, edges, px, py, dx, dy, True)
            if not visible:
                continue
            seen.add(key)
            if visible:
                lower = max(lower, squared)
                if lower == diameter:
                    return math.sqrt(diameter)
            best_squared = max(best_squared, span * span * squared, float(lower))
    return math.sqrt(best_squared)


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    count = values[0]
    points = list(zip(values[1::2], values[2::2]))
    print(f"{longest_segment(points[:count]):.12f}")


if __name__ == "__main__":
    main()
