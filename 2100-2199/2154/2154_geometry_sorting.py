import math
import sys


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(values)
    points = [(next(values), next(values)) for _ in range(count)]
    if (0, 0) in points:
        print(f"{0:.10f}")
        return

    # Slopes order directions modulo pi; bounded integer slopes stay distinct.
    points.sort(key=lambda point: point[0] / point[1] if point[1] else math.inf)
    answer = math.inf
    previous_x, previous_y = points[-1]
    for x, y in points:
        cross = previous_x * y - previous_y * x
        dx = previous_x - x
        dy = previous_y - y
        distance = abs(cross) / math.sqrt(dx * dx + dy * dy)
        if distance < answer:
            answer = distance
        previous_x, previous_y = x, y

    print(f"{answer:.10f}")


if __name__ == "__main__":
    main()
