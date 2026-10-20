import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    height = data[1:]
    order = sorted(range(n), key=height.__getitem__, reverse=True)
    parent = list(range(n))
    size = [0] * n

    def find_root(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    answer = 0
    for vertex in order:
        size[vertex] = 1
        answer += height[vertex]
        for neighbor in (vertex - 1, vertex + 1):
            if neighbor < 0 or neighbor >= n or size[neighbor] == 0:
                continue
            a = find_root(vertex)
            b = find_root(neighbor)
            # Joining two odd runs saves one strike at every remaining level.
            if size[a] % 2 == 1 and size[b] % 2 == 1:
                answer -= height[vertex]
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
    print(answer)


if __name__ == "__main__":
    main()
