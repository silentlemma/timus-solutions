import math

SIDES = 4


def main():
    a, r = map(int, input().split())
    half = a / 2
    if r <= half:
        area = math.pi * r * r
    elif r * r >= 2 * half * half:
        area = a * a
    else:
        # the circle minus the four caps cut off by the sides
        cap = r * r * math.acos(half / r) - half * math.sqrt(r * r - half * half)
        area = math.pi * r * r - SIDES * cap
    print("%.3f" % area)


main()
