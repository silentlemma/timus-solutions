import random
import sys


MIN_SIZE = 2
MAX_SIZE = 300
MAX_MISSING = 100_000
SMALL_SIZE = 7
MEDIUM_MIN = 30
MEDIUM_MAX = 80
SPARSE_DENOMINATOR = 10


def grid_edges(rows, columns):
    edges = []
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            if row < rows:
                edges.append((row, column, row + 1, column))
            if column < columns:
                edges.append((row, column, row, column + 1))
    return edges


def generate(mode, rng):
    if mode in ("small", "dense"):
        rows = rng.randint(MIN_SIZE, SMALL_SIZE)
        columns = rng.randint(MIN_SIZE, SMALL_SIZE)
        edges = grid_edges(rows, columns)
        if mode == "small":
            missing = [edge for edge in edges if rng.randrange(SPARSE_DENOMINATOR) == 0]
        else:
            count = rng.randint(len(edges) // 2, len(edges))
            missing = rng.sample(edges, count)
    elif mode == "medium":
        rows = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        columns = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        edges = grid_edges(rows, columns)
        missing = [edge for edge in edges if rng.randrange(SPARSE_DENOMINATOR) == 0]
    elif mode in ("max-open", "max-missing", "max-alive"):
        rows = columns = MAX_SIZE
        if mode == "max-open":
            missing = []
        else:
            edges = grid_edges(rows, columns)
            if mode == "max-alive":
                edges = [edge for edge in edges if all(1 < value < MAX_SIZE for value in edge)]
            missing = rng.sample(edges, MAX_MISSING)
    elif mode == "thin":
        rows, columns = MIN_SIZE, MAX_SIZE
        missing = [
            (1, column, rows, column) for column in range(2, columns) if rng.randrange(2) == 0
        ]
        if rng.randrange(2) == 0:
            rows, columns = columns, rows
            missing = [(b, a, d, c) for a, b, c, d in missing]
    elif mode == "bottleneck":
        rows = rng.randint(MEDIUM_MIN, MAX_SIZE)
        columns = rng.randint(MEDIUM_MIN, MAX_SIZE)
        pivot = (rows // 2 + 1, columns // 2 + 1)
        diagonal = sum(pivot)
        missing = [
            edge
            for edge in grid_edges(rows, columns)
            if edge[0] + edge[1] == diagonal - 1 and edge[2:] != pivot
        ]
    else:
        raise SystemExit("unknown mode")
    rng.shuffle(missing)
    return rows, columns, missing


def main():
    if len(sys.argv) != 1 + 2:
        raise SystemExit("usage: python gen.py MODE SEED")
    rng = random.Random(int(sys.argv[2]))
    rows, columns, missing = generate(sys.argv[1], rng)
    lines = [f"{rows} {columns}", str(len(missing))]
    for edge in missing:
        a, b, c, d = edge
        if rng.randrange(2) == 0:
            a, b, c, d = c, d, a, b
        lines.append(f"{a} {b} {c} {d}")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
