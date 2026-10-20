import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    m = next(data)
    one_way = next(data)
    two_way = next(data)
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for _ in range(m):
        start = next(data) - 1
        end = next(data) - 1
        graph[start].append(end)
        reverse[end].append(start)
    del data

    seen = bytearray(n)
    order = []
    stack = []
    for root in range(n):
        if seen[root]:
            continue
        stack.append(root)
        while stack:
            vertex = stack.pop()
            # A complemented vertex marks the return from its DFS call.
            if vertex < 0:
                order.append(~vertex)
            elif not seen[vertex]:
                seen[vertex] = 1
                stack.append(~vertex)
                for neighbor in graph[vertex]:
                    if not seen[neighbor]:
                        stack.append(neighbor)

    component = [-1] * n
    for root in reversed(order):
        if component[root] != -1:
            continue
        component[root] = root
        stack.append(root)
        while stack:
            vertex = stack.pop()
            for neighbor in reverse[vertex]:
                if component[neighbor] == -1:
                    component[neighbor] = root
                    stack.append(neighbor)

    seen = bytearray(n)
    answer = 0
    for root in range(n):
        if seen[root]:
            continue
        vertices = 0
        components = 0
        seen[root] = 1
        stack.append(root)
        while stack:
            vertex = stack.pop()
            vertices += 1
            components += component[vertex] == vertex
            for neighbor in graph[vertex]:
                if not seen[neighbor]:
                    seen[neighbor] = 1
                    stack.append(neighbor)
            for neighbor in reverse[vertex]:
                if not seen[neighbor]:
                    seen[neighbor] = 1
                    stack.append(neighbor)
        if one_way < two_way:
            tree = (vertices - components) * two_way + (components - 1) * one_way
            answer += min(tree, vertices * one_way)
        else:
            answer += (vertices - 1) * two_way
    print(answer)


if __name__ == "__main__":
    main()
