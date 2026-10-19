import sys

DIRECTION_COUNT = 4
ROW_STEP = (-1, 0, 1, 0)
COL_STEP = (0, 1, 0, -1)
TURN = "FR?L"
DEPOT = ord("S")
STATION = ord("X")
HORIZONTAL = ord("-")
VERTICAL = ord("|")


def main():
    read = sys.stdin.buffer.readline
    rows, cols = map(int, read().split())
    stride = cols + 2
    capacity = (rows + 2) * stride
    border = b"." * (2 * cols + 1)
    grid = [border]
    root = 0
    for row in range(2 * rows - 1):
        line = b"." + read().strip() + b"."
        grid.append(line)
        depot_col = line.find(b"S")
        if depot_col != -1:
            root = (row // 2 + 1) * stride + (depot_col + 1) // 2
    grid.append(border)

    parent = [0] * capacity
    depth = [0] * capacity
    first = [0] * capacity
    sibling = [0] * capacity
    incoming = [0] * capacity
    turn = [""] * capacity
    tin = [0] * capacity
    size = [1] * capacity
    heavy = [0] * capacity
    preferred = [0] * capacity
    head = [0] * capacity
    offsets = (-stride, 1, stride, -1)
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        tin[node] = len(order)
        order.append(node)
        row, col = divmod(node, stride)
        map_row = 2 * row - 1
        map_col = 2 * col - 1
        for direction in range(DIRECTION_COUNT):
            edge = grid[map_row + ROW_STEP[direction]][map_col + COL_STEP[direction]]
            if edge != HORIZONTAL and edge != VERTICAL:
                continue
            child = node + offsets[direction]
            if child == parent[node]:
                continue
            parent[child] = node
            depth[child] = depth[node] + 1
            incoming[child] = direction
            turn[child] = TURN[(direction - incoming[node]) % DIRECTION_COUNT]
            sibling[child] = first[node]
            first[node] = child
            stack.append(child)

    for node in reversed(order):
        row, col = divmod(node, stride)
        state = grid[2 * row - 1][2 * col - 1]
        if state == STATION:
            preferred[node] = node
        child = first[node]
        while child:
            size[node] += size[child]
            if not heavy[node] or size[child] > size[heavy[node]]:
                heavy[node] = child
            if state == DEPOT or ord(turn[child]) == state:
                preferred[node] = preferred[child]
            child = sibling[child]

    head[root] = root
    for node in order:
        child = first[node]
        while child:
            head[child] = head[node] if child == heavy[node] else child
            child = sibling[child]

    base = 1
    while base < len(order):
        base *= 2
    recent = [0] * (2 * base)
    count = int(read())
    destinations = [0] * (count + 1)
    events = []
    previous = preferred[root]
    for index in range(1, count + 1):
        departure, row, col = map(int, read().split())
        destination = row * stride + col
        destinations[index] = destination
        if destination == previous:
            continue

        endpoint = previous
        while endpoint != destination:
            left = destination
            right = endpoint
            while head[left] != head[right]:
                if depth[head[left]] > depth[head[right]]:
                    left = parent[head[left]]
                else:
                    right = parent[head[right]]
            junction = left if depth[left] < depth[right] else right
            child = first[junction]
            position = tin[destination]
            while not tin[child] <= position < tin[child] + size[child]:
                child = sibling[child]
            events.append((departure + depth[junction], junction, turn[child]))

            # The latest visitor fixes every switch on its path through this subtree.
            left = base + tin[child]
            right = left + size[child]
            latest = 0
            while left < right:
                if left & 1:
                    if recent[left] > latest:
                        latest = recent[left]
                    left += 1
                if right & 1:
                    right -= 1
                    if recent[right] > latest:
                        latest = recent[right]
                left //= 2
                right //= 2
            endpoint = destinations[latest] if latest else preferred[child]

        position = base + tin[destination]
        while position:
            recent[position] = index
            position //= 2
        previous = destination

    events.sort()
    output = [str(len(events))]
    for time, node, direction in events:
        row, col = divmod(node, stride)
        output.append(f"{time} {row} {col} {direction}")
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
