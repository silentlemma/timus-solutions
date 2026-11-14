import sys

HEADER = 4
PADDING = 4
SEA = 0
LAND = 1
EXTERIOR = 2
BLOCKED = 4
VISITED = 8
CELL_VALUES = bytes.maketrans(b".#", bytes((SEA, LAND)))


def flood(cells, start, steps, mask, target, mark):
    cells[start] = mark
    stack = [start]
    append, pop = stack.append, stack.pop
    while stack:
        cell = pop()
        for step in steps:
            neighbor = cell + step
            if cells[neighbor] & mask == target:
                cells[neighbor] = mark
                append(neighbor)


def count_islands(width, height, x, y, raw):
    stride = width + PADDING
    edge = bytes((BLOCKED,)) * stride
    border = bytes((BLOCKED, EXTERIOR))
    reverse_border = border[::-1]
    outside = border + bytes((EXTERIOR,)) * width + reverse_border
    cells = bytearray(edge + outside)
    map_cells = raw.translate(CELL_VALUES, b" \t\r\n\v\f")
    for offset in range(0, width * height, width):
        cells.extend(border + map_cells[offset : offset + width] + reverse_border)
    cells.extend(outside + edge)
    sides = (1, -1, stride, -stride)
    directions = sides + (stride + 1, stride - 1, 1 - stride, -stride - 1)
    start = (y + 1) * stride + x + 1
    if cells[start] == SEA:
        flood(cells, start, directions, LAND | EXTERIOR | BLOCKED, SEA, BLOCKED)
    flood(cells, stride + 1, sides, BLOCKED | VISITED, SEA, VISITED)
    count = 0
    for index, state in enumerate(cells):
        if state == LAND:
            count += 1
            flood(cells, index, sides, LAND, LAND, VISITED)
    return count


def main():
    *header, cells = sys.stdin.buffer.read().split(maxsplit=HEADER)
    print(count_islands(*map(int, header), cells))


if __name__ == "__main__":
    main()
