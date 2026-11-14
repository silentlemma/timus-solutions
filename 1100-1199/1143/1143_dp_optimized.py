from math import hypot
import sys

DECIMALS = 3


def shortest(x, y):
    n = len(x)
    edge = [hypot(x[i] - x[i - 1], y[i] - y[i - 1]) for i in range(n)]
    left, right = [0.0] * n, [0.0] * n
    for span in range(1, n):
        first_left, first_right = left[0], right[0]
        end = span
        for start in range(n):
            if start + 1 == n:
                next_left, next_right = first_left, first_right
                next_edge = edge[0]
            else:
                next_left, next_right = left[start + 1], right[start + 1]
                next_edge = edge[start + 1]
            chord = hypot(x[start] - x[end], y[start] - y[end])
            a, b = next_left + next_edge, next_right + chord
            c, d = left[start] + chord, right[start] + edge[end]
            left[start] = a if a < b else b
            right[start] = c if c < d else d
            end += 1
            if end == n:
                end = 0
    return min(min(left), min(right))


def main():
    words = iter(sys.stdin.buffer.read().split())
    n = int(next(words))
    x, y = [0.0] * n, [0.0] * n
    for i in range(n):
        x[i], y[i] = float(next(words)), float(next(words))
    print(f"{shortest(x, y):.{DECIMALS}f}")


if __name__ == "__main__":
    main()
