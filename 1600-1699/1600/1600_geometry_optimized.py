import math
import sys


BASE = 10
X_VELOCITY = 3


def decimal_parts(token):
    mantissa, separator, exponent = token.lower().partition(b"e")
    integer, _, fractional = mantissa.partition(b".")
    fractional = fractional.rstrip(b"0")
    digits = integer + fractional
    if digits in (b"", b"+", b"-") or not (value := int(digits)):
        return 0, 0
    return value, (int(exponent) if separator else 0) - len(fractional)


def read_objects():
    reader = sys.stdin.buffer
    count, distance = reader.readline().split()
    parts = [decimal_parts(distance)]
    for _ in range(int(count)):
        parts.extend(map(decimal_parts, reader.readline().split()))
    smallest_scale = min(exponent for _, exponent in parts)
    exponents = {exponent for _, exponent in parts}
    powers = {exponent: BASE ** (exponent - smallest_scale) for exponent in exponents}
    values = (number * powers[exponent] for number, exponent in parts)
    radius = next(values)
    return radius, list(zip(values, values, values, values, values, values, strict=True))


def main():
    radius, objects = read_objects()
    radius_squared = radius * radius
    best = math.inf
    pair = None
    if not objects:
        print("OK")
        return
    ordered = sorted(
        (x, y, z, u, v, w, number) for number, (x, y, z, u, v, w) in enumerate(objects, 1)
    )
    slowest = min(row[X_VELOCITY] for row in ordered)
    # Once a collision is found, limit the sweep by its certified time bound.
    deadline = None
    for i, (x, y, z, u, v, w, number) in enumerate(ordered):
        extent = x + radius + deadline * (u - slowest) if deadline is not None else math.inf
        for xx, yy, zz, uu, vv, ww, other in ordered[i + 1 :]:
            if xx > extent:
                break
            px, vx = xx - x, uu - u
            # A pair already too far apart on x cannot meet while moving farther apart.
            if px > radius and vx >= 0:
                continue
            vy, vz = vv - v, ww - w
            if not (vx or vy or vz):
                continue
            py, pz = yy - y, zz - z
            projection = px * vx + py * vy + pz * vz
            if projection >= 0:
                continue
            offset = px * px + py * py + pz * pz - radius_squared
            speed = vx * vx + vy * vy + vz * vz
            approach = -projection
            square = approach * approach
            discriminant = square - speed * offset
            if discriminant >= 0:
                # This form of the smaller root avoids cancellation.
                time = (offset / approach) / (1 + math.sqrt(discriminant / square))
                if time < best:
                    best, pair = time, (min(number, other), max(number, other))
                    bound = math.ceil(time)
                    # At or beyond closest approach, or already inside the sphere.
                    if (
                        bound * speed >= approach
                        or (bound * speed - 2 * approach) * bound + offset <= 0
                    ):
                        deadline = min(deadline, bound) if deadline is not None else bound
                    elif deadline is None:
                        deadline = (approach + speed - 1) // speed
                    if deadline is not None:
                        extent = x + radius + deadline * (u - slowest)

    if pair is None:
        print("OK")
    else:
        print(f"ALARM!\n{best:.3f} {pair[0]} {pair[1]}")


if __name__ == "__main__":
    main()
