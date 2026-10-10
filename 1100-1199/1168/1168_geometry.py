import sys
from math import isqrt

# R is a real number; all other lengths are integers, so a squared distance
# is an integer and only the integer part of R*R matters
EPS = 1e-6
# above every altitude a station allows: 32000 plus 100000
SKY = 10**6


def main():
    data = iter(sys.stdin.buffer.read().split())
    m, n, k = int(next(data)), int(next(data)), int(next(data))
    h = [int(next(data)) for _ in range(m * n)]
    stations = []
    taken = set()
    for _ in range(k):
        i, j, r = int(next(data)) - 1, int(next(data)) - 1, float(next(data))
        stations.append((i, j, h[i * n + j], int(r * r + EPS)))
        taken.add(i * n + j)
    total = 0
    for i in range(m):
        for j in range(n):
            if i * n + j in taken:
                continue
            # the receiver at altitude a hears a station at height z when
            # (a - z)^2 <= R^2 - (horizontal distance)^2
            low, high = h[i * n + j], SKY
            for si, sj, z, reach in stations:
                rest = reach - (i - si) ** 2 - (j - sj) ** 2
                if rest < 0:
                    high = -1
                    break
                s = isqrt(rest)
                if z - s > low:
                    low = z - s
                if z + s < high:
                    high = z + s
                if low > high:
                    break
            if low <= high:
                total += high - low + 1
    print(total)


main()
