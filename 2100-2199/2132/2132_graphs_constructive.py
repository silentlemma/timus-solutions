import sys

ROOT_PARENT = -1


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    largest = max(data)
    graph = [[] for _ in range(largest + 1)]
    for index in range(0, len(data), 2):
        first, second = data[index], data[index + 1]
        graph[first].append(second)
        graph[second].append(first)
    del data

    parent = [0] * (largest + 1)
    rank = [0] * (largest + 1)
    order = []
    for root in range(1, largest + 1):
        if parent[root] or not graph[root]:
            continue
        parent[root] = ROOT_PARENT
        stack = [root]
        while stack:
            vertex = stack.pop()
            rank[vertex] = len(order)
            order.append(vertex)
            for neighbor in graph[vertex]:
                if parent[neighbor] == 0:
                    parent[neighbor] = vertex
                    stack.append(neighbor)

    used_parent = bytearray(largest + 1)
    answer = []
    for vertex in reversed(order):
        pending = 0
        ancestor = parent[vertex]
        for neighbor in graph[vertex]:
            if neighbor == ancestor:
                continue
            if parent[neighbor] == vertex:
                if used_parent[neighbor]:
                    continue
            elif rank[neighbor] > rank[vertex]:
                continue
            if pending:
                answer.append(f"{pending} {vertex} {neighbor}")
                pending = 0
            else:
                pending = neighbor
        # An odd leftover consumes the parent edge; an even subtree returns it.
        if pending:
            if ancestor == ROOT_PARENT:
                sys.stdout.write(str(ROOT_PARENT) + "\n")
                return
            answer.append(f"{pending} {vertex} {ancestor}")
            used_parent[vertex] = 1

    sys.stdout.write(str(len(answer)) + "\n" + "\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
