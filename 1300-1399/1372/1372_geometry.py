import math
import sys

TINY = 1e-9  # a torque this small is no torque at all
TURN = 360.0
HALF_UNIT = 5e-9  # half of the last printed digit
AXES = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
HEADER = 5  # numbers before the engines
ENGINE = 4  # numbers per engine
ANSWER = 5  # numbers printed


def unit(lon, lat):
    lon, lat = math.radians(lon), math.radians(lat)
    return (math.cos(lat) * math.cos(lon), math.cos(lat) * math.sin(lon), math.sin(lat))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def angles(v):
    length = math.sqrt(sum(c * c for c in v))
    lat = math.degrees(math.asin(max(-1.0, min(1.0, v[2] / length))))
    lon = math.degrees(math.atan2(v[1], v[0])) % TURN
    if lon >= TURN - HALF_UNIT:
        lon = 0.0  # it would print as 360
    return lon + 0.0, lat + 0.0  # no negative zeros


def main():
    data = list(map(float, sys.stdin.read().split()))
    radius, _, mast, thrust, count = data[:HEADER]
    arm = radius + mast  # the engines sit on masts above the surface
    torque = [0.0, 0.0, 0.0]
    for i in range(int(count)):
        lon, lat, dlon, dlat = data[HEADER + ENGINE * i : HEADER + ENGINE * (i + 1)]
        t = cross(unit(lon, lat), unit(dlon, dlat))
        for k in range(len(torque)):
            torque[k] += arm * thrust * t[k]
    size = math.sqrt(sum(c * c for c in torque))
    if size < TINY:
        print(" ".join(["%.8f" % 0.0] * ANSWER))
        return
    # a force f at p turns the station by p x f, at most |p| |f|; so the
    # least thrust |T| / |p| needs p across the torque T and f = p x T / |p|^2
    axis = [c / size for c in torque]
    pick = min(AXES, key=lambda e: abs(sum(a * b for a, b in zip(e, axis))))
    dot = sum(a * b for a, b in zip(pick, axis))
    place = [p - dot * a for p, a in zip(pick, axis)]
    push = cross(place, torque)
    print("%.8f %.8f %.8f %.8f %.8f" % (*angles(place), *angles(push), size / arm))


main()
