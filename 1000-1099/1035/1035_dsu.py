import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    rows = data[2:]
    # the vertices of the grid are (i, j) -> i * (m + 1) + j; balance[v] is the number
    # of front stitches minus the number of back stitches that end at v
    width = m + 1
    vertices = (n + 1) * width
    parent = list(range(vertices))
    balance = [0] * vertices
    stitched = [False] * vertices

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    back, slash, cross = ord("\\"), ord("/"), ord("X")
    for side in range(2):
        sign = 1 if side == 0 else -1
        for i in range(n):
            row = rows[side * n + i]
            top = i * width
            for j in range(m):
                c = row[j]
                stitches = []
                if c == back or c == cross:
                    stitches.append((top + j, top + width + j + 1))
                if c == slash or c == cross:
                    stitches.append((top + width + j, top + j + 1))
                for a, b in stitches:
                    balance[a] += sign
                    balance[b] += sign
                    stitched[a] = stitched[b] = True
                    parent[find(a)] = find(b)
    # a group needs one thread per two unbalanced stitch ends, and at least one
    ends = {}
    for v in range(vertices):
        if stitched[v]:
            r = find(v)
            ends[r] = ends.get(r, 0) + abs(balance[v])
    print(sum(e // 2 if e else 1 for e in ends.values()))


main()
