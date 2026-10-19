import sys

DIMENSIONS = 3


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def subtract(a, b):
    return tuple(x - y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def sign(value):
    return (value > 0) - (value < 0)


def projection_sign_at_entry(
    point, edge, velocity, a, b, discriminant_sign, radius_squared
):
    x = dot(edge, point)
    y = dot(edge, velocity)
    if y == 0:
        return sign(x)
    numerator = -x if y > 0 else x
    denominator = abs(y)
    vertex_offset = a * numerator + b * denominator
    if vertex_offset >= 0:
        comparison = 0 if vertex_offset == 0 and discriminant_sign == 0 else -1
    else:
        scaled = tuple(w * y - v * x for w, v in zip(point, velocity))
        comparison = sign(dot(scaled, scaled) - radius_squared * y * y)
    return comparison if y > 0 else -comparison


def ray_hits(point, velocity, radius_squared):
    projection = dot(point, velocity)
    return projection < 0 and projection * projection >= dot(velocity, velocity) * (
        dot(point, point) - radius_squared
    )


def classify(center, radius, first, second, velocity):
    left = subtract(first, center)
    right = subtract(second, center)
    edge = subtract(right, left)
    normal = cross(edge, velocity)
    offset = cross(edge, left)
    radius_squared = radius * radius
    a = dot(normal, normal)
    b = dot(offset, normal)
    c = dot(offset, offset) - radius_squared * dot(edge, edge)
    if a and c > 0 and b < 0:
        height = dot(left, normal)
        discriminant_sign = radius_squared * a - height * height
        if discriminant_sign >= 0:
            left_sign = projection_sign_at_entry(
                left, edge, velocity, a, b, discriminant_sign, radius_squared
            )
            right_sign = projection_sign_at_entry(
                right, edge, velocity, a, b, discriminant_sign, radius_squared
            )
            if left_sign < 0 < right_sign:
                return "Warning"
    if ray_hits(left, velocity, radius_squared) or ray_hits(
        right, velocity, radius_squared
    ):
        return "Crash"
    return "False alarm"


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))

    def vector():
        return tuple(next(tokens) for _ in range(DIMENSIONS))

    center = vector()
    radius = next(tokens)
    first = vector()
    second = vector()
    velocity = vector()
    print(classify(center, radius, first, second, velocity))


if __name__ == "__main__":
    main()
