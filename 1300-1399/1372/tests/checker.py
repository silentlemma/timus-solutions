"""Checker: a place, a direction and a thrust for the new engine that
cancel the torque of the running ones, with the least thrust that can,
|T| / (R + h)."""

import math
import sys

FIELDS = 5
TOLERANCE = 1e-6  # relative, the angles are printed to eight decimals


def unit(lon, lat):
    lon, lat = math.radians(lon), math.radians(lat)
    return (math.cos(lat) * math.cos(lon), math.cos(lat) * math.sin(lon), math.sin(lat))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = list(map(float, open(inp).read().split()))
    radius, _, mast, thrust, count = data[:5]
    arm = radius + mast
    torque = [0.0, 0.0, 0.0]
    for i in range(int(count)):
        lon, lat, dlon, dlat = data[5 + 4 * i : 9 + 4 * i]
        t = cross(unit(lon, lat), unit(dlon, dlat))
        torque = [a + arm * thrust * b for a, b in zip(torque, t)]
    size = math.sqrt(sum(c * c for c in torque))
    try:
        got = [float(w) for w in open(output).read().split()]
    except ValueError:
        fail("not a number")
    if len(got) != FIELDS:
        fail("expected five numbers")
    lon, lat, dlon, dlat, force = got
    if not (-90 <= lat <= 90 and -90 <= dlat <= 90 and force >= 0):
        fail("a latitude or the thrust is out of range")
    if abs(force - size / arm) > TOLERANCE * max(1.0, size / arm):
        fail("thrust %.8f, the least is %.8f" % (force, size / arm))
    own = cross(unit(lon, lat), unit(dlon, dlat))
    rest = [a + arm * force * b for a, b in zip(torque, own)]
    left = math.sqrt(sum(c * c for c in rest))
    if left > TOLERANCE * max(1.0, size):
        fail("a torque of %.6f is left" % left)


if __name__ == "__main__":
    main()
