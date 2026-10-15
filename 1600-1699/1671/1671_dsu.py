import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    ends = data[2:2 + 2 * m]
    start = 2 + 2 * m
    q = int(data[start])
    cuts = [int(w) - 1 for w in data[start + 1:start + 1 + q]]
    parent = list(range(n + 1))

    def find(v):
        root = v
        while parent[root] != root:
            root = parent[root]
        while parent[v] != root:
            parent[v], v = root, parent[v]
        return root

    pieces = n

    def join(i):
        nonlocal pieces
        a, b = find(int(ends[2 * i])), find(int(ends[2 * i + 1]))
        if a != b:
            parent[a] = b
            pieces -= 1

    # run backwards: start from the web after all cuts and put the threads
    # back one by one, last cut first
    cut = bytearray(m)
    for i in cuts:
        cut[i] = 1
    for i in range(m):
        if not cut[i]:
            join(i)
    answers = []
    for i in reversed(cuts):
        answers.append(pieces)
        join(i)
    print(" ".join(map(str, reversed(answers))))


main()
