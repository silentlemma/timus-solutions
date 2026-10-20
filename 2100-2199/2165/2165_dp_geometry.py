import sys

HALF_DIGIT = 5


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    cross = [[a * d - b * c for c, d in zip(x, y)] for a, b in zip(x, y)]
    total = sum(cross[i][(i + 1) % n] for i in range(n))

    # Scores are doubled areas; an edge places no restriction on the minimum.
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i + 1] = total
    for left in range(n - 2, -1, -1):
        row = dp[left]
        base = cross[left]
        for right in range(left + 2, n):
            best = 0
            closing = base[right]
            for middle in range(left + 1, right):
                candidate = row[middle]
                if candidate <= best:
                    continue
                other = dp[middle][right]
                if other <= best:
                    continue
                if other < candidate:
                    candidate = other
                area = base[middle] + cross[middle][right] - closing
                if area < candidate:
                    candidate = area
                if candidate > best:
                    best = candidate
            row[right] = best

    answer = dp[0][n - 1]
    print(f"{answer // 2}.{answer % 2 * HALF_DIGIT}")


if __name__ == "__main__":
    main()
