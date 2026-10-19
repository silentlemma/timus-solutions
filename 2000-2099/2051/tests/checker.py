"""Check both continuous envelopes and exact areas, accepting any reconstruction."""

from pathlib import Path
import re
import sys

MAX_TIME = 1000000
MAX_HEIGHT = 1000000
MAX_INPUT_KNOTS = 100000
MAX_CONTACTS = 30
MAX_OUTPUT_KNOTS = 2 * MAX_INPUT_KNOTS + MAX_CONTACTS


def read_curve(fields):
    count = next(fields)
    if not 2 <= count <= MAX_OUTPUT_KNOTS:
        raise ValueError("Invalid knot count")
    return [(next(fields), next(fields)) for _ in range(count)]


def shape(curve, duration):
    if curve[0][0] != 0 or curve[-1][0] != duration:
        return False
    if any(not 0 <= y <= MAX_HEIGHT for _, y in curve):
        return False
    for i in range(len(curve) - 1):
        if curve[i][0] >= curve[i + 1][0]:
            return False
    for (a, x), (b, y), (c, z) in zip(curve, curve[1:], curve[2:]):
        if (y - x) * (c - b) == (z - y) * (b - a):
            return False
    return True


def equal(a, b):
    return a[0] * b[1] == b[0] * a[1]


def pair_sum(a, b):
    return a[0] * b[1] + b[0] * a[1], a[1] * b[1]


def envelope(values):
    upper, lower, first, second = values
    if first[0] * second[1] < second[0] * first[1]:
        first, second = second, first
    return equal(first, upper) and equal(second, lower)


def validate(duration, upper, lower, raw):
    try:
        tokens = raw.decode("ascii").split()
        if any(re.fullmatch(r"[+-]?[0-9]+", word) is None for word in tokens):
            return False
        fields = iter(map(int, tokens))
        first, second = read_curve(fields), read_curve(fields)
        if next(fields, None) is not None:
            return False
    except (ValueError, StopIteration, UnicodeDecodeError):
        return False
    if not shape(first, duration) or not shape(second, duration):
        return False
    areas = [
        sum((a[1] + b[1]) * (b[0] - a[0]) for a, b in zip(curve, curve[1:]))
        for curve in (first, second)
    ]
    if areas[0] != areas[1]:
        return False
    curves = [upper, lower, first, second]
    times = sorted({t for curve in curves for t, _ in curve})
    indices = [0] * len(curves)
    previous = None
    for time in times:
        values = []
        for index, curve in enumerate(curves):
            edge = indices[index]
            while edge + 2 < len(curve) and curve[edge + 1][0] <= time:
                edge += 1
            indices[index] = edge
            a, x = curve[edge]
            b, y = curve[edge + 1]
            values.append((x * (b - time) + y * (time - a), b - a))
        if not envelope(values):
            return False
        if previous is not None and not envelope(
            [pair_sum(a, b) for a, b in zip(previous, values)]
        ):
            return False
        previous = values
    return True


def main():
    fields = iter(map(int, Path(sys.argv[1]).read_text(encoding="ascii").split()))
    duration = next(fields)
    upper, lower = read_curve(fields), read_curve(fields)
    if not validate(duration, upper, lower, Path(sys.argv[3]).read_bytes()):
        print("Invalid knots, envelope, continuity or exact area balance")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
