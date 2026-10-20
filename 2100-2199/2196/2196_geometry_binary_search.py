import bisect
import math
import sys

SPLITTER = 134217729.0
CLOSE_DISTANCE = 1e-5
MAX_DISTANCE = 3e9
PI = (math.pi, 1.2246467991473532e-16)


def precise_integer(value):
    high = float(value)
    return high, float(value - int(high))


def add(first, second):
    high = first[0] + second[0]
    part = high - first[0]
    low = (first[0] - (high - part)) + (second[0] - part)
    low += first[1] + second[1]
    result = high + low
    return result, low - (result - high)


def subtract(first, second):
    return add(first, (-second[0], -second[1]))


def multiply(first, second):
    high = first[0] * second[0]
    split = SPLITTER * first[0]
    first_high = split - (split - first[0])
    first_low = first[0] - first_high
    split = SPLITTER * second[0]
    second_high = split - (split - second[0])
    second_low = second[0] - second_high
    low = (first_high * second_high - high) + first_high * second_low
    low += first_low * second_high + first_low * second_low
    low += first[0] * second[1] + first[1] * second[0]
    result = high + low
    return result, low - (result - high)


def nonnegative(value):
    return value[0] > 0 or (value[0] == 0 and value[1] >= 0)


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(data)
    vertices = [(next(data), next(data)) for _ in range(count)]
    polygon = []
    for index, point in enumerate(vertices):
        before = vertices[index - 1]
        after = vertices[(index + 1) % count]
        turn = (point[0] - before[0]) * (after[1] - point[1])
        turn -= (point[1] - before[1]) * (after[0] - point[0])
        if turn:
            polygon.append(point)
    del vertices
    count = len(polygon)
    x = [point[0] for point in polygon]
    y = [point[1] for point in polygon]
    x.append(x[0])
    y.append(y[0])
    dx = [x[index + 1] - x[index] for index in range(count)]
    dy = [y[index + 1] - y[index] for index in range(count)]
    length_squared = [dx[index] ** 2 + dy[index] ** 2 for index in range(count)]
    rx = [value - x[0] for value in x]
    ry = [value - y[0] for value in y]
    area_twice = sum(
        rx[index] * ry[index + 1] - ry[index] * rx[index + 1] for index in range(1, count - 1)
    )
    perimeter = math.fsum(math.hypot(dx[index], dy[index]) for index in range(count))
    perimeter_squared = multiply((perimeter, 0.0), (perimeter, 0.0))
    precise_area = multiply(precise_integer(area_twice), (1 / 2, 0.0))
    area = area_twice / 2
    half_perimeter = perimeter / 2
    radii = [0.0]
    extras = [(0.0, 0.0)]
    target = precise_area
    multiplier = 1
    while radii[-1] <= MAX_DISTANCE:
        target = add(target, target)
        multiplier *= 2
        extra = area * (multiplier - 1)
        root = math.sqrt(half_perimeter * half_perimeter + math.pi * extra)
        radii.append(extra / (half_perimeter + root))
        extras.append(subtract(target, precise_area))

    def infected(day, base, denominator, square):
        # Squaring removes the square root from a close threshold comparison.
        numerator = precise_integer(base)
        if square:
            numerator = multiply(numerator, numerator)
        divisor = precise_integer(denominator)
        remaining = subtract(multiply(extras[day], divisor), multiply(PI, numerator))
        if not nonnegative(remaining):
            return False
        left = multiply(multiply(perimeter_squared, numerator), divisor)
        return nonnegative(subtract(multiply(remaining, remaining), left))

    answers = []
    for _ in range(next(data)):
        qx, qy = next(data), next(data)
        first_visible = dx[0] * (qy - y[0]) - dy[0] * (qx - x[0]) < 0
        last_visible = dx[-1] * (qy - y[count - 1]) - dy[-1] * (qx - x[count - 1]) < 0
        if first_visible != last_visible:
            visible, hidden = (0, count - 1) if first_visible else (count - 1, 0)
        else:
            px, py = qx - x[0], qy - y[0]
            low, high = 1, count - 1
            if first_visible:
                while high - low > 1:
                    middle = (low + high) // 2
                    if rx[middle] * py - ry[middle] * px <= 0:
                        low = middle
                    else:
                        high = middle
                visible, hidden = 0, low
            else:
                while high - low > 1:
                    middle = (low + high) // 2
                    if rx[middle] * py - ry[middle] * px >= 0:
                        low = middle
                    else:
                        high = middle
                visible, hidden = low, 0
                side = dx[visible] * (qy - y[visible]) - dy[visible] * (qx - x[visible])
                if side >= 0:
                    answers.append("0")
                    continue

        projection = (qx - x[visible]) * dx[visible] + (qy - y[visible]) * dy[visible]
        edge = visible
        if projection < 0 or projection > length_squared[visible]:
            forward = projection > 0
            start, end = (visible, hidden) if forward else (hidden, visible)
            low, high = 0, (end - start) % count
            # A visible convex chain has only one minimum of the distance.
            while high - low > 1:
                middle = (low + high) // 2
                edge = (start + middle) % count
                side = dx[edge] * (qy - y[edge]) - dy[edge] * (qx - x[edge])
                if side >= 0:
                    found = forward
                else:
                    derivative = (x[edge + 1] - qx) * dx[edge]
                    derivative += (y[edge + 1] - qy) * dy[edge]
                    found = derivative >= 0
                if found:
                    high = middle
                else:
                    low = middle
            edge = (start + high) % count

        px, py = qx - x[edge], qy - y[edge]
        projection = px * dx[edge] + py * dy[edge]
        denominator = 1
        square = False
        if projection <= 0:
            base = px * px + py * py
            distance = math.hypot(px, py)
        elif projection >= length_squared[edge]:
            px, py = qx - x[edge + 1], qy - y[edge + 1]
            base = px * px + py * py
            distance = math.hypot(px, py)
        else:
            base = abs(dx[edge] * py - dy[edge] * px)
            denominator = length_squared[edge]
            square = True
            distance = base / math.sqrt(denominator)
        day = bisect.bisect_left(radii, distance)
        if abs(distance - radii[day]) <= CLOSE_DISTANCE:
            if not infected(day, base, denominator, square):
                day += 1
        elif day > 1 and abs(distance - radii[day - 1]) <= CLOSE_DISTANCE:
            if infected(day - 1, base, denominator, square):
                day -= 1
        answers.append(str(day))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
