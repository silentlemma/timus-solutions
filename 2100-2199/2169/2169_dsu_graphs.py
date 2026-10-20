import sys

MODULUS = 1_000_000_007
MAX_INCOMING = 3
MAX_DEGREE = MAX_INCOMING + 1


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    m = next(data)
    parent = list(range(n))
    size = [1] * n
    edges = [0] * n
    degree = [0] * n

    def find(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for _ in range(m):
        left = next(data) - 1
        right = next(data) - 1
        degree[left] += 1
        degree[right] += 1
        left = find(left)
        right = find(right)
        if left != right:
            if size[left] < size[right]:
                left, right = right, left
            parent[right] = left
            size[left] += size[right]
            edges[left] += edges[right]
        edges[left] += 1

    if any(value > MAX_DEGREE for value in degree):
        print(0)
        return

    roots = [0] * n
    for vertex, value in enumerate(degree):
        if value <= MAX_INCOMING:
            roots[find(vertex)] += 1

    answer = 1
    for vertex in range(n):
        if parent[vertex] != vertex:
            continue
        if edges[vertex] > size[vertex]:
            print(0)
            return
        # A tree chooses its sink; a single cycle chooses its direction.
        ways = 2 if edges[vertex] == size[vertex] else roots[vertex]
        answer = answer * ways % MODULUS
    print(answer)


if __name__ == "__main__":
    main()
