import sys

ROOT = 1
UNSEEN = -1


def main():
    values = map(int, sys.stdin.buffer.read().split())
    count = next(values)
    graph = [[] for _ in range(count + 1)]
    for _ in range(count - 1):
        left = next(values)
        right = next(values)
        graph[left].append(right)
        graph[right].append(left)
    query_count = next(values)
    if query_count == 0:
        return

    parent = [ROOT] * (count + 1)
    representative = list(range(count + 1))
    first = [UNSEEN] * (count + 1)
    order = []
    adjacent = [0] * (count - 1)
    stack = [ROOT]
    while stack:
        event = stack.pop()
        if event < 0:
            vertex = -event
            representative[vertex] = parent[vertex]
            continue
        vertex = event
        first[vertex] = len(order)
        order.append(vertex)
        # Finished subtrees point to their nearest ancestor still on the DFS path.
        for neighbor in (vertex - 1, vertex + 1):
            if ROOT <= neighbor <= count and first[neighbor] != UNSEEN:
                ancestor = neighbor
                while representative[ancestor] != ancestor:
                    representative[ancestor] = representative[representative[ancestor]]
                    ancestor = representative[ancestor]
                adjacent[min(vertex, neighbor) - 1] = first[ancestor]
        stack.append(-vertex)
        for neighbor in graph[vertex]:
            if neighbor != parent[vertex]:
                parent[neighbor] = vertex
                stack.append(neighbor)
    del graph, parent, representative, stack

    table = [adjacent]
    span = 1
    while span * 2 <= len(adjacent):
        previous = table[-1]
        table.append([a if a < b else b for a, b in zip(previous, previous[span:])])
        span *= 2

    answer_text = [str(vertex) + "\n" for vertex in order]
    output = []
    for left, right in zip(values, values):
        if left == right:
            position = first[left]
        else:
            level = (right - left).bit_length() - 1
            span = 1 << level
            row = table[level]
            # The range LCA has the smallest preorder among adjacent LCAs.
            first_position = row[left - 1]
            last_position = row[right - 1 - span]
            position = first_position if first_position < last_position else last_position
        output.append(answer_text[position])
    sys.stdout.write("".join(output))


if __name__ == "__main__":
    main()
