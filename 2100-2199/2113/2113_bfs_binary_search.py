import sys

MAX_HEIGHT = 100000


def solve(data):
    values = iter(map(int, data.split()))
    rows = next(values)
    columns = next(values)
    stride = columns + 2
    size = (rows + 2) * stride
    infinity = size
    height = [MAX_HEIGHT + 1] * size
    flood = [0] * size
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            cell = row * stride + column
            height[cell] = next(values)
            flood[cell] = infinity
    start = next(values) * stride + next(values)
    source = next(values) * stride + next(values)
    offsets = (-stride, stride, -1, 1)
    flood[source] = 0
    queue = [source]
    for cell in queue:
        arrival = flood[cell] + 1
        for offset in offsets:
            neighbor = cell + offset
            if flood[neighbor] == infinity and height[neighbor] <= height[cell]:
                flood[neighbor] = arrival
                queue.append(neighbor)

    def survives(jump):
        if flood[start] == infinity:
            return True
        distance = [-1] * size
        distance[start] = 0
        queue = [start]
        for cell in queue:
            arrival = distance[cell] + 1
            ceiling = height[cell] + jump
            for offset in offsets:
                neighbor = cell + offset
                if (
                    distance[neighbor] == -1
                    and height[neighbor] <= ceiling
                    and arrival < flood[neighbor]
                ):
                    if flood[neighbor] == infinity:
                        return True
                    distance[neighbor] = arrival
                    queue.append(neighbor)
        return False

    if not survives(MAX_HEIGHT):
        return -1
    low = 0
    high = MAX_HEIGHT
    while low < high:
        middle = (low + high) // 2
        if survives(middle):
            high = middle
        else:
            low = middle + 1
    return low


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
