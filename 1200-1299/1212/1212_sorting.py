rows, cols, ship_count = map(int, input().split())
zones = []
for _ in range(ship_count):
    fields = input().split()
    col, row, size = map(int, fields[:-1])
    horizontal = size if fields[-1] == "H" else 1
    zones.append((col - 2, row - 2, col + horizontal, row + size + 1 - horizontal))
zones.sort()

extra = int(input()) - 1
answer = 0
for dx in {0, extra}:
    dy = extra - dx
    answer += max(0, (cols - dx) * (rows - dy))
    ends = {}
    for left, top, right, bottom in zones:
        # Use the last cell of the new ship as its placement coordinate.
        right = min(cols, right + dx)
        for line in range(max(dy, top), min(rows, bottom + dy)):
            start = max(left, ends.get(line, dx))
            if right > start:
                answer -= right - start
                ends[line] = right
print(answer)
