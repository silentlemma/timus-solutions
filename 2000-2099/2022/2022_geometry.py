import math
import sys

G = 10
HALF_G = G // 2
QUADRATIC_FACTOR = 4
MARGIN = 1e-6
INPUT_FIELDS = 8


def roots(a, b, c):
    """Roots of -a*t*t+b*t+c; the discriminant is evaluated as an exact integer."""
    discriminant = b * b + QUADRATIC_FACTOR * a * c
    if discriminant < 0:
        return None
    if discriminant == 0:
        value = b / (2 * a)
        return value, value
    radical = math.sqrt(discriminant)
    q = (b + math.copysign(radical, b)) / 2
    if q == 0:
        return 0.0, 0.0
    x, y = q / a, -c / q
    return min(x, y), max(x, y)


def feasible_intervals(data):
    distance, height, thickness, diameter, vx, vy, ux, uy = data
    lo, hi = 0.0, min(2 * vy / G, distance / vx)

    def face(x, level):
        return (
            HALF_G * (ux * ux + vx * vx),
            vy * ux * ux - uy * vx * ux + G * x * vx,
            uy * x * ux - HALF_G * x * x - level * ux * ux,
        )

    for x in (distance, distance + thickness):
        pair = roots(*face(x, height))
        if pair is None:
            return []
        lo, hi = max(lo, pair[0]), min(hi, pair[1])
        if lo >= hi:
            return []
    ceiling = height + diameter
    before = (G * distance - ux * uy) / (G * vx)
    after = (G * (distance + thickness) - ux * uy) / (G * vx)
    pieces = [
        (lo, min(hi, before), face(distance, ceiling)),
        (max(lo, before), min(hi, after), (G * G, 2 * G * vy, uy * uy - 2 * G * ceiling)),
        (max(lo, after), hi, face(distance + thickness, ceiling)),
    ]
    bad = []
    for left, right, polynomial in pieces:
        if left > right:
            continue
        pair = roots(*polynomial)
        if pair is None:
            continue
        a, b = max(left, pair[0]), min(right, pair[1])
        if a <= b:
            bad.append((a, b))
    if not bad:
        return [(lo, hi)]
    # The maximum height is concave in throw time, so its ceiling-superlevel set is one interval.
    bad_lo, bad_hi = min(a for a, _ in bad), max(b for _, b in bad)
    return [(a, b) for a, b in ((lo, bad_lo), (bad_hi, hi)) if a < b]


def solve(data):
    intervals = feasible_intervals(data)
    if not intervals:
        return None
    lo, hi = max(intervals, key=lambda pair: pair[1] - pair[0])
    if hi - lo <= 2 * MARGIN:
        return None
    return (lo + hi) / 2


def run(tokens):
    data = [next(tokens) for _ in range(INPUT_FIELDS)]
    answer = solve(data)
    return "-1\n" if answer is None else str(answer) + "\n"


if __name__ == "__main__":
    sys.stdout.write(run(iter(map(int, sys.stdin.buffer.read().split()))))
