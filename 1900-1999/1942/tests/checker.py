"""Check exact maximum count and absolute distance error by rational bounds."""

from collections import Counter
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path
import re
import sys

SCALE = 1000
EPSILON = Fraction(1, 100000)
INTEGER = re.compile(r"[+-]?[0-9]+\Z")
REAL = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?\Z")


def target(path):
    words = Path(path).read_text(encoding="utf-8").split()
    size = int(words[0])
    if len(words) != 1 + 2 * size:
        raise ValueError("invalid input size")
    groups = Counter()
    for index in range(size):
        x = Fraction(words[1 + 2 * index]) * SCALE
        y = Fraction(words[2 + 2 * index]) * SCALE
        if x.denominator != 1 or y.denominator != 1:
            raise ValueError("invalid precision")
        groups[(int(x) % SCALE, int(y) % SCALE)] += 1
    count = max(groups.values())
    norms = []
    for (x, y), frequency in groups.items():
        if frequency == count:
            dx, dy = min(x, SCALE - x), min(y, SCALE - y)
            norms.append(dx * dx + dy * dy)
    return count, Fraction(min(norms), SCALE * SCALE)


def check(input_path, actual_path):
    count, norm = target(input_path)
    words = Path(actual_path).read_text(encoding="utf-8").split()
    if len(words) != 2 or not INTEGER.fullmatch(words[0]) or int(words[0]) != count:
        return False, "wrong integer count or output shape"
    if not REAL.fullmatch(words[1]):
        return False, "invalid distance"
    value = Decimal(words[1])
    if not value.is_finite() or value < -1 or value > 1:
        return False, "distance outside tolerance"
    if norm == 0:
        return value.copy_abs() <= Decimal("0.00001"), "zero-distance tolerance"
    if value < Decimal("0.0005"):
        return False, "distance too small"
    distance = Fraction(value)
    lower = max(Fraction(0), distance - EPSILON)
    upper = distance + EPSILON
    valid = upper >= 0 and lower * lower <= norm <= upper * upper
    return valid, "OK" if valid else "absolute distance error exceeds 1e-5"


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("usage: checker.py INPUT EXPECTED ACTUAL")
        accepted, reason = check(sys.argv[1], sys.argv[3])
    except (OSError, ValueError, InvalidOperation, ZeroDivisionError):
        accepted, reason = False, "invalid input or output"
    print(reason)
    sys.exit(0 if accepted else 1)
