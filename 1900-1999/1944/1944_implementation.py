import sys


def draw(points):
    left = min(0, min(x for x, _ in points))
    right = max(0, max(x for x, _ in points))
    lower = min(0, min(y for _, y in points))
    upper = max(0, max(y for _, y in points))
    width = right - left + 1
    grid = [bytearray(b"." * width) for _ in range(upper - lower + 1)]
    for row in grid:
        row[-left] = ord("|")
    grid[upper] = bytearray(b"-" * width)
    grid[upper][-left] = ord("+")
    for x, y in points:
        grid[upper - y][x - left] = ord("*")
    return b"\n".join(grid) + b"\n"


if __name__ == "__main__":
    words = iter(map(int, sys.stdin.buffer.read().split()))
    size = next(words)
    points = [(next(words), next(words)) for _ in range(size)]
    sys.stdout.buffer.write(draw(points))
