import sys

PADDING = 2
DIRECTION_COUNT = 4
COORDINATE_COUNT = 3
EMPTY = ord(".")
WALK = 0
JUMP = 1
DROP = 2
CLIMB = 3
DIRECTIONS = ("north", "east", "south", "west")
TYPES = ("walk", "jump", "drop", "climb")


def main():
    data = sys.stdin.buffer.read().split()
    a, b, h = map(int, data[:COORDINATE_COUNT])
    width = b + 2 * PADDING
    rows = a + 2 * PADDING
    plane = width * rows
    size = (h + 2) * plane
    air = bytearray(size)
    standing = bytearray(size)
    offset = COORDINATE_COUNT
    for z in range(1, h + 1):
        for x in range(1, a + 1):
            row = data[offset]
            offset += 1
            base = z * plane + (x + 1) * width + PADDING
            for y, value in enumerate(row):
                cell = base + y
                air[cell] = value == EMPTY
                standing[cell] = air[cell] and not air[cell - plane]
    x, y, z = map(int, data[offset : offset + COORDINATE_COUNT])
    start = z * plane + (x + 1) * width + y + 1
    offset += COORDINATE_COUNT
    x, y, z = map(int, data[offset : offset + COORDINATE_COUNT])
    goal = z * plane + (x + 1) * width + y + 1
    deltas = (-width, 1, width, -1)
    parent = [-1] * size
    action = bytearray(size)
    queue = [start]
    parent[start] = start
    head = 0
    while head < len(queue) and parent[goal] == -1:
        cell = queue[head]
        head += 1
        for direction, delta in enumerate(deltas):
            near = cell + delta
            if standing[near] and parent[near] == -1:
                parent[near] = cell
                action[near] = WALK * DIRECTION_COUNT + direction
                queue.append(near)
            target = near + delta
            if air[near] and air[near - plane] and standing[target] and parent[target] == -1:
                parent[target] = cell
                action[target] = JUMP * DIRECTION_COUNT + direction
                queue.append(target)
            target = near - plane
            if air[near] and standing[target] and parent[target] == -1:
                parent[target] = cell
                action[target] = DROP * DIRECTION_COUNT + direction
                queue.append(target)
            target = near + plane
            if air[cell + plane] and standing[target] and parent[target] == -1:
                parent[target] = cell
                action[target] = CLIMB * DIRECTION_COUNT + direction
                queue.append(target)
    if parent[goal] == -1:
        print("NO")
        return
    path = []
    cell = goal
    while cell != start:
        move = action[cell]
        path.append(TYPES[move // DIRECTION_COUNT] + " " + DIRECTIONS[move % DIRECTION_COUNT])
        cell = parent[cell]
    sys.stdout.write("YES\n" + str(len(path)) + "\n" + "".join(line + "\n" for line in path[::-1]))


if __name__ == "__main__":
    main()
