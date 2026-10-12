import math
import sys

HEADER = 3  # n, m and the radius
MOST = 4.0  # the longest squared chord, between opposite points


def unit(latitude, longitude):
    """The point on the unit sphere."""
    a, b = math.radians(latitude), math.radians(longitude)
    return math.cos(a) * math.cos(b), math.cos(a) * math.sin(b), math.sin(a)


def main():
    data = sys.stdin.read().split()
    n, m, r = int(data[0]), int(data[1]), float(data[2])
    words = [float(x) for x in data[HEADER:]]
    pads = [unit(words[2 * i], words[2 * i + 1]) for i in range(m)]
    out = []
    for i in range(m, m + n):
        x, y, z = unit(words[2 * i], words[2 * i + 1])
        # the nearest pad has the shortest chord through the planet
        best = MOST
        for px, py, pz in pads:
            dx, dy, dz = x - px, y - py, z - pz
            chord = dx * dx + dy * dy + dz * dz
            if chord < best:
                best = chord
        half = min(1.0, math.sqrt(best) / 2)
        out.append("%.2f" % (2 * r * math.asin(half)))
    print("\n".join(out))


main()
