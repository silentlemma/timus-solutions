import sys


def count_lines(rows, cols, zones, length):
    width = cols - length + 1
    if width <= 0:
        return 0
    blocked = set()
    # Lengths are at most four: each zone excludes at most 36 starting cells.
    for top, bottom, left, right in zones:
        for row in range(max(1, top), min(rows, bottom) + 1):
            offset = (row - 1) * cols
            for col in range(max(1, left - length + 1), min(width, right) + 1):
                blocked.add(offset + col - 1)
    return rows * width - len(blocked)


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    rows, cols, ships = int(next(tokens)), int(next(tokens)), int(next(tokens))
    zones = []
    for _ in range(ships):
        col, row, size = int(next(tokens)), int(next(tokens)), int(next(tokens))
        way = next(tokens)
        bottom = row + size - 1 if way == b"V" else row
        right = col + size - 1 if way == b"H" else col
        zones.append((row - 1, bottom + 1, col - 1, right + 1))
    length = int(next(tokens))
    answer = count_lines(rows, cols, zones, length)
    if length > 1:
        flipped = [(left, right, top, bottom) for top, bottom, left, right in zones]
        answer += count_lines(cols, rows, flipped, length)
    print(answer)


main()
