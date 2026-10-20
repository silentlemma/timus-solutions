import sys
from functools import cmp_to_key

DECIMAL_PLACES = 6
DECIMAL_SCALE = 10**DECIMAL_PLACES


def compare_directions(first, second):
    cross = first[1] * second[0] - second[1] * first[0]
    return (cross > 0) - (cross < 0)


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(data)
    lines = []
    for _ in range(count):
        x1, y1, x2, y2 = next(data), next(data), next(data), next(data)
        dx, dy = x2 - x1, y2 - y1
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        lines.append((dx, dy, dy * x1 - dx * y1))

    lines.sort(key=cmp_to_key(compare_directions))
    best_numerator, best_denominator = 0, 1
    dx1, dy1, c1 = lines[-1]
    # Every directional extreme occurs between cyclic neighboring directions.
    for dx2, dy2, c2 in lines:
        denominator = abs(dx1 * dy2 - dy1 * dx2)
        numerator = abs(dx1 * c2 - c1 * dx2) + abs(dy1 * c2 - c1 * dy2)
        if numerator * best_denominator > best_numerator * denominator:
            best_numerator, best_denominator = numerator, denominator
        dx1, dy1, c1 = dx2, dy2, c2

    rounded = (best_numerator * DECIMAL_SCALE + best_denominator // 2) // best_denominator
    integer, fraction = divmod(rounded, DECIMAL_SCALE)
    if fraction:
        digits = str(fraction).zfill(DECIMAL_PLACES).rstrip("0")
        print(f"{integer}.{digits}")
    else:
        print(integer)


if __name__ == "__main__":
    main()
