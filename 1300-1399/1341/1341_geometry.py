import math
import sys

RADIUS = 6400.0
HALF_TURN = 180.0
SHOWN = 0.0005  # values that print as 0.000
FIELDS = 3


def shown(value):
    """Three decimals, without a minus sign on zero."""
    return "%.3f" % (0.0 if abs(value) < SHOWN else value)


def main():
    w, lon, side = map(float, sys.stdin.read().split()[:FIELDS])
    arc = side / RADIUS  # the angle of one side seen from the center
    south = math.radians(w)
    north = south + arc
    # north and south along meridians cancel; east runs along the northern
    # parallel and west along the southern one, at different speeds
    lon += math.degrees(arc / math.cos(north) - arc / math.cos(south))
    lon = math.fmod(lon, 2 * HALF_TURN)
    if lon > HALF_TURN:
        lon -= 2 * HALF_TURN
    elif lon <= -HALF_TURN:
        lon += 2 * HALF_TURN
    print(shown(w))
    print(shown(lon))


main()
