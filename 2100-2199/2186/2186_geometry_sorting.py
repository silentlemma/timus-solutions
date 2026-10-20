import bisect
import functools
import math
import sys

SCALE = 100000
HEADER_FIELDS = 3
ANGLE_EPS = 1e-12
GRID_EPS = 1e-7
DIGITS = 10
HALF_TURN = 180
FULL_TURN = 2 * math.pi


def direction_order(left, right):
    cross = left[1] * right[2] - left[2] * right[1]
    return -1 if cross > 0 else int(cross < 0)


def fits(left, right, distance, cosine):
    _, x, y = left
    _, u, v = right
    cross = x * v - y * u
    dot = x * u + y * v
    if cross < 0:
        return False
    if cross == 0:
        return dot > 0
    if dot >= 0 > cosine:
        return True
    if cosine >= 0 > dot:
        return False
    lhs = dot * dot * distance * distance
    rhs = cosine * cosine * (x * x + y * y) * (u * u + v * v)
    return lhs >= rhs if dot >= 0 else lhs <= rhs


def main():
    data = sys.stdin.buffer.read().split()
    n, shots, queries = map(int, data[:HEADER_FIELDS])
    offset = HEADER_FIELDS
    guns = []
    for _ in range(n):
        x, y = int(data[offset]), int(data[offset + 1])
        offset += 2
        guns.append((math.atan2(y, x), x, y))
    a, b, radius = map(int, data[offset : offset + HEADER_FIELDS])
    offset += HEADER_FIELDS
    distance = a * a + b * b
    radius_squared = radius * radius
    cosine = distance - 2 * radius_squared
    half_width = math.atan2(radius, math.sqrt(distance - radius_squared))
    width = 2 * half_width
    lower = math.atan2(b, a) - half_width
    guns.sort(key=lambda gun: gun[0])
    begin = 0
    while begin < n:
        end = begin + 1
        while end < n and guns[end][0] == guns[begin][0]:
            end += 1
        if end - begin > 1:
            guns[begin:end] = sorted(guns[begin:end], key=functools.cmp_to_key(direction_order))
        begin = end

    initial = 0
    for _, x, y in guns:
        cross = a * y - b * x
        if a * x + b * y >= 0 and cross * cross <= radius_squared * (x * x + y * y):
            initial += 1
    best = [math.inf] * (n + 1)
    best[0] = best[initial] = 0.0
    end = 0
    for begin, gun in enumerate(guns):
        if end < begin:
            end = begin
        while end < begin + n:
            other = guns[end % n]
            delta = other[0] - gun[0] + (FULL_TURN if end >= n else 0.0)
            if abs(delta - width) <= ANGLE_EPS:
                inside = fits(gun, other, distance, cosine)
            else:
                inside = delta < width
            if not inside:
                break
            end += 1
        angle = (lower - gun[0]) % FULL_TURN
        if angle <= ANGLE_EPS or FULL_TURN - angle <= ANGLE_EPS:
            # The exact side of the tangent distinguishes zero from a full turn.
            _, x, y = gun
            cross = a * y - b * x
            strict = cross * cross < radius_squared * (x * x + y * y)
            angle = FULL_TURN - ANGLE_EPS if strict else 0.0
        count = end - begin
        if angle < best[count]:
            best[count] = angle
    for count in range(n - 1, -1, -1):
        best[count] = min(best[count], best[count + 1])

    levels = [0] * (n + 1)
    denominator = n**shots
    for count in range(1, n):
        if shots == 1:
            levels[count] = SCALE * count // n
            continue
        remaining = n - count
        value = SCALE * (1.0 - (remaining / n) ** shots)
        nearest = int(value + 1 / 2)
        if abs(value - nearest) < GRID_EPS:
            # Exact arithmetic decides which side of a query boundary this lies on.
            enough = SCALE * remaining**shots <= (SCALE - nearest) * denominator
            level = nearest if enough else nearest - 1
        else:
            level = int(value)
        levels[count] = min(level, SCALE - 1)
    levels[n] = SCALE

    answers = {}
    output = []
    for word in data[offset : offset + queries]:
        parts = word.split(b".")
        probability = int(parts[0]) * SCALE
        if len(parts) > 1:
            probability += int(parts[1].ljust(len(str(SCALE)) - 1, b"0"))
        count = bisect.bisect_left(levels, probability)
        if count not in answers:
            angle = best[count]
            answers[count] = (
                "-1" if math.isinf(angle) else f"{angle * HALF_TURN / math.pi:.{DIGITS}f}"
            )
        output.append(answers[count])
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
