import sys

MODULUS = 1_000_000_007
QUERY = 2


def main():
    read = sys.stdin.buffer.readline
    size = int(read())
    direct = [0, *map(int, read().split())]
    neighbors = [[] for _ in range(size + 1)]
    for _ in range(size - 1):
        a, b = map(int, read().split())
        neighbors[a].append(b)
        neighbors[b].append(a)

    # The input is a tree, so skipping the parent prevents revisits.
    parent = [0] * (size + 1)
    order = [1]
    for vertex in order:
        for child in neighbors[vertex]:
            if child != parent[vertex]:
                parent[child] = vertex
                order.append(child)
    del neighbors, order

    # Index zero has no parent broadcasts. Its direct value is never read.
    # Broadcasts reach children through their parent's total.
    broadcast = [0] * (size + 1)
    for _ in range(int(read())):
        kind, vertex = map(int, read().split())
        above = parent[vertex]
        value = (direct[vertex] + broadcast[above]) % MODULUS
        if kind == QUERY:
            print(value)
        else:
            broadcast[vertex] = (broadcast[vertex] + value) % MODULUS
            direct[above] = (direct[above] + value) % MODULUS


if __name__ == "__main__":
    main()
