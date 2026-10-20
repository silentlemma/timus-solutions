import math
import sys

SCALE = 1000
AREA_SCALE = SCALE * SCALE
OUTPUT_DIGITS = 6
FULL_TURN = 360000
HALF_TURN = FULL_TURN // 2
QUARTER_TURN = HALF_TURN // 2
OCTANT = QUARTER_TURN // 2
PI = 3.141592653589793
ANGLE_EPSILON = 1e-11
SIN_COEFFICIENTS = (
    2.8114572543455206e-15,
    -7.647163731819816e-13,
    1.6059043836821613e-10,
    -2.505210838544172e-8,
    2.7557319223985893e-6,
    -0.0001984126984126984,
    0.008333333333333333,
    -0.16666666666666666,
    1.0,
)
COS_COEFFICIENTS = (
    -1.5619206968586225e-16,
    4.779477332387385e-14,
    -1.1470745597729725e-11,
    2.08767569878681e-9,
    -2.755731922398589e-7,
    2.48015873015873e-5,
    -0.001388888888888889,
    0.041666666666666664,
    -0.5,
    1.0,
)


def fixed(token):
    return int(token.replace(b".", b""))


def sine_cosine(angle):
    angle %= FULL_TURN
    quadrant, reduced = divmod(angle, QUARTER_TURN)
    mirror = reduced > OCTANT
    if mirror:
        reduced = QUARTER_TURN - reduced
    x = reduced * (PI / HALF_TURN)
    squared = x * x
    sine = 0.0
    cosine = 0.0
    # The same polynomial and operation order keep every language's output identical.
    for coefficient in SIN_COEFFICIENTS:
        sine = sine * squared + coefficient
    for coefficient in COS_COEFFICIENTS:
        cosine = cosine * squared + coefficient
    sine = x * sine
    if reduced == OCTANT:
        sine = cosine
    if mirror:
        sine, cosine = cosine, sine
    if quadrant == 0:
        return sine, cosine
    if quadrant == 1:
        return cosine, -sine
    if quadrant == 2:
        return -sine, -cosine
    return -cosine, sine


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    points = [(fixed(next(tokens)), fixed(next(tokens))) for _ in range(n)]
    hole_x, hole_y = fixed(next(tokens)), fixed(next(tokens))
    points = [(x - hole_x, y - hole_y) for x, y in points]
    start = 0
    for i, (x, y) in enumerate(points):
        nx, ny = points[(i + 1) % n]
        if x * ny - y * nx == 0 and x * nx + y * ny < 0:
            start = (i + 1) % n
            break
    points = points[start:] + points[:start]
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    prefix = [0] * n
    for i in range(n - 1):
        prefix[i + 1] = prefix[i] + xs[i] * ys[i + 1] - ys[i] * xs[i + 1]
    total = prefix[-1]

    def capacity(angle):
        sine, cosine = sine_cosine(angle)
        first = xs[0] * sine + ys[0] * cosine
        if first == 0:
            return float(total) if xs[0] * cosine - ys[0] * sine < 0 else 0.0
        below = first < 0
        low, high = 0, n - 1
        while high - low > 1:
            middle = (low + high) // 2
            height = xs[middle] * sine + ys[middle] * cosine
            if (height < 0) == below:
                low = middle
            else:
                high = middle
        left = xs[low] * sine + ys[low] * cosine
        right = xs[high] * sine + ys[high] * cosine
        fraction = max(0.0, min(1.0, left / (left - right)))
        triangle = prefix[high] - prefix[low]
        if below:
            return float(prefix[low]) + fraction * float(triangle)
        return float(total - prefix[high]) + (1.0 - fraction) * float(triangle)

    empty = ys[0] == 0 and xs[0] > 0
    zero = -math.atan2(ys[0], xs[0]) * (HALF_TURN / PI)
    lower, upper = (zero - FULL_TURN, zero) if zero > 0 else (zero, zero + FULL_TURN)
    remaining = 0.0 if empty else capacity(0)
    angle = 0
    output = []

    def record():
        units = int(remaining / 2 + 1 / 2)
        output.append(f"{units // AREA_SCALE}.{units % AREA_SCALE:0{OUTPUT_DIGITS}d}000")

    record()
    queries = int(next(tokens))
    for _ in range(queries):
        angle += fixed(next(tokens))
        if not empty:
            # Crossing either boundary empties the polygon during the slow rotation.
            if angle <= lower + ANGLE_EPSILON or angle >= upper - ANGLE_EPSILON:
                empty = True
                remaining = 0.0
            else:
                remaining = min(remaining, capacity(angle))
        record()
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
