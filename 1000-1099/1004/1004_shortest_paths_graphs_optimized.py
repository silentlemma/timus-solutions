import sys

INF = 32767
END_OF_INPUT = -1
MIN_CYCLE_LENGTH = 3


def solve(size, roads, tokens):
    direct = [[INF] * size for _ in range(size)]
    for vertex, row in enumerate(direct):
        row[vertex] = 0
    for _ in range(roads):
        a, b, length = next(tokens) - 1, next(tokens) - 1, next(tokens)
        if length < direct[a][b]:
            direct[a][b] = direct[b][a] = length

    distance = [row[:] for row in direct]
    following = [bytearray(range(size)) for _ in range(size)]
    best = INF
    cycle = []
    for k in range(size):
        edges = direct[k]
        for i in range(k):
            left = edges[i]
            if left >= best:
                continue
            row = distance[i]
            for j in range(i + 1, k):
                length = left + edges[j] + row[j]
                if length < best:
                    best = length
                    cycle = [i]
                    while cycle[-1] != j:
                        cycle.append(following[cycle[-1]][j])
                    cycle.append(k)
                    if best == MIN_CYCLE_LENGTH:
                        return cycle

        # A path already as long as the best cycle cannot improve it.
        middle = distance[k]
        for i, left in enumerate(middle):
            if i == k or left >= best:
                continue
            row, hop = distance[i], following[i]
            via = hop[k]
            for j in range(i + 1, size):
                length = left + middle[j]
                if length < best and length < row[j]:
                    row[j] = distance[j][i] = length
                    hop[j] = via
                    following[j][i] = following[j][k]
    return cycle


def main():
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    for size in tokens:
        if size == END_OF_INPUT:
            break
        cycle = solve(size, next(tokens), tokens)
        print(" ".join(str(vertex + 1) for vertex in cycle) if cycle else "No solution.")


if __name__ == "__main__":
    main()
