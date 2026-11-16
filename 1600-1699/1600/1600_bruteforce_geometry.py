import math
import sys


def main():
    size, distance = sys.stdin.buffer.readline().split()
    distance_squared = float(distance) ** 2
    objects = [tuple(map(float, sys.stdin.buffer.readline().split())) for _ in range(int(size))]
    best = math.inf
    pair = None

    for i, (x, y, z, u, v, w) in enumerate(objects, 1):
        for j, (xx, yy, zz, uu, vv, ww) in enumerate(objects[i:], i + 1):
            px, py, pz = xx - x, yy - y, zz - z
            vx, vy, vz = uu - u, vv - v, ww - w
            projection = px * vx + py * vy + pz * vz
            if projection >= 0:
                continue

            speed_squared = vx * vx + vy * vy + vz * vz
            offset = -distance_squared + px * px + py * py + pz * pz
            discriminant = projection * projection - speed_squared * offset
            if discriminant < 0:
                continue

            # The equivalent smaller root avoids subtracting nearly equal values.
            time = offset / (-projection + math.sqrt(discriminant))
            if 0 <= time < best:
                best, pair = time, (i, j)

    if pair is None:
        print("OK")
    else:
        print(f"ALARM!\n{best:.3f} {pair[0]} {pair[1]}")


if __name__ == "__main__":
    main()
