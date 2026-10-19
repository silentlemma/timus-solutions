import math
import sys

FOCAL_SCALE = 3
AXIS_SCALE = 6


def solve(a, b, c):
    x, y, z = a * a, b * b, c * c
    discriminant = 2 * ((x - y) ** 2 + (y - z) ** 2 + (z - x) ** 2)
    gap = math.sqrt(discriminant)
    return math.sqrt(2 * gap) / FOCAL_SCALE, math.sqrt(x + y + z + gap) / AXIS_SCALE


def main():
    focal_distance, radius = solve(*map(int, sys.stdin.buffer.read().split()))
    print(f"{focal_distance:.12f} {radius:.12f}")


if __name__ == "__main__":
    main()
