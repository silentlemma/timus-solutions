"""Check a legal blocker and compare literal BFS distance with the expected blocker."""

from collections import deque
from pathlib import Path
import sys

DISCONNECTED = 10**9
DOT = ord(".")
HEADER_SIZE = 6


def read_case(path):
    data = path.read_bytes().split()
    rows, cols, sr, sc, tr, tc = map(int, data[:HEADER_SIZE])
    grid = data[HEADER_SIZE:]
    if len(grid) != rows or any(len(row) != cols for row in grid):
        raise ValueError("invalid grid")
    return grid, (sr - 1, sc - 1), (tr - 1, tc - 1)


def distance_after(grid, start, target, ban):
    rows, cols = len(grid), len(grid[0])
    distance = [-1] * (rows * cols)
    begin = start[0] * cols + start[1]
    finish = target[0] * cols + target[1]
    distance[begin] = 0
    queue = deque([begin])
    while queue:
        vertex = queue.popleft()
        if vertex == finish:
            return distance[vertex]
        row, col = divmod(vertex, cols)
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) == ban:
                continue
            other = nr * cols + nc
            if grid[nr][nc] == DOT and distance[other] < 0:
                distance[other] = distance[vertex] + 1
                queue.append(other)
    return DISCONNECTED


def selected_score(grid, start, target, data):
    try:
        coordinates = list(map(int, data.split()))
    except ValueError:
        return None
    if len(coordinates) != 2:
        return None
    row, col = (value - 1 for value in coordinates)
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return None
    if (row, col) in (start, target) or grid[row][col] != DOT:
        return None
    return distance_after(grid, start, target, (row, col))


if __name__ == "__main__":
    input_path, expected_path, actual_path = map(Path, sys.argv[1:])
    grid, start, target = read_case(input_path)
    expected = selected_score(grid, start, target, expected_path.read_bytes())
    actual = selected_score(grid, start, target, actual_path.read_bytes())
    valid = expected is not None and actual == expected
    print("OK" if valid else "illegal cell or nonoptimal replacement distance")
    sys.exit(0 if valid else 1)
