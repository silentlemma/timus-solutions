"""Check relative error against the exact distance, including small positive answers."""

from fractions import Fraction
from pathlib import Path
import re
import sys

TOLERANCE = Fraction("0.0001")
NUMBER = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")


def exact_answer(text):
    data = iter(map(int, text.split()))
    count = next(data)
    lines = []
    for _ in range(count):
        x1, y1, x2, y2 = next(data), next(data), next(data), next(data)
        dx, dy = x2 - x1, y2 - y1
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        lines.append((dx, dy, dy * x1 - dx * y1))
    lines.sort(key=lambda line: (line[0] == 0, Fraction(line[1], line[0]) if line[0] else 0))
    best = Fraction(0)
    dx1, dy1, c1 = lines[-1]
    for dx2, dy2, c2 in lines:
        numerator = abs(dx1 * c2 - c1 * dx2) + abs(dy1 * c2 - c1 * dy2)
        denominator = abs(dx1 * dy2 - dy1 * dx2)
        best = max(best, Fraction(numerator, denominator))
        dx1, dy1, c1 = dx2, dy2, c2
    return best


def accepts(expected, text):
    tokens = text.split()
    if len(tokens) != 1 or NUMBER.fullmatch(tokens[0]) is None:
        return False
    try:
        actual = Fraction(tokens[0])
        return abs(actual - expected) <= expected * TOLERANCE
    except (ValueError, ZeroDivisionError, OverflowError):
        return False


def main():
    try:
        expected = exact_answer(Path(sys.argv[1]).read_text(encoding="ascii"))
        actual = Path(sys.argv[3]).read_text(encoding="ascii")
        passed = accepts(expected, actual)
    except (OSError, UnicodeError, IndexError, ValueError, ZeroDivisionError):
        passed = False
    if not passed:
        print("Expected one finite number within relative error 1e-4 (exact zero for zero).")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
