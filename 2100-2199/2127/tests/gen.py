import random
import sys


MAX_N = 200_000
MAX_EXTRA = 50
MAX_CYCLES = MAX_EXTRA + 1
SMALL_N = 60
TREE_N = 500
DENSE_N = 12
CUBIC_MIN = 4
CUBIC_MAX = 100
SUBDIVIDE_MAX = 8
THETA_MAX_LENGTH = 12
SMALL_COMPONENTS = 10
TRIANGLE = 3
SQUARE = 4
HEXAGON = 6


def cycle_edges(size, first=0):
    return [(first + vertex, first + (vertex + 1) % size) for vertex in range(size)]


def add_path(edges, first, last, inside, next_vertex):
    previous = first
    for _ in range(inside):
        edges.append((previous, next_vertex))
        previous = next_vertex
        next_vertex += 1
    edges.append((previous, last))
    return next_vertex


def cubic_graph(rng, size):
    edges = cycle_edges(size)
    occupied = {tuple(sorted(edge)) for edge in edges}
    vertices = list(range(size))
    while True:
        rng.shuffle(vertices)
        matching = list(zip(vertices[::2], vertices[1::2]))
        if all(tuple(sorted(edge)) not in occupied for edge in matching):
            return edges + matching


def cubic_cycles(rng):
    first_size = CUBIC_MAX // 2 - 1
    second_size = CUBIC_MAX - first_size
    edges = cycle_edges(first_size) + cycle_edges(second_size, first_size)
    occupied = {tuple(sorted(edge)) for edge in edges}
    halves = [list(range(first_size)), list(range(first_size, CUBIC_MAX))]
    leftovers = []
    for vertices in halves:
        rng.shuffle(vertices)
        leftovers.append(vertices.pop())
        while True:
            rng.shuffle(vertices)
            matching = list(zip(vertices[::2], vertices[1::2]))
            if all(tuple(sorted(edge)) not in occupied for edge in matching):
                edges.extend(matching)
                break
    edges.append(tuple(leftovers))
    return edges


def dense_core():
    edges = []
    for first in range(DENSE_N):
        for last in range(first + 1, DENSE_N):
            if first != 0 or last > SQUARE:
                edges.append((first, last))
    return DENSE_N, edges


def wheel():
    size = MAX_CYCLES + 1
    edges = cycle_edges(MAX_CYCLES, 1)
    edges.extend((0, vertex) for vertex in range(1, size))
    return size, edges


def attach_pairs(rng, size, edges, target):
    while size < target:
        anchor = rng.randrange(size)
        edges.append((anchor, size))
        edges.append((size, size + 1))
        size += 2
    return size, edges


def subdivide(rng, size, edges, additions):
    result = []
    for (first, last), inside in zip(edges, additions):
        size = add_path(result, first, last, inside, size)
    return size, result


def pruning_graph(rng, large):
    edges = [(0, 1)]
    size = 2
    count = MAX_CYCLES if large else rng.randint(1, SMALL_COMPONENTS)
    for index in range(count):
        length = TRIANGLE if large else rng.randint(TRIANGLE, THETA_MAX_LENGTH)
        if large and index == count - 1:
            length = HEXAGON
        edges.extend(cycle_edges(length, size))
        edges.append((0, size))
        size += length
    if large:
        size, edges = attach_pairs(rng, size, edges, MAX_N)
    return size, edges


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small" or mode == "dense":
        limit = SMALL_N if mode == "small" else DENSE_N
        size = rng.randint(1, limit)
        edges = [(vertex, rng.randrange(vertex)) for vertex in range(1, size)]
        occupied = {tuple(sorted(edge)) for edge in edges}
        available = size * (size - 1) // 2 - len(edges)
        extra = rng.randint(0, min(MAX_CYCLES, available))
        if mode == "dense":
            extra = min(MAX_CYCLES, available)
        while extra:
            first, last = rng.sample(range(size), 2)
            edge = tuple(sorted((first, last)))
            if edge not in occupied:
                occupied.add(edge)
                edges.append(edge)
                extra -= 1
    elif mode == "tree":
        size = rng.randint(1, TREE_N)
        edges = [(vertex, rng.randrange(vertex)) for vertex in range(1, size)]
    elif mode == "path_max":
        size = MAX_N
        edges = [(vertex - 1, vertex) for vertex in range(1, size)]
    elif mode == "star_max":
        size = MAX_N
        edges = [(0, vertex) for vertex in range(1, size)]
    elif mode in ("cycle_max", "cycle_odd_max", "cycle_even_max"):
        size = MAX_N
        if mode == "cycle_odd_max":
            size -= 1
        elif mode == "cycle_even_max":
            size -= 2
        edges = cycle_edges(size)
    elif mode == "cubic" or mode == "subdivide":
        size = 2 * rng.randint(CUBIC_MIN // 2, CUBIC_MAX // 2)
        edges = cubic_graph(rng, size)
        if mode == "subdivide":
            additions = [rng.randint(0, SUBDIVIDE_MAX) for _ in edges]
            size, edges = subdivide(rng, size, edges, additions)
    elif mode == "cubic_max" or mode == "cubic_subdivide_max":
        size = CUBIC_MAX
        if mode == "cubic_max":
            edges = cubic_graph(rng, size)
            additions = [0] * len(edges)
        else:
            edges = cubic_cycles(rng)
            additions = [1] * CUBIC_MAX + [0] * (len(edges) - CUBIC_MAX)
        blocks = (MAX_N - size - sum(additions)) // SQUARE
        for index in range(len(edges) - 1):
            amount = rng.randint(0, blocks)
            additions[index] += SQUARE * amount
            blocks -= amount
        additions[-1] += SQUARE * blocks
        size, edges = subdivide(rng, size, edges, additions)
    elif mode == "theta" or mode == "theta_max":
        paths = rng.randint(2, MAX_CYCLES + 1)
        if mode == "theta_max":
            paths = MAX_CYCLES + 1
            additions = [1] * paths
            remaining = MAX_N - 2 - paths
            for index in range(paths - 1):
                amount = rng.randint(0, remaining)
                additions[index] += amount
                remaining -= amount
            additions[-1] += remaining
            rng.shuffle(additions)
        else:
            additions = [rng.randint(1, THETA_MAX_LENGTH - 1) for _ in range(paths)]
        size = 2
        edges = []
        for inside in additions:
            size = add_path(edges, 0, 1, inside, size)
    elif mode == "wheel_max" or mode == "wheel_subdivide_max":
        size, edges = wheel()
        if mode == "wheel_max":
            previous = 0
            while size < MAX_N:
                edges.append((previous, size))
                previous = size
                size += 1
        else:
            blocks = (MAX_N - size) // SQUARE
            additions = [0] * len(edges)
            for index in range(len(edges) - 1):
                amount = rng.randint(0, blocks)
                additions[index] = SQUARE * amount
                blocks -= amount
            additions[-1] = SQUARE * blocks
            rng.shuffle(additions)
            size, edges = subdivide(rng, size, edges, additions)
    elif mode == "leaf_pairs_max":
        size, edges = dense_core()
        size, edges = attach_pairs(rng, size, edges, MAX_N)
    elif mode == "prune" or mode == "prune_max":
        size, edges = pruning_graph(rng, mode == "prune_max")
    else:
        raise ValueError("unknown generator mode: " + mode)

    labels = list(range(1, size + 1))
    rng.shuffle(labels)
    result = []
    for first, last in edges:
        if rng.randrange(2):
            first, last = last, first
        result.append((labels[first], labels[last]))
    rng.shuffle(result)
    return size, result


def main():
    mode, seed = sys.argv[1:]
    size, edges = generate(mode, int(seed))
    output = [str(size) + " " + str(len(edges))]
    output.extend(str(first) + " " + str(last) for first, last in edges)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
