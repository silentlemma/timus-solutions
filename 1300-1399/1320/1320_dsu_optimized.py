from os import _exit, write

VERTICES = 1000


def decomposable(values):
    parent = [-2] * (VERTICES + 1)

    def find(vertex):
        while parent[vertex] >= 0:
            following = parent[vertex]
            if parent[following] >= 0:
                parent[vertex] = parent[following]
            vertex = following
        return vertex

    values = iter(values)
    odd = 0
    for a, b in zip(values, values):
        a, b = find(a), find(b)
        first = -parent[a]
        odd -= first & 1
        if a != b:
            second = -parent[b]
            odd -= second & 1
            if first < second:
                a, b = b, a
            parity = (first ^ second ^ 1) & 1
            parent[b] = a
            parent[a] = -((first & ~1) + (second & ~1) + parity)
        else:
            parity = (first ^ 1) & 1
            parent[a] = -(first ^ 1)
        odd += parity
    return odd == 0


values = map(int, open(0, "rb", buffering=0).read().split())
write(1, b"1\n" if decomposable(values) else b"0\n")
_exit(0)
