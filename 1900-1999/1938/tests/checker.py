"""Check the actual six decimal coordinates with high-precision geometric distances."""

from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
import re
import sys

PRECISION_DIGITS = 80
COORDINATE_BOUND = Decimal(100000000)
TOLERANCE = Decimal("0.000001")
LINE_COUNT = 3
COORDINATES_PER_LINE = 4
REAL_PATTERN = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")


def check(lines, output):
    tokens = output.split()
    if len(tokens) != 2 * LINE_COUNT or any(
        REAL_PATTERN.fullmatch(token) is None for token in tokens
    ):
        return False, "expected exactly six finite decimal coordinates", None
    try:
        coordinates = [Decimal(token) for token in tokens]
    except InvalidOperation:
        return False, "invalid decimal coordinate", None
    if any(
        not value.is_finite() or value.copy_abs() > COORDINATE_BOUND
        for value in coordinates
    ):
        return False, "coordinate outside permitted bounds", None
    with localcontext() as context:
        context.prec = PRECISION_DIGITS
        points = list(zip(coordinates[::2], coordinates[1::2]))
        max_line_distance = Decimal(0)
        for (x, y), line in zip(points, lines):
            first_x, first_y, second_x, second_y = map(Decimal, line)
            normal_x, normal_y = first_y - second_y, second_x - first_x
            constant = first_x * second_y - second_x * first_y
            distance = (
                abs(normal_x * x + normal_y * y + constant)
                / (normal_x * normal_x + normal_y * normal_y).sqrt()
            )
            max_line_distance = max(max_line_distance, distance)
            if distance > TOLERANCE:
                return False, "point is too far from its assigned line", None
        distances = []
        for first in range(LINE_COUNT):
            for second in range(first + 1, LINE_COUNT):
                dx = points[first][0] - points[second][0]
                dy = points[first][1] - points[second][1]
                distances.append((dx * dx + dy * dy).sqrt())
        if min(distances) < TOLERANCE:
            return False, "two points are too close", None
        if max(distances) - min(distances) > TOLERANCE:
            return False, "pairwise distances differ beyond the allowed tolerance", None
        metrics = {
            "max_line_distance": str(max_line_distance),
            "min_separation": str(min(distances)),
            "side_difference": str(max(distances) - min(distances)),
            "max_coordinate": str(max(abs(value) for value in coordinates)),
        }
    return True, "valid points on the assigned lines with equal distances", metrics


if __name__ == "__main__":
    data = list(map(int, Path(sys.argv[1]).read_text().split()))
    source = [
        data[start : start + COORDINATES_PER_LINE]
        for start in range(0, len(data), COORDINATES_PER_LINE)
    ]
    accepted, reason, _ = check(source, Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
