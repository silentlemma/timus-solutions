"""Generate impossible simple graphs: their unique answer is -1.

Every mode has an even total and at least two odd-edge components.
"""

import itertools
import random
import sys

MAX_VERTEX = 100000
MAX_EDGES = 100000
MIN_CYCLE = 3
MINIMUM_VERTICES = 4
DENSE_VERTICES = 448
EXTRA_EDGES = 3
SMALL_VERTICES = 80
MIXED_COMPONENTS = 10
LATE_RESERVED_VERTICES = 6
ARGUMENT_COUNT = 2


def path(edges, start, length):
    edges.extend((vertex, vertex + 1) for vertex in range(start, start + length))


def star(edges, start, degree):
    edges.extend((start, start + step) for step in range(1, degree + 1))


def cycle(edges, start, length):
    path(edges, start, length - 1)
    edges.append((start, start + length - 1))


def make_graph(mode, rng):
    edges = []
    if mode == "minimum":
        edges = [(0, 1), (2, MINIMUM_VERTICES - 1)]
        count = MINIMUM_VERTICES
    elif mode in ("odd_paths", "odd_stars"):
        total = MAX_VERTEX - 2
        first = rng.randrange(1, total, 2)
        second = total - first
        build = path if mode == "odd_paths" else star
        build(edges, 0, first)
        build(edges, first + 1, second)
        count = MAX_VERTEX
    elif mode == "odd_cycles":
        first = rng.randrange(MIN_CYCLE, MAX_VERTEX - MIN_CYCLE + 1, 2)
        cycle(edges, 0, first)
        cycle(edges, first, MAX_VERTEX - first)
        count = MAX_VERTEX
    elif mode == "dense":
        edges = list(
            itertools.islice(itertools.combinations(range(DENSE_VERTICES), 2), MAX_EDGES - 1)
        )
        edges.append((DENSE_VERTICES, DENSE_VERTICES + 1))
        count = DENSE_VERTICES + 2
    elif mode == "sparse":
        main_count = MAX_EDGES - EXTRA_EDGES
        edges = [(vertex, rng.randrange(vertex)) for vertex in range(1, main_count)]
        used = {tuple(sorted(edge)) for edge in edges}
        while len(edges) < MAX_EDGES - 1:
            a, b = rng.sample(range(main_count), 2)
            edge = (min(a, b), max(a, b))
            if edge not in used:
                used.add(edge)
                edges.append(edge)
        edges.append((main_count, main_count + 1))
        count = main_count + 2
    elif mode == "mixed":
        count = 0
        component_count = 2 * rng.randint(1, MIXED_COMPONENTS // 2)
        for _ in range(component_count):
            size = rng.randint(2, SMALL_VERTICES)
            component = {(vertex, vertex + 1) for vertex in range(size - 1)}
            maximum = size * (size - 1) // 2
            target = rng.randint(size - 1, min(maximum, 2 * size))
            if target % 2 == 0:
                target -= 1
            if target < size - 1:
                target += 2
            while len(component) < target:
                a, b = rng.sample(range(size), 2)
                component.add((min(a, b), max(a, b)))
            edges.extend((a + count, b + count) for a, b in sorted(component))
            count += size
    elif mode == "many_components":
        edges = [(vertex, vertex + 1) for vertex in range(0, MAX_VERTEX, 2)]
        count = MAX_VERTEX
    elif mode == "late_failure":
        main_edges = MAX_VERTEX - LATE_RESERVED_VERTICES
        path(edges, 0, main_edges)
        edges.extend(
            (
                (MAX_VERTEX - MINIMUM_VERTICES, MAX_VERTEX - MIN_CYCLE),
                (MAX_VERTEX - 2, MAX_VERTEX - 1),
            )
        )
        count = MAX_VERTEX
    else:
        raise ValueError("unknown mode: " + mode)
    return edges, count


def generate(mode, seed):
    rng = random.Random(seed)
    edges, count = make_graph(mode, rng)
    if mode == "late_failure":
        labels = list(range(1, count + 1))
        main_edges = len(edges) - 2
        prefix = edges[:main_edges]
        rng.shuffle(prefix)
        edges[:main_edges] = prefix
    else:
        labels = rng.sample(range(1, MAX_VERTEX), count - 1)
        labels.append(MAX_VERTEX)
        rng.shuffle(labels)
        rng.shuffle(edges)
    lines = []
    for a, b in edges:
        if rng.randrange(2):
            a, b = b, a
        lines.append(f"{labels[a]} {labels[b]}")
    sys.stdout.write("\n".join(lines) + "\n")


def main():
    if len(sys.argv) != ARGUMENT_COUNT + 1:
        raise SystemExit("usage: python gen.py MODE SEED")
    generate(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    main()
