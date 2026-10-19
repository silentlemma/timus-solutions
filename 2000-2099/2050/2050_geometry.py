import math
import sys

DIMENSION = 3
POINTS = 4
AXIS_THRESHOLD = 1900
AXIS_STEP = 2
ANGLE = 180


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def normalize(a):
    length = math.sqrt(dot(a, a))
    return [x / length for x in a]


def axis(middle, displacement, direction, difference):
    coefficient = dot(displacement, direction) / (2 * dot(direction, direction))
    center = [middle[i] + coefficient * difference[i] for i in range(DIMENSION)]
    unit = normalize(direction)
    projection = dot(center, unit)
    p = [center[i] - projection * unit[i] for i in range(DIMENSION)]
    q = [p[i] + AXIS_STEP * unit[i] for i in range(DIMENSION)]
    return p, q


def solve(points):
    a, b, c, d = points
    first = [b[i] - a[i] for i in range(DIMENSION)]
    second = [d[i] - c[i] for i in range(DIMENSION)]
    if dot(first, second) < 0:
        second = [-value for value in second]
    u, v = normalize(first), normalize(second)
    middle = [(a[i] + c[i]) / 2 for i in range(DIMENSION)]
    displacement = [c[i] - a[i] for i in range(DIMENSION)]
    plus = [u[i] + v[i] for i in range(DIMENSION)]
    minus = [u[i] - v[i] for i in range(DIMENSION)]
    p, q = axis(middle, displacement, plus, minus)
    if dot(p, p) > AXIS_THRESHOLD**2:
        p, q = axis(middle, displacement, minus, plus)
    return p, q


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    points = [values[i * DIMENSION : (i + 1) * DIMENSION] for i in range(POINTS)]
    for row in solve(points):
        print(*(f"{x:.15f}" for x in row))
    print(ANGLE)


if __name__ == "__main__":
    main()
