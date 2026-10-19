import math
import sys

DIMENSIONS = 3
RADIUS = 100
OUTPUT_DIGITS = 10


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def area(points):
    first = tuple(b - a for a, b in zip(points[0], points[1]))
    second = tuple(b - a for a, b in zip(points[0], points[2]))
    normal = cross(first, second)
    norm_squared = dot(normal, normal)
    offset = dot(normal, points[0])
    residual = RADIUS * RADIUS * norm_squared - offset * offset
    if residual <= 0:
        return 0.0

    radius_squared = residual / norm_squared
    axis = tuple(value / math.sqrt(dot(first, first)) for value in first)
    unit_normal = tuple(value / math.sqrt(norm_squared) for value in normal)
    other_axis = cross(unit_normal, axis)
    projected = [(dot(p, axis), dot(p, other_axis)) for p in points]
    total = 0.0
    for index in range(DIMENSIONS):
        following = (index + 1) % DIMENSIONS
        p, end = points[index], points[following]
        delta = tuple(b - a for a, b in zip(p, end))
        quadratic = dot(delta, delta)
        linear = dot(p, delta)
        constant = dot(p, p) - RADIUS * RADIUS
        discriminant = linear * linear - quadratic * constant
        cuts = [0.0, 1.0]
        low, high = 1.0, 0.0
        if discriminant > 0:
            stable = -linear - math.copysign(math.sqrt(discriminant), linear)
            low, high = sorted((stable / quadratic, constant / stable))
            cuts.extend(t for t in (low, high) if 0.0 < t < 1.0)
        cuts.sort()
        x, y = projected[index]
        dx, dy = projected[following][0] - x, projected[following][1] - y
        for left, right in zip(cuts, cuts[1:]):
            ax, ay = x + left * dx, y + left * dy
            bx, by = x + right * dx, y + right * dy
            signed = ax * by - ay * bx
            if low < (left + right) / 2 < high:
                total += signed
            else:
                total += radius_squared * math.atan2(signed, ax * bx + ay * by)
    return abs(total) / 2


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    points = [values[i : i + DIMENSIONS] for i in range(0, len(values), DIMENSIONS)]
    print(f"{area(points):.{OUTPUT_DIGITS}f}")


if __name__ == "__main__":
    main()
