"""Check input, expected, candidate by exact 3D projection and aligned color order."""
from pathlib import Path
import sys


BLOCK_SIDE = 2


def check(photo, candidate):
    rows, columns = len(photo), len(photo[0])
    lines = candidate.splitlines()
    at = 0
    projected = [[0] * columns for _ in range(rows)]
    white_seen = set()
    for level in range(min(rows, columns) // BLOCK_SIDE):
        if level:
            if at >= len(lines) or lines[at] != '':
                return False
            at += 1
        for row in range(rows // BLOCK_SIDE - level):
            if at >= len(lines):
                return False
            line = lines[at]
            at += 1
            if len(line) != columns // BLOCK_SIDE - level or not set(line) <= set('RW'):
                return False
            for column, color in enumerate(line):
                x = level + BLOCK_SIDE * row
                y = level + BLOCK_SIDE * column
                if color == 'W':
                    white_seen.add((x, y))
                else:
                    if (x, y) in white_seen:
                        return False
                    for dx in range(BLOCK_SIDE):
                        for dy in range(BLOCK_SIDE):
                            projected[x + dx][y + dy] += 1
    return not any(line.strip() for line in lines[at:]) and projected == photo


def main():
    data = iter(map(int, Path(sys.argv[1]).read_text().split()))
    rows, columns = next(data), next(data)
    photo = [[next(data) for _ in range(columns)] for _ in range(rows)]
    if not check(photo, Path(sys.argv[3]).read_text()):
        print('Expected valid R/W layers with matching projection and no aligned red above white')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
