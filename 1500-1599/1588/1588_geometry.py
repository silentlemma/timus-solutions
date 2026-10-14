import math
import sys

HALF = 0.5  # rounds to the nearest mile


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    xs = [int(v) for v in data[1 : 2 * n + 1 : 2]]
    ys = [int(v) for v in data[2 : 2 * n + 2 : 2]]
    total = 0.0
    for i in range(n):
        # the farthest city in each reduced direction from city i, in steps
        far = {}
        for j in range(n):
            if j != i:
                dx, dy = xs[j] - xs[i], ys[j] - ys[i]
                g = math.gcd(dx, dy)
                d = (dx // g, dy // g)
                far[d] = max(far.get(d, 0), g)
        for (dx, dy), steps in far.items():
            # city i ends the road in this direction when nothing lies behind it
            if (-dx, -dy) not in far:
                total += steps * math.hypot(dx, dy)
    # every road is found from both of its ends
    print(math.floor(total / 2 + HALF))


main()
