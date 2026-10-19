import sys

GROUPS = 4  # both courses, only the first, only the second, neither


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    rows = [data[2 + i * m:2 + (i + 1) * m] for i in range(n)]
    columns = [[rows[i][j] == "1" for i in range(n)] for j in range(m)]
    best, pair = n + 1, None
    # every pair of courses is tried: the four groups of a pair are counted
    # in one pass over the programs
    for a in range(m):
        for b in range(a + 1, m):
            count = [0] * GROUPS
            for x, y in zip(columns[a], columns[b]):
                count[2 * x + y] += 1
            if max(count) < best:
                best, pair = max(count), (a + 1, b + 1)
    print(best)
    print(*pair)


main()
