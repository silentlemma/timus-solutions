import math

DIMENSIONS = 3
CIRCLES = 3
PERIOD_SHIFTS = 2
TAU = 2 * math.pi


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, value):
    return tuple(x * value for x in a)


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def unit(a):
    length = math.sqrt(dot(a, a))
    return scale(a, 1 / length), length


def above_length(center, radius, first, tangent, angle, threshold):
    amplitude = radius * math.hypot(first[2], tangent[2])
    if amplitude == 0:
        return radius * angle if center[2] >= threshold else 0.0
    ratio = (threshold - center[2]) / amplitude
    if ratio <= -1:
        return radius * angle
    if ratio >= 1:
        return 0.0
    half_width = math.acos(ratio)
    phase = math.atan2(tangent[2], first[2])
    measure = 0.0
    for shift in range(-PERIOD_SHIFTS, PERIOD_SHIFTS + 1):
        left = phase - half_width + shift * TAU
        right = phase + half_width + shift * TAU
        measure += max(0.0, min(angle, right) - max(0.0, left))
    return radius * measure


def trajectory(centers):
    radial_start = tuple(-coordinate for coordinate in centers[0])
    radius_squared = dot(radial_start, radial_start)
    first, radius = unit(radial_start)
    # Preserve the exact integer normal when adjacent circles are coplanar.
    normal_raw = (-centers[0][1], centers[0][0], 0)
    tangent, _ = unit(cross(normal_raw, first))
    arcs = []
    for i, center in enumerate(centers):
        if i + 1 == len(centers):
            angle = TAU
        else:
            displacement = sub(centers[i + 1], center)
            normal, normal_length = unit(normal_raw)
            direction, cross_length = unit(cross(normal_raw, displacement))
            toward, _ = unit(cross(direction, normal))
            plane_distance = cross_length / normal_length
            normal_distance = dot(displacement, normal_raw) / normal_length
            angle = math.atan2(dot(toward, tangent), dot(toward, first))
            if angle <= 0:
                angle += TAU
            assert 0 < angle < TAU
        arcs.append((center, radius, first, tangent, angle))
        if i + 1 < len(centers):
            difference = math.fsum(
                (
                    radius_squared,
                    -dot(displacement, displacement),
                    normal_distance * normal_distance,
                )
            )
            radial_distance = difference / (radius + plane_distance)
            radius = math.hypot(radial_distance, normal_distance)
            assert radius > 0
            first = scale(
                sub(scale(toward, radial_distance), scale(normal, normal_distance)), 1 / radius
            )
            radius_squared = math.fsum(
                (radial_distance * radial_distance, normal_distance * normal_distance)
            )
            if normal_distance == 0:
                if radial_distance < 0:
                    normal_raw = tuple(-value for value in normal_raw)
            else:
                normal_raw = add(scale(normal, radial_distance), scale(toward, normal_distance))
            tangent, _ = unit(cross(normal_raw, first))
    return arcs


def solve(speed, acceleration, centers):
    threshold = speed * speed / (2 * acceleration)
    return math.fsum(above_length(*arc, threshold) for arc in trajectory(centers))


def main():
    import sys

    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(tokens)
    output = []
    for _ in range(count):
        speed, acceleration = next(tokens), next(tokens)
        centers = [tuple(next(tokens) for _ in range(DIMENSIONS)) for _ in range(CIRCLES)]
        output.append(f"{solve(speed, acceleration, centers):.12f}")
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
