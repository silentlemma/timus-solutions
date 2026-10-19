import math
import sys

TERMINALS = 3
DECIMALS = 12
DISCRIMINANT_SCALE = 4
SUCCESS = "Now we have enough power"


def squared_distance(first, second):
    return sum((a - b) ** 2 for a, b in zip(first, second))


def radical_at_most(target, coefficient, radicand):
    if coefficient == 0 or radicand == 0:
        return target >= 0
    left = target * target
    right = coefficient * coefficient * radicand
    if coefficient > 0:
        return target >= 0 and left >= right
    return target >= 0 or left <= right


def common_point(points, radii):
    for point in points:
        if all(
            squared_distance(point, center) <= radius * radius
            for center, radius in zip(points, radii)
        ):
            return point
    for first in range(TERMINALS):
        for second in range(first + 1, TERMINALS):
            third = TERMINALS - first - second
            origin = points[first]
            dx = points[second][0] - origin[0]
            dy = points[second][1] - origin[1]
            distance = dx * dx + dy * dy
            radius_squared = radii[first] ** 2
            along = distance + radius_squared - radii[second] ** 2
            discriminant = (
                DISCRIMINANT_SCALE * radius_squared * distance - along * along
            )
            if discriminant < 0:
                continue
            wx = origin[0] - points[third][0]
            wy = origin[1] - points[third][1]
            target = distance * (radii[third] ** 2 - radius_squared - wx * wx - wy * wy)
            target -= along * (wx * dx + wy * dy)
            cross = wy * dx - wx * dy
            for sign in (-1, 1):
                if radical_at_most(target, sign * cross, discriminant):
                    height = sign * math.sqrt(discriminant)
                    return (
                        origin[0] + (along * dx - height * dy) / (2 * distance),
                        origin[1] + (along * dy + height * dx) / (2 * distance),
                    )
    return None


def solve(radius, points):
    if all(
        squared_distance(points[0], point) <= (2 * radius) ** 2 for point in points[1:]
    ):
        return [
            tuple((a + b) / 2 for a, b in zip(points[0], point)) for point in points[1:]
        ]
    for doubled in range(TERMINALS):
        radii = [radius] * TERMINALS
        radii[doubled] *= 2
        hub = common_point(points, radii)
        if hub is not None:
            midpoint = tuple((a + b) / 2 for a, b in zip(hub, points[doubled]))
            return [hub, midpoint]
    return None


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    radius = next(values)
    points = [(next(values), next(values)) for _ in range(TERMINALS)]
    answer = solve(radius, points)
    if answer is None:
        print("Death")
    else:
        print(SUCCESS)
        for x, y in answer:
            print(f"{x:.{DECIMALS}f} {y:.{DECIMALS}f}")


if __name__ == "__main__":
    main()
