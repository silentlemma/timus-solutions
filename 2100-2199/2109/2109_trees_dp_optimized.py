from array import array
import sys

BUFFER_SIZE = 65536
OUTPUT_ROWS = 8192
SPACE = ord(" ")
ROOT = 1


def integers():
    read = sys.stdin.buffer.read
    pending = b""
    while True:
        block = read(BUFFER_SIZE)
        if not block:
            break
        data = pending + block
        words = data.split()
        pending = words.pop() if data[-1] > SPACE else b""
        yield from map(int, words)
    if pending:
        yield int(pending)


def find(representative, vertex):
    while representative[vertex] != vertex:
        representative[vertex] = representative[representative[vertex]]
        vertex = representative[vertex]
    return vertex


def prepare(count, values):
    head = array("I", [0]) * (count + 1)
    target = array("I", [0]) * (2 * count - 1)
    following = array("I", [0]) * len(target)
    for edge in range(1, len(target), 2):
        left, right = next(values), next(values)
        target[edge], following[edge], head[left] = right, head[left], edge
        target[edge + 1], following[edge + 1], head[right] = left, head[right], edge + 1
    queries = next(values)
    if queries == 0:
        return None, None, 0
    parent = array("I", [0]) * (count + 1)
    representative = array("I", [0]) * (count + 1)
    first = array("I", [0]) * (count + 1)
    parent[ROOT] = ROOT
    order = array("I")
    adjacent = array("I", [0]) * (count - 1)
    stack = array("i", [ROOT])
    while stack:
        event = stack.pop()
        if event < 0:
            vertex = -event
            representative[vertex] = parent[vertex]
            continue
        vertex = event
        first[vertex] = len(order) + 1
        representative[vertex] = vertex
        order.append(vertex)
        if vertex > ROOT and first[vertex - 1]:
            adjacent[vertex - 2] = first[find(representative, vertex - 1)] - 1
        if vertex < count and first[vertex + 1]:
            adjacent[vertex - 1] = first[find(representative, vertex + 1)] - 1
        stack.append(-vertex)
        edge = head[vertex]
        while edge:
            neighbor = target[edge]
            if neighbor != parent[vertex]:
                parent[neighbor] = vertex
                stack.append(neighbor)
            edge = following[edge]
    return order, adjacent, queries


def main():
    values = integers()
    count = next(values)
    order, adjacent, queries = prepare(count, values)
    if queries == 0:
        return
    table = [adjacent]
    span = 1
    while span * 2 <= len(adjacent):
        previous = table[-1]
        table.append(array("I", (a if a < b else b for a, b in zip(previous, previous[span:]))))
        span *= 2
    write = sys.stdout.write
    output = []
    for _ in range(queries):
        left, right = next(values), next(values)
        answer = left
        if left < right:
            level = (right - left).bit_length() - 1
            row = table[level]
            first_position = row[left - 1]
            other = row[right - 1 - (1 << level)]
            answer = order[first_position if first_position < other else other]
        output.append(str(answer))
        if len(output) == OUTPUT_ROWS:
            write("\n".join(output) + "\n")
            output.clear()
    if output:
        write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
