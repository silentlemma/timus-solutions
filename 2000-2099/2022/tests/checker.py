"""Exact rational feasibility and high-precision physical trajectory checks."""

from decimal import Decimal, localcontext
from fractions import Fraction

EPS = Decimal("0.000001")


def intervals(data, precision=80):
    with localcontext() as ctx:
        ctx.prec = precision
        L, h, width, diameter, vx, vy, ux, uy = map(int, data)
        gravity, half = Decimal(10), Decimal(5)
        ratio = Fraction(vx, ux)
        lo, hi = Decimal(0), min(Decimal(vy) / half, Decimal(L) / vx)

        def decimal(value):
            return Decimal(value.numerator) / value.denominator

        def bounds(a, b, c):
            delta = b * b - 4 * a * c
            if delta < 0:
                return None
            if delta == 0:
                root = decimal(-b / (2 * a))
                return root, root
            if c == 0:
                result = (Decimal(0), decimal(-b / a))
                return min(result), max(result)
            root = decimal(delta).sqrt()
            aa, bb = decimal(a), decimal(b)
            result = ((-bb - root) / (2 * aa), (-bb + root) / (2 * aa))
            return min(result), max(result)

        def at_face(x, level):
            delay = Fraction(x, ux)
            return (
                -5 * (1 + ratio * ratio),
                vy - ratio * uy + 10 * ratio * delay,
                uy * delay - 5 * delay * delay - level,
            )

        for x in (L, L + width):
            pair = bounds(*at_face(x, h))
            if pair is None:
                return []
            lo, hi = max(lo, pair[0]), min(hi, pair[1])
            if lo >= hi:
                return []
        lower = (L - Decimal(ux * uy) / gravity) / vx
        upper = (L + width - Decimal(ux * uy) / gravity) / vx
        ceiling = h + diameter
        bad = []
        for left, right, coefficients in (
            (lo, min(hi, lower), at_face(L, ceiling)),
            (
                max(lo, lower),
                min(hi, upper),
                (Fraction(-5), Fraction(vy), Fraction(uy * uy, 20) - ceiling),
            ),
            (max(lo, upper), hi, at_face(L + width, ceiling)),
        ):
            if left > right:
                continue
            pair = bounds(*coefficients)
            if pair is not None:
                a, b = max(left, pair[0]), min(right, pair[1])
                if a <= b:
                    bad.append((a, b))
        if not bad:
            return [(+lo, +hi)]
        first, last = min(a for a, _ in bad), max(b for _, b in bad)
        return [(+a, +b) for a, b in ((lo, first), (last, hi)) if a < b]


def valid_window(data, answer, precision=80):
    """Extrema of physical height over the entire (throw-time, wall-position) rectangle."""
    with localcontext() as ctx:
        ctx.prec = precision
        L, h, width, diameter, vx, vy, ux, uy = map(Decimal, data)
        t = answer if isinstance(answer, Decimal) else Decimal(str(answer))
        a, b = t - EPS, t + EPS
        end = min(vy / Decimal(5), L / vx)
        if not 0 < a < b < end:
            return False, {"reason": "throw window outside airborne/before-wall domain"}
        right = L + width
        gravity = Decimal(10)

        def y(time, x):
            frog = vy * time - gravity * time * time / 2
            delay = (x - vx * time) / ux
            return frog + uy * delay - gravity * delay * delay / 2

        corners = [(time, x) for time in (a, b) for x in (L, right)]
        minimum = min(y(time, x) for time, x in corners)
        candidates = list(corners)
        for time in (a, b):
            apex = vx * time + ux * uy / gravity
            candidates.append((time, min(right, max(L, apex))))
        k = vx / ux
        for x in (L, right):
            optimum = (vy - k * uy + gravity * k * x / ux) / (gravity * (1 + k * k))
            candidates.append((min(b, max(a, optimum)), x))
        time = vy / gravity
        x = vx * time + ux * uy / gravity
        if a <= time <= b and L <= x <= right:
            candidates.append((time, x))
        maximum = max(y(time, x) for time, x in candidates)
        valid = minimum > h and maximum < h + diameter
        return valid, {
            "minimum_floor_clearance": str(minimum - h),
            "minimum_ceiling_clearance": str(h + diameter - maximum),
        }


from decimal import DecimalException
from pathlib import Path
import re
import sys

INPUT_FIELDS = 8
MAX_VALUE = 1000
PRECISION = 120
NUMBER = re.compile(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?")


def read_case(text):
    data = list(map(int, text.split()))
    if len(data) != INPUT_FIELDS or any(not 1 <= value <= MAX_VALUE for value in data):
        raise ValueError("bad input")
    return data


def validate(text, data):
    try:
        tokens = text.split()
        if len(tokens) != 1 or NUMBER.fullmatch(tokens[0]) is None:
            return False
        answer = Decimal(tokens[0])
        if not answer.is_finite():
            return False
        with localcontext() as ctx:
            ctx.prec = PRECISION
            if answer == -1:
                return not any(hi - lo > 2 * EPS for lo, hi in intervals(data, PRECISION))
            return valid_window(data, answer, PRECISION)[0]
    except (DecimalException, ValueError, OverflowError):
        return False


if __name__ == "__main__":
    try:
        data = read_case(Path(sys.argv[1]).read_text())
        passed = validate(Path(sys.argv[3]).read_text(), data)
    except (OSError, ValueError, IndexError, DecimalException):
        passed = False
    if not passed:
        print("Expected any robustly wall-clear launch time, or -1 only if no such time exists.")
    raise SystemExit(0 if passed else 1)
