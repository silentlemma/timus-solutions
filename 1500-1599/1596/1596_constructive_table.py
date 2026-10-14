"""Print the table TOURS of the solutions: a closed knight's tour of every
block with sides from 6 to 11 and an even area, one direction per cell, row
by row, as "rows columns directions".

Each tour also moves between (1, C-2) and (3, C-1) and between (R-2, 1) and
(R-1, 3), the moves the solutions drop to join blocks. A depth-first search
with Warnsdorff's ordering (fewest onward moves first, ties broken by a
seeded random choice) starts with the first of these moves and is restarted
after a bounded number of steps until it closes a tour that has both.
"""

import random
import sys

MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
SMALLEST = 6
LARGEST = 11
SEED = 2024
STEPS = 20000  # search steps before a restart


def tour(rows, cols, rng):
    cells = rows * cols

    def neighbours(r, c):
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    start = (1, cols - 2)
    second = (3, cols - 1)
    wanted = {((rows - 2, 1), (rows - 1, 3)), ((rows - 1, 3), (rows - 2, 1))}
    while True:
        seen = {start, second}
        path = [start, second]
        steps = [0]

        def free_degree(cell):
            return sum(1 for x in neighbours(*cell) if x not in seen)

        def extend():
            steps[0] += 1
            if steps[0] > STEPS:
                return False
            if len(path) == cells:
                closed = start in set(neighbours(*path[-1]))
                pairs = set(zip(path, path[1:])) | {(path[-1], path[0])}
                return closed and bool(pairs & wanted)
            options = [x for x in neighbours(*path[-1]) if x not in seen]
            rng.shuffle(options)
            options.sort(key=free_degree)
            for x in options:
                seen.add(x)
                path.append(x)
                if extend():
                    return True
                path.pop()
                seen.discard(x)
            return False

        if extend():
            return path


def directions(rows, cols, path):
    out = [0] * (rows * cols)
    for i, (r, c) in enumerate(path):
        nr, nc = path[(i + 1) % len(path)]
        out[r * cols + c] = MOVES.index((nr - r, nc - c)) + 1
    return "".join(map(str, out))


def main():
    sys.setrecursionlimit(10000)
    rng = random.Random(SEED)
    for rows in range(SMALLEST, LARGEST + 1):
        for cols in range(SMALLEST, LARGEST + 1):
            if rows * cols % 2:
                continue
            print(rows, cols, directions(rows, cols, tour(rows, cols, rng)), flush=True)


main()
