import sys

BASE = ord("1")
BASE_CELL = b"1"


def row_transform(values, far):
    width = len(values)
    if max(values) <= 1:
        return list(values)
    costs = [value * value for value in values]
    intercepts = [value + x * x for x, value in enumerate(costs)]
    sites = [0] * width
    starts = [0] * width
    used = 0
    for q in range(width):
        if values[q] >= far:
            continue
        first = 0
        while used:
            p = sites[used - 1]
            denominator = 2 * (q - p)
            numerator = intercepts[q] - intercepts[p]
            first = -((-numerator) // denominator)
            if first > starts[used - 1]:
                break
            used -= 1
        if not used:
            first = 0
        sites[used] = q
        starts[used] = first
        used += 1
    answer = []
    current = 0
    for x in range(width):
        while current + 1 < used and starts[current + 1] <= x:
            current += 1
        p = sites[current]
        delta = x - p
        answer.append(delta * delta + costs[p])
    return answer


def distance_rows(height, width, cells):
    far = height + width
    active = [column for column in range(width) if BASE_CELL in cells[column::width]]
    distances = []
    last = [-far] * width
    for row in range(height):
        cells_row = cells[row * width : (row + 1) * width]
        values = [far] * width
        for column in active:
            if cells_row[column] == BASE:
                last[column] = row
            values[column] = row - last[column]
        distances.append(values)
    following = [height + far] * width
    for row in range(height - 1, -1, -1):
        values = distances[row]
        for column in active:
            value = values[column]
            if value == 0:
                following[column] = row
            else:
                below = following[column] - row
                if below < value:
                    values[column] = below
    for values in distances:
        yield row_transform(values, far)


def main():
    height, width = map(int, sys.stdin.buffer.readline().split())
    cells = sys.stdin.buffer.read().translate(None, b" \t\r\n")
    write = sys.stdout.write
    for row in distance_rows(height, width, cells):
        write(" ".join(map(str, row)) + "\n")


if __name__ == "__main__":
    main()
