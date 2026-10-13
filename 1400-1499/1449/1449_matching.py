import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # the Hungarian method minimises the cost -A; rows and columns from 1, 0 is a helper
    cost = [[0] * (n + 1)] + [
        [0] + [-int(x) for x in data[1 + i * n : 1 + (i + 1) * n]] for i in range(n)
    ]
    inf = float("inf")
    u, v = [0] * (n + 1), [0] * (n + 1)
    match = [0] * (n + 1)  # match[j]: the row matched to column j
    way = [0] * (n + 1)
    for i in range(1, n + 1):
        match[0] = i
        j0 = 0
        low = [inf] * (n + 1)
        used = [False] * (n + 1)
        while match[j0]:
            used[j0] = True
            i0, delta, j1 = match[j0], inf, 0
            row, ui0 = cost[i0], u[match[j0]]
            for j in range(1, n + 1):
                if not used[j]:
                    cur = row[j] - ui0 - v[j]
                    if cur < low[j]:
                        low[j], way[j] = cur, j0
                    if low[j] < delta:
                        delta, j1 = low[j], j
            for j in range(n + 1):
                if used[j]:
                    u[match[j]] += delta
                    v[j] -= delta
                else:
                    low[j] -= delta
            j0 = j1
        while j0:
            j1 = way[j0]
            match[j0] = match[j1]
            j0 = j1
    # u + v <= -A, so the bribes -u, -v cover every credit and add up to the
    # heaviest matching; shifting them until a row bribe is 0 keeps all >= 0
    rows, cols = [-x for x in u[1:]], [-x for x in v[1:]]
    shift = min(rows)
    print(" ".join(str(x - shift) for x in rows))
    print(" ".join(str(x + shift) for x in cols))


main()
