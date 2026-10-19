import sys


def intersection_area(first, second):
    ax, ay, bx, by = first
    cx, cy, dx, dy = second
    vx, vy = bx - ax, by - ay
    wx, wy = dx - cx, dy - cy
    determinant = vx * wy - vy * wx
    if determinant:
        return (vx * vx + vy * vy) * (wx * wx + wy * wy) / abs(determinant)
    first_low, first_high = sorted((vx * ax + vy * ay, vx * bx + vy * by))
    second_low, second_high = sorted((vx * cx + vy * cy, vx * dx + vy * dy))
    return -1 if max(first_low, second_low) < min(first_high, second_high) else 0


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    middle = len(values) // 2
    answer = intersection_area(values[:middle], values[middle:])
    print(-1 if answer < 0 else f"{answer:.10f}")


if __name__ == "__main__":
    main()
