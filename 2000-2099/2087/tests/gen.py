"""Generate a deterministic railway tree and a valid train schedule."""

import random
import sys

MAX_SIDE = 500
MAX_TRAINS = 200_000
MAX_TIME = 10**9
SMALL_SIDE = 10
SMALL_TRAINS = 100
BATCH_TRAINS = 1_000
ARM_SIDE = 3
ARGUMENTS = 3
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
TURN = {0: "F", 1: "R", len(DIRECTIONS) - 1: "L"}


def add_edge(adjacency, first, second):
    adjacency[first].append(second)
    adjacency[second].append(first)


def relative(parent, vertex, child, width):
    before = (vertex // width - parent // width, vertex % width - parent % width)
    after = (child // width - vertex // width, child % width - vertex % width)
    return TURN[(DIRECTIONS.index(after) - DIRECTIONS.index(before)) % len(DIRECTIONS)]


def rooted(adjacency, depot):
    parent = [-1] * len(adjacency)
    parent[depot] = depot
    order = [depot]
    for vertex in order:
        for child in adjacency[vertex]:
            if parent[child] == -1:
                parent[child] = vertex
                order.append(child)
    return parent, order


def random_tree(height, width, rng, sparse=False):
    adjacency = [[] for _ in range(height * width)]
    start = rng.randrange(height * width)
    visited = {start}
    stack = [start]
    limit = rng.randint(2, height * width) if sparse else height * width
    while stack and len(visited) < limit:
        vertex = stack[-1]
        row, column = divmod(vertex, width)
        available = []
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, column + dc
            child = nr * width + nc
            if 0 <= nr < height and 0 <= nc < width and child not in visited:
                available.append(child)
        if available:
            child = rng.choice(available)
            add_edge(adjacency, vertex, child)
            visited.add(child)
            stack.append(child)
        else:
            stack.pop()
    leaves = [vertex for vertex in visited if len(adjacency[vertex]) == 1]
    return adjacency, rng.choice(sorted(leaves))


def snake():
    height = width = MAX_SIDE
    adjacency = [[] for _ in range(height * width)]
    path = []
    for row in range(height - 1):
        columns = range(width) if row % 2 == 0 else range(width - 1, -1, -1)
        for column in columns:
            if row != height - 2 or column != width - 1:
                path.append(row * width + column)
    branch = (height - 1) * width + width - 2
    path.append(branch)
    for first, second in zip(path, path[1:]):
        add_edge(adjacency, first, second)
    left = list(range(branch, (height - 1) * width - 1, -1))
    for first, second in zip(left, left[1:]):
        add_edge(adjacency, first, second)
    right = branch + 1
    upper = right - width
    add_edge(adjacency, branch, right)
    add_edge(adjacency, right, upper)
    return height, width, adjacency, path[0], [upper, left[-1]], branch


def comb():
    height = width = MAX_SIDE
    adjacency = [[] for _ in range(height * width)]
    for column in range(width):
        if column:
            add_edge(adjacency, column - 1, column)
        for row in range(1, height):
            add_edge(adjacency, (row - 1) * width + column, row * width + column)
    depot = (height - 1) * width
    stations = [height * width - 2, height * width - 1]
    return height, width, adjacency, depot, stations, width - 2


def cross():
    height = width = ARM_SIDE
    adjacency = [[] for _ in range(height * width)]
    center = width + 1
    leaves = [1, center + 1, center + width]
    depot = center - 1
    for leaf in [depot] + leaves:
        add_edge(adjacency, center, leaf)
    return height, width, adjacency, depot, leaves, center


def sweep(adjacency, depot, width, count):
    parent = [-1] * len(adjacency)
    parent[depot] = depot
    stack = [depot]
    stations = []
    override = {}
    while stack:
        vertex = stack.pop()
        children = [child for child in adjacency[vertex] if child != parent[vertex]]
        if vertex != depot:
            if children:
                override[vertex] = relative(parent[vertex], vertex, children[0], width)
            else:
                stations.append(vertex)
        for child in children:
            parent[child] = vertex
        stack.extend(reversed(children))
    destinations = []
    index, step = 0, 1
    for _ in range(count):
        destinations.append(stations[index])
        if len(stations) > 1:
            if not 0 <= index + step < len(stations):
                step = -step
            index += step
    return override, destinations


def make_case(mode, seed):
    rng = random.Random(seed)
    override = {}
    if mode == "sweep":
        height = width = MAX_SIDE
        adjacency, depot = random_tree(height, width, rng)
        count = MAX_TRAINS
        override, destinations = sweep(adjacency, depot, width, count)
        times = range(MAX_TIME - count + 1, MAX_TIME + 1)
    elif mode in {"snake", "snake_repeat", "comb", "max_output"}:
        constructor = {
            "snake": snake,
            "snake_repeat": snake,
            "comb": comb,
            "max_output": cross,
        }[mode]
        height, width, adjacency, depot, stations, branch = constructor()
        parent, _ = rooted(adjacency, depot)
        first = stations[0]
        child = first
        while parent[child] != depot:
            vertex = parent[child]
            override[vertex] = relative(parent[vertex], vertex, child, width)
            child = vertex
        child = first
        while parent[child] != branch:
            child = parent[child]
        wanted = relative(parent[branch], branch, child, width)
        alternatives = [
            relative(parent[branch], branch, vertex, width)
            for vertex in adjacency[branch]
            if vertex != parent[branch]
        ]
        override[branch] = (
            wanted
            if mode == "snake_repeat"
            else next(letter for letter in alternatives if letter != wanted)
        )
        count = MAX_TRAINS
        destinations = [
            stations[0] if mode == "snake_repeat" else stations[i % len(stations)]
            for i in range(count)
        ]
        times = range(MAX_TIME - count + 1, MAX_TIME + 1)
    elif mode in {"random", "sparse", "batches", "repeats", "zero"}:
        height, width = rng.randint(2, SMALL_SIDE), rng.randint(2, SMALL_SIDE)
        adjacency, depot = random_tree(height, width, rng, mode == "sparse")
        stations = [
            vertex
            for vertex, neighbors in enumerate(adjacency)
            if len(neighbors) == 1 and vertex != depot
        ]
        count = rng.randint(1, SMALL_TRAINS)
        if mode == "batches":
            count = BATCH_TRAINS
        elif mode == "repeats":
            count = MAX_TRAINS
        destinations = []
        target = rng.choice(stations)
        for _ in range(count):
            if mode not in {"repeats", "zero"} and rng.randrange(SMALL_SIDE) == 0:
                target = rng.choice(stations)
            destinations.append(target)
        if mode in {"random", "sparse"}:
            destinations = [rng.choice(stations) for _ in range(count)]
        times = sorted(rng.sample(range(1, MAX_TIME + 1), count))
        if mode == "zero":
            parent, _ = rooted(adjacency, depot)
            child = destinations[0]
            while parent[child] != depot:
                vertex = parent[child]
                override[vertex] = relative(parent[vertex], vertex, child, width)
                child = vertex
    else:
        raise ValueError("unknown mode: " + mode)

    parent, order = rooted(adjacency, depot)
    cells = [["."] * (2 * width - 1) for _ in range(2 * height - 1)]
    for vertex in order:
        row, column = divmod(vertex, width)
        if vertex == depot:
            letter = "S"
        elif len(adjacency[vertex]) == 1:
            letter = "X"
        else:
            choices = [
                relative(parent[vertex], vertex, child, width)
                for child in adjacency[vertex]
                if child != parent[vertex]
            ]
            letter = override.get(vertex, rng.choice(choices))
        cells[2 * row][2 * column] = letter
        if vertex != depot:
            previous_row, previous_column = divmod(parent[vertex], width)
            edge = "|" if column == previous_column else "-"
            cells[row + previous_row][column + previous_column] = edge
    lines = [f"{height} {width}"]
    lines.extend("".join(row) for row in cells)
    lines.append(str(count))
    lines.extend(
        f"{time} {vertex // width + 1} {vertex % width + 1}"
        for time, vertex in zip(times, destinations)
    )
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != ARGUMENTS:
        raise SystemExit("usage: python gen.py MODE SEED")
    sys.stdout.write(make_case(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
