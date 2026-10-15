import sys
from collections import defaultdict

HEADER = 3  # m, n and k come first


def main():
    data = sys.stdin.buffer.read().split()
    m, n, k = int(data[0]), int(data[1]), int(data[2])
    black = set()
    rows, cols = defaultdict(list), defaultdict(list)
    for i in range(k):
        x, y = int(data[HEADER + 2 * i]), int(data[HEADER + 2 * i + 1])
        black.add((x, y))
        rows[x].append(y)
        cols[y].append(x)

    def closed(x, y):
        return not (1 <= x <= m and 1 <= y <= n) or (x, y) in black

    count = 0
    # A white run of length 2 or more is a strip by itself; a single white
    # cell is one only if it is closed in the other direction too.
    for x in range(1, m + 1):
        prev = 0
        for b in sorted(rows[x]) + [n + 1]:
            length = b - prev - 1
            if length >= 2:
                count += 1
            elif length == 1 and closed(x - 1, prev + 1) and closed(x + 1, prev + 1):
                count += 1
            prev = b
    for y in range(1, n + 1):
        prev = 0
        for b in sorted(cols[y]) + [m + 1]:
            if b - prev - 1 >= 2:
                count += 1
            prev = b
    print(count)


main()
