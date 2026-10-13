import math

GRAVITY = 10


def main():
    n, m = map(int, input().split())
    # the speed at depth d is sqrt(2 g d), whatever the way down was
    speed = [math.sqrt(2 * GRAVITY * d) for d in range(m + 1)]
    length = [[math.hypot(dx, dd) for dd in range(m + 1)] for dx in range(n + 1)]
    # best holds the least time to reach each depth and distance to the left,
    # where a board with constant acceleration takes 2 L / (v1 + v2)
    best = [[math.inf] * (n + 1) for _ in range(m + 1)]
    best[0][0] = 0.0
    for d in range(1, m + 1):
        row, vd = best[d], speed[d]
        for e in range(d):
            vs = vd + speed[e]
            board = [2 * length[k][d - e] / vs for k in range(n + 1)]
            for x, t in enumerate(best[e]):
                if t < math.inf:
                    row[x:] = map(min, row[x:], [t + b for b in board])
    print("%.4f" % best[m][n])


main()
