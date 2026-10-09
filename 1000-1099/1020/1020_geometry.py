import math
import sys


def main():
    data = sys.stdin.read().split()
    n, r = int(data[0]), float(data[1])
    coords = list(map(float, data[2:]))
    points = list(zip(coords[0::2], coords[1::2]))[:n]
    # the straight parts are the sides of the polygon, the arcs around the
    # nails turn by 2*pi in total: one full circle of radius r
    length = 2 * math.pi * r
    if n > 1:
        length += sum(math.dist(points[i], points[(i + 1) % n]) for i in range(n))
    print("%.2f" % length)


main()
