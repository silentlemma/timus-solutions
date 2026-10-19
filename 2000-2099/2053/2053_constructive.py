import math

GRID = 4
VERTICES = GRID * GRID
OUTER_SCALE = 900
DIMENSION = 2
ROUNDING_OFFSET = 0.5


def make_graph():
    graph = [[0] * VERTICES for _ in range(VERTICES)]

    def connect(a, b):
        graph[a][b] = graph[b][a] = 1

    for row in range(GRID):
        for column in range(GRID):
            vertex = row * GRID + column
            if column + 1 < GRID:
                connect(vertex, vertex + 1)
            if row + 1 < GRID:
                connect(vertex, vertex + GRID)
            if row + 1 < GRID and column + 1 < GRID:
                connect(vertex, vertex + GRID + 1)
    corners = [0, GRID - 1, VERTICES - 1, VERTICES - GRID]
    for side, a in enumerate(corners):
        d = corners[(side + 1) % GRID]
        step = (d - a) // (GRID - 1)
        connect(a, d)
        connect(a, d - step)
    connect(corners[1], corners[-1])
    return graph, corners


def solve():
    graph, corners = make_graph()
    fixed = [None] * VERTICES
    fixed[corners[0]] = (-OUTER_SCALE, -OUTER_SCALE)
    fixed[corners[1]] = (OUTER_SCALE, -OUTER_SCALE)
    fixed[corners[-1]] = (0, OUTER_SCALE)
    inside = [v for v in range(VERTICES) if fixed[v] is None]
    index = {v: i for i, v in enumerate(inside)}
    size = len(inside)
    matrix = [[0.0] * (size + DIMENSION) for _ in inside]
    for vertex in inside:
        row = matrix[index[vertex]]
        row[index[vertex]] = float(sum(graph[vertex]))
        for neighbour in range(VERTICES):
            if not graph[vertex][neighbour]:
                continue
            if fixed[neighbour] is None:
                row[index[neighbour]] -= 1
            else:
                for axis in range(DIMENSION):
                    row[size + axis] += fixed[neighbour][axis]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(matrix[row][column]))
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        divisor = matrix[column][column]
        matrix[column] = [value / divisor for value in matrix[column]]
        for row in range(size):
            if row != column:
                factor = matrix[row][column]
                matrix[row] = [a - factor * b for a, b in zip(matrix[row], matrix[column])]
    points = []
    for vertex in range(VERTICES):
        if fixed[vertex] is not None:
            points.append(fixed[vertex])
        else:
            points.append(
                tuple(math.floor(value + ROUNDING_OFFSET) for value in matrix[index[vertex]][size:])
            )
    return points, graph


def main():
    points, graph = solve()
    for point in points:
        print(*point)
    for row in graph:
        print("".join(map(str, row)))


if __name__ == "__main__":
    main()
