import math
import sys
from fractions import Fraction


def read_objects():
    size, distance = sys.stdin.readline().split()
    distance = Fraction(distance)
    rows = [tuple(map(Fraction, sys.stdin.readline().split())) for _ in range(int(size))]
    scale = distance.denominator
    for row in rows:
        scale = math.lcm(scale, *(value.denominator for value in row))

    def scaled(value):
        return value.numerator * (scale // value.denominator)

    return scaled(distance), [tuple(map(scaled, row)) for row in rows]


def main():
    distance, objects = read_objects()
    distance_squared = distance * distance
    best = math.inf
    pair = None

    for i, (x, y, z, u, v, w) in enumerate(objects):
        for j in range(i + 1, len(objects)):
            xx, yy, zz, uu, vv, ww = objects[j]
            px, py, pz = xx - x, yy - y, zz - z
            vx, vy, vz = uu - u, vv - v, ww - w
            projection = px * vx + py * vy + pz * vz
            if projection >= 0:
                continue
            speed_squared = vx * vx + vy * vy + vz * vz
            offset = px * px + py * py + pz * pz - distance_squared
            discriminant = projection * projection - speed_squared * offset
            if discriminant < 0:
                continue

            # Normalize before taking the square root to avoid large floats.
            relative_root = math.sqrt(discriminant / (projection * projection))
            time = (offset / -projection) / (1 + relative_root)
            if time < best:
                best, pair = time, (i + 1, j + 1)

    if pair is None:
        print("OK")
    else:
        print(f"ALARM!\n{best:.3f} {pair[0]} {pair[1]}")


if __name__ == "__main__":
    main()
