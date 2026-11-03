import sys


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    points = list(zip(tokens, tokens))
    best = 2
    # Every line through two input points is tried; cross products are exact.
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            dx, dy = points[j][0] - xi, points[j][1] - yi
            count = sum((x - xi) * dy == (y - yi) * dx for x, y in points)
            best = max(best, count)
            if best == n:
                print(best)
                return
    print(best)


main()
