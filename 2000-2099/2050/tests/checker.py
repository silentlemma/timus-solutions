"""Check any bounded rotation by applying its quaternion to the source line."""

import math
from pathlib import Path
import sys

DIMENSION = 3
POINTS = 4
ANSWER_FIELDS = 7
COORDINATE_BOUND = 2000
FULL_TURN = 360
TOLERANCE = 1e-5


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def validate(points, raw):
    try:
        tokens = raw.decode("ascii").split()
        if len(tokens) != ANSWER_FIELDS:
            return False
        values = list(map(float, tokens))
    except (ValueError, UnicodeDecodeError, OverflowError):
        return False
    if not all(math.isfinite(x) for x in values):
        return False
    p, q = values[:DIMENSION], values[DIMENSION : 2 * DIMENSION]
    angle = values[-1]
    if any(abs(x) > COORDINATE_BOUND for x in p + q) or not 0 <= angle <= FULL_TURN:
        return False
    axis = [p[i] - q[i] for i in range(DIMENSION)]
    norm = math.sqrt(dot(axis, axis))
    if norm < 1:
        return False
    half_angle = math.radians(angle) / 2
    scalar = math.cos(half_angle)
    vector = [x * math.sin(half_angle) / norm for x in axis]

    def rotate(offset):
        first = cross(vector, offset)
        second = cross(vector, first)
        return [offset[i] + 2 * (scalar * first[i] + second[i]) for i in range(DIMENSION)]

    a, b, c, d = points
    origin_offset = rotate([c[i] - p[i] for i in range(DIMENSION)])
    origin = [p[i] + origin_offset[i] for i in range(DIMENSION)]
    direction = rotate([d[i] - c[i] for i in range(DIMENSION)])
    length_squared = dot(direction, direction)
    if not math.isfinite(length_squared) or length_squared == 0:
        return False
    for target in (a, b):
        normal = cross([target[i] - origin[i] for i in range(DIMENSION)], direction)
        distance_squared = dot(normal, normal) / length_squared
        if not math.isfinite(distance_squared) or distance_squared > TOLERANCE**2:
            return False
    return True


def main():
    values = list(map(int, Path(sys.argv[1]).read_text(encoding="ascii").split()))
    points = [values[i * DIMENSION : (i + 1) * DIMENSION] for i in range(POINTS)]
    if not validate(points, Path(sys.argv[3]).read_bytes()):
        print("Invalid axis, angle or rotated source line")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
