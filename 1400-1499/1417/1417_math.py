import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    vals = list(map(float, data[1 : 1 + n * n]))
    # rows A x = 1: every player move then earns the same; x scaled to sum 1 is the answer
    rows = [vals[i * n : (i + 1) * n] + [1.0] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(rows[r][col]))
        rows[col], rows[pivot] = rows[pivot], rows[col]
        head = rows[col]
        for r in range(col + 1, n):
            f = rows[r][col] / head[col]
            if f:
                row = rows[r]
                rows[r] = [a - f * b for a, b in zip(row, head)]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        row = rows[i]
        x[i] = (row[n] - sum(row[j] * x[j] for j in range(i + 1, n))) / row[i]
    total = sum(x)
    print("\n".join("%.5f" % (v / total) for v in x))


main()
