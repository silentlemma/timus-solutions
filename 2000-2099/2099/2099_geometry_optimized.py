import sys


def valid(coordinates):
    ax, ay, az, bx, by, bz, cx, cy, cz, dx, dy, dz = coordinates
    ux, uy, uz = bx - ax, by - ay, bz - az
    vx, vy, vz = dx - cx, dy - cy, dz - cz
    if ux * vx + uy * vy + uz * vz:
        return False
    wx, wy, wz = cx - ax, cy - ay, cz - az
    if wx * ux + wy * uy + wz * uz < ux * ux + uy * uy + uz * uz:
        return False
    if wx * vx + wy * vy + wz * vz < 0:
        return False
    # The scalar triple product vanishes exactly when the lines are coplanar.
    return wx * (uy * vz - uz * vy) + wy * (uz * vx - ux * vz) + wz * (ux * vy - uy * vx) == 0


def main():
    coordinates = map(int, sys.stdin.buffer.read().split())
    print("Valid" if valid(coordinates) else "Invalid")


if __name__ == "__main__":
    main()
