import sys

MODULUS = 1_000_000_007


class Network:
    def __init__(self, initial, edges, root=0):
        size = len(initial)
        neighbors = [[] for _ in range(size)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        parent = [-1] * size
        parent[root] = root
        order = [root]
        for vertex in order:
            for neighbor in neighbors[vertex]:
                if parent[neighbor] < 0:
                    parent[neighbor] = vertex
                    order.append(neighbor)
        self.direct = list(initial)
        self.broadcast = [0] * size
        self.parent = parent
        self.root = root

    def process(self, kind, vertex):
        value = self.direct[vertex]
        if vertex != self.root:
            value += self.broadcast[self.parent[vertex]]
            if value >= MODULUS:
                value -= MODULUS
        if kind == 2:
            return value
        self.broadcast[vertex] += value
        if self.broadcast[vertex] >= MODULUS:
            self.broadcast[vertex] -= MODULUS
        if vertex != self.root:
            above = self.parent[vertex]
            self.direct[above] += value
            if self.direct[above] >= MODULUS:
                self.direct[above] -= MODULUS
        return -1


def main():
    read = sys.stdin.buffer.readline
    first = read()
    if not first:
        return
    size = int(first)
    initial = list(map(int, read().split()))

    def edges():
        for _ in range(size - 1):
            a, b = map(int, read().split())
            yield a - 1, b - 1

    network = Network(initial, edges())
    del initial
    answers = []
    count = int(read())
    for _ in range(count):
        kind, vertex = map(int, read().split())
        answer = network.process(kind, vertex - 1)
        if answer >= 0:
            answers.append(str(answer))
    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
