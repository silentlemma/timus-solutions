from math import factorial

ISLANDS = 3


def main():
    n = int(input())
    # plane[b][c][i]: sequences of islands that start on the tourist's island
    # 0, use a, b and c cities of the islands (a fixed per plane), never
    # repeat an island twice in a row and end on island i
    prev = None
    for a in range(1, n + 1):
        cur = [[[0] * ISLANDS for _ in range(n + 1)] for _ in range(n + 1)]
        for b in range(n + 1):
            for c in range(n + 1):
                cell = cur[b][c]
                if a == 1 and b == c == 0:
                    cell[0] = 1
                if prev:
                    cell[0] = prev[b][c][1] + prev[b][c][2]
                if b:
                    left = cur[b - 1][c]
                    cell[1] = left[0] + left[2]
                if c:
                    left = cur[b][c - 1]
                    cell[2] = left[0] + left[1]
        prev = cur
    # the trip closes back on island 0, so it must not end there
    shapes = prev[n][n][1] + prev[n][n][2]
    # cities fill the island slots in any order, except the fixed start, and
    # every trip is counted once in each direction
    print(shapes * factorial(n - 1) * factorial(n) ** 2 // 2)


main()
