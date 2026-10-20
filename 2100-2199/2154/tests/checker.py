"""Compare one finite distance with the permitted absolute or relative error."""

from decimal import Decimal, DecimalException, localcontext
from pathlib import Path
import re
import sys

TOLERANCE = Decimal("0.000001")
NUMBER = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")


def read_value(text):
    tokens = text.split()
    if len(tokens) != 1 or NUMBER.fullmatch(tokens[0]) is None:
        raise ValueError("expected one finite number")
    value = Decimal(tokens[0])
    if not value.is_finite():
        raise ValueError("expected one finite number")
    return value


def accepts(expected, actual):
    try:
        expected = read_value(expected)
        actual = read_value(actual)
        with localcontext() as context:
            context.prec = max(len(expected.as_tuple().digits), len(actual.as_tuple().digits)) + 28
            return abs(actual - expected) <= max(TOLERANCE, abs(expected) * TOLERANCE)
    except (ValueError, DecimalException):
        return False


def main():
    try:
        expected = Path(sys.argv[2]).read_text(encoding="ascii")
        actual = Path(sys.argv[3]).read_text(encoding="ascii")
        passed = accepts(expected, actual)
    except (OSError, UnicodeError, IndexError):
        passed = False
    if not passed:
        print("Expected one finite number within absolute or relative error 1e-6.")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
