from sys import stdin, stdout

import pypyjit

pypyjit.set_param("off")

VERTICES = 1000
# A negative root packs twice its component size and its edge-count parity.
parent = [-2] * (VERTICES + 1)


def find(vertex):
    while parent[vertex] >= 0:
        next_vertex = parent[vertex]
        if parent[next_vertex] >= 0:
            parent[vertex] = parent[next_vertex]
        vertex = next_vertex
    return vertex


numbers = (int(word) for line in stdin for word in line.split())
odd = 0
for a, b in zip(numbers, numbers):
    a, b = find(a), find(b)
    first = -parent[a]
    odd -= first & 1
    if a != b:
        second = -parent[b]
        odd -= second & 1
        if first // 2 < second // 2:
            a, b = b, a
        size = first // 2 + second // 2
        parity = (first ^ second ^ 1) & 1
        parent[b] = a
        parent[a] = -(2 * size + parity)
    else:
        parity = (first ^ 1) & 1
        parent[a] = -(first // 2 * 2 + parity)
    odd += parity
stdout.write("1\n" if odd == 0 else "0\n")
