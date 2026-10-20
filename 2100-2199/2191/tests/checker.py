"""Check the expression at every input vertex and every absolute-value root.

All decimal coefficients share an exact integer scale, so large cancelling
terms cannot conceal an error through floating-point rounding. Values must
match within 10^-6.
"""

from fractions import Fraction
import re
import sys

OUTPUT_LIMIT = 8 * 1024 * 1024
TOLERANCE_DENOMINATOR = 10**6
MAX_DECIMAL_SPAN = 10000
MAX_EXPONENT_DIGITS = 1000
SCALING_BUDGET = 8 * OUTPUT_LIMIT
NUMBER = rb"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
TERM = re.compile(rb"([+-]?)\|([+-]?" + NUMBER + rb")x([+-])(" + NUMBER + rb")\|")


class Bad(Exception):
    pass


def decimal(token):
    text = token.decode("ascii").lower()
    mantissa, separator, exponent = text.partition("e")
    if len(exponent.lstrip("+-").lstrip("0")) > MAX_EXPONENT_DIGITS:
        raise Bad("decimal exponent exceeds the checker's resource limit")
    power = int(exponent) if separator else 0
    sign = -1 if mantissa.startswith("-") else 1
    mantissa = mantissa.lstrip("+-")
    whole, separator, fraction = mantissa.partition(".")
    digits = (whole + fraction).lstrip("0")
    if not digits:
        return 0, 0
    power -= len(fraction)
    trimmed = digits.rstrip("0")
    power += len(digits) - len(trimmed)
    return sign * int(trimmed), power


def read_terms(path, count):
    with open(path, "rb") as stream:
        raw = stream.read(OUTPUT_LIMIT + 1)
    if len(raw) > OUTPUT_LIMIT:
        raise Bad("output exceeds eight megabytes")
    text = raw.strip().replace(b" ", b"").replace(b"\t", b"")
    position = 0
    terms = {}
    for index in range(count):
        match = TERM.match(text, position)
        if match is None:
            raise Bad("term %d has invalid syntax" % (index + 1))
        outer, left, inner, right = match.groups()
        if index == 0 and outer == b"+":
            raise Bad("the first term cannot have a leading plus")
        if index and not outer:
            raise Bad("a sign is required between terms")
        sign = -1 if outer == b"-" else 1
        a, ae = decimal(left)
        b, be = decimal(right)
        if inner == b"-":
            b = -b
        if a < 0 or (a == 0 and b < 0):
            a, b = -a, -b
        if a or b:
            key = a, ae, b, be
            terms[key] = terms.get(key, 0) + sign
        position = match.end()
    if position != len(text):
        raise Bad("expected exactly %d terms on one line" % count)
    return [(key, sign) for key, sign in terms.items() if sign]


def scaled_terms(terms):
    low = 0
    high = 0
    for (a, ae, b, be), _ in terms:
        if a:
            low, high = min(low, ae), max(high, ae)
        if b:
            low, high = min(low, be), max(high, be)
    if high - low > MAX_DECIMAL_SPAN:
        raise Bad("decimal exponent span exceeds the checker's resource limit")
    work = sum((ae - low if a else 0) + (be - low if b else 0) for (a, ae, b, be), _ in terms)
    if work > SCALING_BUDGET:
        raise Bad("exact decimal expansion exceeds the checker's resource limit")
    scale = 10**-low
    result = []
    for (a, ae, b, be), sign in terms:
        a = a * 10 ** (ae - low) if a else 0
        b = b * 10 ** (be - low) if b else 0
        result.append((sign, a, b))
    return scale, result


def check(source, expected, output):
    with open(source) as stream:
        data = list(map(int, stream.read().split()))
    count = data[0]
    points = list(zip(data[1::2], data[2::2]))
    scale, terms = scaled_terms(read_terms(output, count))
    first, last = points[0][0], points[-1][0]
    slope = 0
    intercept = 0
    events = []
    for sign, a, b in terms:
        direction = -1 if a * first + b < 0 else 1
        slope += sign * direction * a
        intercept += sign * direction * b
        if a and a * first + b < 0 < a * last + b:
            events.append((Fraction(-b, a), 2 * sign * a, 2 * sign * b))
    events.sort(key=lambda event: event[0])
    index = 0
    if abs(slope * first + intercept - points[0][1] * scale) * TOLERANCE_DENOMINATOR > scale:
        raise Bad("the function differs at the first vertex")
    for vertex, ((left, low), (right, high)) in enumerate(zip(points, points[1:]), 2):
        width = right - left
        rise = high - low
        while index < len(events) and events[index][0] <= right:
            root, change_slope, change_intercept = events[index]
            numerator, denominator = root.numerator, root.denominator
            actual = (slope * numerator + intercept * denominator) * width
            wanted = low * width * denominator + rise * (numerator - left * denominator)
            error = abs(actual - wanted * scale) * TOLERANCE_DENOMINATOR
            if error > denominator * width * scale:
                raise Bad("the function differs at an absolute-value root")
            slope += change_slope
            intercept += change_intercept
            index += 1
        error = abs(slope * right + intercept - high * scale) * TOLERANCE_DENOMINATOR
        if error > scale:
            raise Bad("the function differs at vertex %d" % vertex)


def main():
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    try:
        check(*sys.argv[1:])
    except (Bad, ValueError, OverflowError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
