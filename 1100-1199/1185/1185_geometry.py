import math
import sys


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n, gap = next(data), next(data)
    pts = sorted(set((next(data), next(data)) for _ in range(n)))
    # the shortest wall is the convex hull pushed out by L: its straight
    # parts add up to the hull perimeter, and its arcs turn once around a
    # full circle of radius L in total
    hull = []
    for seq in (pts, pts[::-1]):
        part = []
        for p in seq:
            while len(part) >= 2 and cross(part[-2], part[-1], p) <= 0:
                part.pop()
            part.append(p)
        hull += part[:-1]
    length = sum(math.dist(hull[k - 1], hull[k]) for k in range(len(hull)))
    print(round(length + 2 * math.pi * gap))


main()
