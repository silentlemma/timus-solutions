from math import pi, sin


SCALE = 1000
HALF_TURN = 180 * SCALE
RADIANS_PER_UNIT = pi / HALF_TURN


def main():
    radius, angle = map(float, input().split())
    # With at most three decimal places, rounding recovers the exact angle units.
    width = round(angle * SCALE)
    steps, remainder = divmod(HALF_TURN, width)
    shore = (steps - 1) * sin(width * RADIANS_PER_UNIT) + sin(remainder * RADIANS_PER_UNIT)
    print(f"{radius + 2 * radius * shore:.7f}")


if __name__ == "__main__":
    main()
