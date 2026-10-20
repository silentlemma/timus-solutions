import sys

MIN_SIDE = 3
HEADER_SIZE = 2 * 2
BOARD_SIZE = 2 * 2


def find(parent, vertex):
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex


def connect(events, parent, sizes):
    events.sort()
    coordinate = None
    last = [-1, -1]
    high = [0, 0]
    for current, low, upper, board, side in events:
        if current != coordinate:
            coordinate = current
            last = [-1, -1]
        opposite = 1 - side
        # Sides of the same kind at this coordinate have disjoint closed intervals.
        if last[opposite] != -1 and high[opposite] >= low:
            first = find(parent, board)
            second = find(parent, last[opposite])
            if first != second:
                if sizes[first] < sizes[second]:
                    first, second = second, first
                parent[second] = first
                sizes[first] += sizes[second]
        last[side] = board
        high[side] = upper


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    count = data[0]
    x, y = data[2:HEADER_SIZE]
    boards = []
    start = 0
    isolated = False
    for index in range(count):
        position = HEADER_SIZE + BOARD_SIZE * index
        left, bottom, right, top = data[position : position + BOARD_SIZE]
        boards.append((left, bottom, right, top))
        if left <= x < right and bottom <= y < top:
            start = index
            isolated = (
                right - left == MIN_SIDE
                and top - bottom == MIN_SIDE
                and x == left + 1
                and y == bottom + 1
            )
    if isolated:
        print(1)
        return
    del data

    parent = list(range(count))
    sizes = [1] * count
    for axis in range(2):
        events = []
        for index, (left, bottom, right, top) in enumerate(boards):
            if axis == 0:
                events.append((right + 1, bottom, top, index, 0))
                events.append((left, bottom, top, index, 1))
            else:
                events.append((top + 1, left, right, index, 0))
                events.append((bottom, left, right, index, 1))
        connect(events, parent, sizes)
    print(sizes[find(parent, start)])


if __name__ == "__main__":
    main()
