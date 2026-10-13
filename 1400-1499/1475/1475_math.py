import sys
from math import isqrt

FIELDS = 3  # H, l and h
SPEED = 4  # bounces k come at 4 h sin(a) k (k + 1) down the slope


def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        height, run, drop = (int(x) for x in data[1 + FIELDS * i : 1 + FIELDS * (i + 1)])
        # the largest k with SPEED * drop * height * k (k + 1) <= run^2 + height^2
        q = (run * run + height * height) // (SPEED * drop * height)
        k = (isqrt((q << 2) + 1) - 1) // 2  # k (k + 1) <= q, so (2k + 1)^2 <= 4q + 1
        out.append(k + 1)
    sys.stdout.write("".join("%d\n" % x for x in out))


main()
