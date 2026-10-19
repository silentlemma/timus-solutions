import math
import sys

DIMENSIONS = 3
ITERATIONS = 80
OUTPUT_DIGITS = 10


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def meeting_time(carrier, ship, speed):
    radius_squared = dot(carrier, carrier)
    distance_squared = dot(ship, ship)
    radius = math.sqrt(radius_squared)
    distance = math.sqrt(distance_squared)
    delta = distance_squared - radius_squared
    tangent = math.sqrt(delta)
    radial_gap = delta / (distance + radius)
    cross = (
        carrier[1] * ship[2] - carrier[2] * ship[1],
        carrier[2] * ship[0] - carrier[0] * ship[2],
        carrier[0] * ship[1] - carrier[1] * ship[0],
    )
    angle = math.atan2(math.sqrt(dot(cross, cross)), dot(carrier, ship))
    visible_angle = math.atan2(tangent, radius)

    def ship_length(beta):
        if beta <= visible_angle:
            sideways = 2 * math.sqrt(distance * radius) * math.sin(beta / 2)
            return math.hypot(radial_gap, sideways)
        return tangent + radius * (beta - visible_angle)

    radial_time = radial_gap / speed
    if radius * angle <= radial_time:
        return radial_time
    low, high = 0.0, angle
    for _ in range(ITERATIONS):
        beta = (low + high) / 2
        if radius * (angle - beta) > ship_length(beta) / speed:
            low = beta
        else:
            high = beta
    beta = (low + high) / 2
    return max(radius * (angle - beta), ship_length(beta) / speed)


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    carrier = values[:DIMENSIONS]
    ship = values[DIMENSIONS : 2 * DIMENSIONS]
    print(f"{meeting_time(carrier, ship, values[-1]):.{OUTPUT_DIGITS}f}")


if __name__ == "__main__":
    main()
